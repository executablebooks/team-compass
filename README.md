# The Executable Books Team Compass

This documentation serves as the Source of Truth for the policy and strategy that guides Executable Books.
It defines the organizational structure of this project, and serves as a guide to help community members understand how to interact with the community.

## Where to read the Team Compass

See [compass.executablebooks.org](https://compass.executablebooks.org) for the full team compass.

## Source files

Find the source files for the Team Compass in `docs/`.

## Build the Team Compass

The easiest way to build the team compass is with Sphinx, using `tox`.
The following command will install the necessary environment to build the team compass, and generate HTML files at `docs/_build/dirhtml`.

```
tox -e docs
```

If you wish to start a **live server that previews the docs and updates as you change things**, run this command:

```
tox -e docs-live
```

## Update the list of team members

To update the list of team members, run this script:

`docs/scripts/update_team_membership.py`

See the comment in that file for more instructions.
You will need to have an authenticated GitHub CLI to run it.
