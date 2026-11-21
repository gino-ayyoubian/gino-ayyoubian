# Target architecture

This is a **proposed** future-state model, not a description of organizations,
services, or controls already deployed. Adopt only the parts that match confirmed
ownership, operational needs, and available platform capabilities.

## Organization boundaries

Potential organization boundaries:

| Organization | Intended scope |
|---|---|
| `kkm-core` | Core business systems |
| `kkm-platform` | Shared services and libraries |
| `kkm-infra` | Infrastructure, GitOps, reusable Actions, and runners |
| `kkm-research` | Research and experiments |
| `kkm-ai` | AI systems |
| `kkm-client` | Client-facing products |
| `kkm-archive` | Retired repositories with an agreed retention policy |

Do not create organizations or transfer repositories until the owner, access
model, billing, compliance requirements, and migration plan have been agreed.
Personal-account repositories may remain personal when that is the simplest
appropriate ownership model.

## Delivery path

```text
Pull request
  -> least-privilege CI and security checks
  -> reviewed, versioned artifact
  -> protected deployment environment
  -> cloud access through short-lived OIDC credentials
```

For container workloads, publish to GHCR or an approved registry, identify
artifacts by immutable digest, and sign/attest them before deployment. Add
GitOps, Kubernetes, or multi-cloud infrastructure only where operating teams
need them; they are not prerequisites for every repository.

## Platform principles

- Keep reusable workflows in a maintained repository and pin callers to an
  immutable commit SHA.
- Grant `GITHUB_TOKEN` only the permissions a job needs; use OIDC instead of
  long-lived cloud credentials where supported.
- Require environment approvals for production changes when a separate reviewer
  is available and the risk warrants it.
- Use ephemeral runners only when hosted runners cannot meet a documented need.
- Treat catalog metadata as useful only when an owner maintains it and a catalog
  consumes it.
- Measure readiness by working controls and operational ownership, not by
  adopting technology names.
