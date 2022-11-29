# Governance and decision making

This page describes the groups with decision-making authority in the project, as well as the processes and policies we follow.

## Overview

In short, here is the decision making process that we follow:

- All organizational policy is defined in this Team Compass.
- Most day to day decisions are made by {team}`Core Team` members.
- Team members are expected to follow inclusive team practices when making decisions, and to actively share information and collaborate with one another.
- There are a few kinds of decisions that require specific process or decision makers.
  - Changes to the MyST specification follow [the MyST specification decision making process](governance:myst).
  - Changes to team policy follow [the team policy decision making process](governance:policy-decision).
- Members of the {team}`Steering Council` may vote to break ties if decision making is at an impasse in any part of the organization.

## Sources of Truth

### Team policy

This Team Compass repository is the source of truth for all team policy, unless explicitly delegated elsewhere.

### Code of Conduct

Our Code of Conduct defines acceptable and unacceptable behavior for any individual participating in an Executable Books space (online or in-person).
It also defines mechanisms for reporting violations and processes for dealing with them.

See [](code-of-conduct.md) for more information.

(governance:myst)=
### The MyST Specification

The MyST Specification is defined at [`executablebooks/myst-spec`](https://github.com/executablebooks/myst-spec).
It uses a combination of documentation, examples, schemas, tests, etc to define MyST markdown in a form that can be used to implement parsers and renderers. It is versioned and includes "releases" in order to make it easy for downstream implementors to track the changes they need to make.

```{admonition} Implementation detail
This repository will need to be modified as-needed to be the source of truth for the MyST Specification, and to have enough information to teach newcomers about its structure and function. One example for inspiration: [the Zarr specifications page](https://zarr.readthedocs.io/en/stable/spec.html). [Here's a comment with some suggestions for what is missing](https://github.com/executablebooks/meta/pull/843#issuecomment-1275474229).
```

## Changing Policy

(governance:policy-decision)=
### Team Policy

Take the following steps for changing any policy, strategy, or governance aspect of the Team Compass.

1. **Open an issue** to explain the policy that you'd like to change, and why. Here is a rough template to follow:
   ```
   ## Context
   
   provide context needed to understand this proposal. Describe the problem this proposal will solve.
   
   ## Proposal
   
   describe your proposal in informal but specific terms.
   
   ## Impact
   
   describe the implications of this proposal and the impact it will have.
   ```
2. **Discuss and incorporate feedback** with others on the team. If there are objections or suggestions, do your best to incorporate them into your proposal.
3. **Make a pull request** to the `Team Compass` repository (or another location if appropriate) and link it to the issue. This is the "formal change" that you wish to make.
4. **Make a decision**. Steering Council members may approve PRs to change policy. To approve a change, use the "Approve" feature in the GitHub UI. To request blocking changes, use the "Request Changes" feature in the GitHub UI[^blocking]. PRs to change organizational policy may be merged when the following conditions are met:
   - Have been open either for five working days or up until all Steering Council members `Approve` the PR.
   - Have `Approval` from at least **one  Steering Council member**
   - Have no `Request Changes` from a Steering Council member.
   - If there are unresolveable objections from a Steering Council member, a decision to merge is made with a majority vote.


[^blocking]: When blocking any change or objecting to a proposal, provide a rationale for what must be changed and why you believe it is critically important. _Do not disapprove because of differences in opinion. Only disapprove if you have a major strategic concern_. See [Strategies for integrating objections](https://www.sociocracyforall.org/strategies-for-integrating-objections/) for what we are aiming for.

### The MyST Specification

We use a special process called **MyST Enhancement Proposals** to change the MyST Specification.

This is currently defined in the pages below, and will be moved to [`executablebooks/myst-enhancement-proposals`](https://github.com/executablebooks/myst-enhancement-proposals) in the future.

```{toctree}
meps
```
