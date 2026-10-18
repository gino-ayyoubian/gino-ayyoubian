# 03 Governance

- Roles: at least 2 org owners; team maintainers per org; CODEOWNERS on every repo.
- Org rulesets on default branch: PR required, 1+ approvals (2 for prod/infra), code-owner review, linear history, signed commits, required status checks, no force-push or deletion.
- Environments `dev`, `staging`, `prod`; `prod` requires reviewers and branch restriction.
- Tokens: default `contents: read`; elevate per job. Pin third-party actions by SHA.
- Secrets: environment-scoped; cloud access via OIDC only; rotate on exposure.
- Quarterly access review.
- Archive policy: no activity for 6 months and no owner -> move to `kkm-archive`.
- New repos are created from templates only, via request.
- Lifecycle topics: `tier:0-3`, `owner:<team>`, `lifecycle:experimental|active|deprecated`.
