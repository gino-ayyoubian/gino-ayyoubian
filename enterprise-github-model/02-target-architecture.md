# 02 Target architecture

Organizations: `kkm-core`, `kkm-platform`, `kkm-infra`, `kkm-research`, `kkm-ai`, `kkm-client`, `kkm-archive`.
Each has a `.github` repo for defaults. `kkm-infra/actions` holds reusable workflows.

```
GitHub -> reusable CI -> signed image (GHCR / internal registry)
       -> infra-gitops repo -> Argo CD / Flux -> Kubernetes
       -> OpenTofu modules (infra-*) -> multi-cloud
```
Auth is by OIDC, with no long-lived cloud keys.

## Security baseline
Rulesets, signed commits, Dependabot, secret scanning with push protection, CODEOWNERS, environment approvals, OIDC, least-privilege tokens.

## Readiness
Kubernetes/GitOps, OpenTofu, internal registry, AI-assisted pipelines, ephemeral self-hosted runners (ARC), multi-cloud, compliance auditing, knowledge graph from `catalog-info.yaml`.
