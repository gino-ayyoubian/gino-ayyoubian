# Adoption roadmap

This roadmap is a proposal, not a report of completed account-wide changes.
Each item stays **proposed** until an owner confirms scope, permission, and
acceptance criteria.

## Status at the 2026-11-21 review

| Workstream | Status | Exit criteria |
|---|---|---|
| Repository inventory | Partially complete | Public metadata is inventoried; private repositories and project contents remain unaudited. |
| Governance and ownership | Proposed | Maintainers confirm ownership, access, and support expectations per repository. |
| Security and Actions settings | Needs owner verification | Actual repository settings are reviewed and least-privilege defaults are recorded. |
| Reusable workflows | Reference examples only | Workflows are published in a maintained repository, pinned by SHA, and adopted by a pilot. |
| Catalog and organization model | Deferred | A real operating need, platform owner, and migration plan are established. |

## Recommended sequence

### 1. Confirm ownership and inventory

- Ask maintainers to confirm purpose, owner, support expectations, and lifecycle.
- Review private repositories separately; do not infer their contents from names.
- Resolve possible overlap only after inspecting code, dependencies, and stakeholder
  needs.

### 2. Establish a practical baseline

- Set repository descriptions and topics; select a license only with owner
  approval.
- Confirm workflow token permissions, branch rules, dependency alerts, secret
  scanning, and push protection in GitHub settings.
- Add project-appropriate CI and documentation.
- Pilot the baseline on one actively maintained repository and capture any
  exceptions.

### 3. Reuse what works

- Publish reusable workflows at immutable revisions.
- Add environment-based deployment and OIDC only to repositories that deploy to
  supported cloud infrastructure.
- Expand the pilot based on measured maintenance effort and team feedback.

### 4. Consider platform expansion

Consider organizations, a service catalog, GitOps, Kubernetes, dedicated
runners, multi-cloud tooling, or compliance mapping only when there is a named
owner, documented requirement, and funded operating plan.

## Change controls

Repository renames, transfers, visibility changes, archival, secret rotation,
and branch-policy changes require explicit owner review. Keep an audit trail
and a recovery plan for changes that could disrupt access, automation, or
deployments.
