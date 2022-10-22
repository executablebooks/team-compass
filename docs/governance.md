# Governance

This page describes the groups with decision-making authority in the project, as well as the processes and policies we follow.

```{epigraph}
_All contributors to the Executable Books Project (including but not limited to individuals contributing code, providing technical support, discussing in repositories, teaching workshops, or discussing changes to EBP policy) are expected to adhere to the [Code of Conduct](policy:coc)._
```

## Decision-Making Groups

The following groups have formal decision-making authority in the project.
Membership in each group comes with responsibilities, expectations, and privileges.

(governance:steerco)=
### Steering Council

Members have decision-making authority over the entire organization.
Their primary duty is to set organizational policy and strategy, to steward all technical and IP assets of the organization, to make decisions when we are at an impasse, and to delegate decision-making power to others in the organization. 

#### Responsibilies

```{note}
This is intentionally blank for now, we will add more information in the coming weeks.
```

% - Define organizational policy, strategy, and values
% - Hold the community accountable to its mission and its code of conduct
% - Oversee the structure and system of work in the community
% - Delegate authority and responsibility to position the project for success

#### Expectations

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

Steering Council Members agree to abide by the [EBP Code of Conduct](policy:coc).

#### Privileges

- _Owner_ status of the [executablebooks](https://github.com/executablebooks) GitHub organizations and repositories.
- Access to any credentials or accounts that the project uses. At least two Steering Council members must have access to all project credentials.
- Voting privileges for [changing Team Policy](governance:policy-decision).
- All [Core Team privileges](governance:privileges:core-team)

### Core Team Members

Individuals who are particularly interested in the EBP community and have demonstrated a willingness to participate in our community and further its mission. They guide discussion, grow the community, contribute code, and generally help the project improve.

#### Responsibilities

```{note}
This is intentionally blank for now, we will add more information in the coming weeks.
```

#### Expectations

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

Core Team Members agree to abide by the [EBP Code of Conduct](https://github.com/executablebooks/.github/blob/master/CODE_OF_CONDUCT.md).

(governance:privileges:core-team)=
#### Privileges

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

- Write permissions for any repository they are willing to steward.
- Voting privileges for [MyST Enhancement Proposals](governance:meps).

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
