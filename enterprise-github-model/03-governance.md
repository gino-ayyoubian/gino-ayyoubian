# Governance baseline

These are recommendations for repositories that opt into the model. They are
not all configured on the account today. Apply the smallest policy that
protects the project without blocking its maintainers.

## Repository defaults

- Keep the default branch and repository purpose clear in the description and
  README.
- Set Actions' default `GITHUB_TOKEN` permission to read-only when available;
  grant extra permissions to individual jobs.
- Protect the default branch with pull requests, required checks, and no
  force-push or deletion. Choose approval counts to match the actual maintainer
  team; a one-person repository cannot satisfy a second-person review rule.
- Use CODEOWNERS to identify reviewers, but remember that it is not enforcement
  unless the branch rules require code-owner review.
- Enable Dependabot alerts and updates, secret scanning, and push protection
  where available and appropriate. Confirm actual state in repository settings.
- Prefer immutable action references and short-lived OIDC credentials over
  mutable tags and long-lived cloud keys.

## Access and environments

- Assign access to named maintainers or teams with the least privilege needed.
- Review access periodically and remove obsolete grants.
- Scope deployment secrets to environments; use OIDC for supported cloud
  providers.
- Gate production deployments with environment protection rules where a
  meaningful independent approval process exists.
- Require signed commits only when the team can consistently produce and verify
  them.

## Lifecycle and ownership

- Record an accountable owner and support expectation for maintained projects.
- Mark experimental, active, or deprecated lifecycle in repository metadata only
  when the owner agrees.
- Ask maintainers before renaming, transferring, merging, or archiving a
  repository. Inactivity alone is not proof that a repository is abandoned.
- Create new repositories from templates only when the templates fit the
  project's language, build system, and deployment model.

## Review cadence

Review access, branch rules, automation permissions, dependency alerts, and
ownership at least annually and after material team or platform changes.
Record exceptions and their owner rather than treating an unavailable control
as enabled.
