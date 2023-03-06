# Shared accounts and services

There are a few resources that the team shares to reduce redundancy, save time, and standardize our practices.
This page has a few major pieces.

## Design assets

The Executable Books team uses [this Figma board](https://www.figma.com/file/ZptZUfzGznnT8GhIplnZBU/icon) to store its logo and other visual design assets.
Anybody can access these assets, though only core team members can edit them.

## Google drive

We have [a shared Google Drive](https://drive.google.com/drive/folders/1lg4YpS3BpMnra4bVmkwfaTmYGYn42l3d?usp=sharing) where we store some assets like presentations and documents.
Access to this Google Drive is restricted to core team members.

## `ebp-bot`

We have a GitHub user that is dedicated to automation and scripting for the organization.
Its name is [`@ebp-bot`](https://github.com/ebp-bot).
It has maintain permissions over Executable Books repositories, and we use its **Personal Access Token** to allow API access to our Actions and ReadTheDocs jobs.
This allows us to have programmatic access to EB resources without requiring a single team member to provide an access token.

Ask a {team}`Core Team` member for access to the `@ebp-bot` account.

## Domain names

Below is a list of domain names for the project, as well as the service we use to manage them.
The {team}`Steering Council` has access to these domains, and if you need access in order to do something just ask them.

```{list-table}
- - [`executablebooks.org`](https://executablebooks.org)
  - [NameCheap](https://www.namecheap.com/)
- - [`jupyterbook.org`](https://jupyterbook.org)
  - [NameCheap](https://www.namecheap.com/)
- - [`myst-tools.org`](https://myst-tools.org)
  - [Google Domains](https://domains.google.com)
```

## `welcome-bot`, `new-issue-bot`, and `new-pr-bot`

We have a bot that automatically replies to issues and pull requests from first-time contributors in a repository.
The configuration for this bot can be found here:

https://github.com/executablebooks/.github/blob/master/.github/config.yml
