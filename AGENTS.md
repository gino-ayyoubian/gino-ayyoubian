# Agent instructions

## Scope and evidence

- This repository contains a profile README and a proposed GitHub governance
  model. Keep those purposes distinct.
- Do not describe a proposed control, organization, or workflow as deployed
  unless repository evidence confirms it.
- Do not invent personal, project, security, or operating claims. Preserve
  owner-approved facts and flag anything that needs confirmation.
- Do not rename, transfer, archive, or change the visibility of repositories
  based only on metadata or inactivity.

## Documentation and workflow changes

- Keep Markdown direct, accessible, and free of placeholder links.
- Treat files under `enterprise-github-model/` as adoption examples. Mark
  placeholders and prerequisites clearly.
- Pin third-party GitHub Actions to immutable commit SHAs. Use the least
  permissions needed at workflow and job level.
- Never interpolate a free-form workflow input directly into a shell command.
- Do not change GitHub-side security, access, or branch-protection settings
  unless the task specifically authorizes it and the setting can be verified.

## Validation

Run `python3 scripts/check_docs.py` after Markdown or link changes. Review
workflow syntax and permissions after editing workflow examples.
