"""Update the directive we use to build the team page with latest results.

This must currently be manually run. We should automate it in the future.
To run it, you must have the GitHub CLI tool installed and authenticated.

- To install, see: https://cli.github.com/manual/installation
- To authenticate, see: https://cli.github.com/manual/gh_auth_login
"""

from subprocess import run
from shlex import split
from json import loads
from textwrap import dedent
from pathlib import Path

# Pull latest team from github
print("Updating team page...")
teams = [
  "steering-council",
  "core-team",
  "emeritus-team",
]
for team in teams:
  path_out = Path(__file__).parent / f"../team/members/team-members-{team}.txt"
  path_out.parent.mkdir(exist_ok=True)
  md = dedent("""
  `````{{grid}} 1 2 3 3
  :gutter: 4

  {members}
  `````
  """)
  resp = run(split(f"gh api /orgs/executablebooks/teams/{team}/members"), capture_output=True)
  members = loads(resp.stdout)
  if len(members) == 0:
    print(f"Found no team members for {team}...")
    path_out.write_text("_This section is currently empty as no team member has formally left the project, we leave it here to encourage these practices moving forward_.")
    continue
  member_strings = []
  for member in members:
    member_str = dedent("""
    ````{{grid-item-card}}
    :link: {html_url}
    :text-align: center
    :class-footer: sd-fs-6

    ```{{image}} https://github.com/{login}.png
    :class: sd-rounded-circle
    :alt: {login} avatar
    ```
    +++
    **@{login}**
    ````
    """)
    member_str = member_str.format(html_url=member["html_url"], login=member["login"])
    member_strings.append(member_str)
  md = md.format(members="\n\n".join(member_strings))
  path_out.write_text(md)
print(f"Finished updating team at {path_out.parent.resolve()}/.")