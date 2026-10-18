# Actions framework

Copy `workflows/` to `kkm-infra/actions/.github/workflows/` and tag releases (`v1`).
Conventions: default `permissions: contents: read`, per-job elevation, concurrency groups, OIDC for cloud auth, and third-party actions pinned by full commit SHA.
Replace each `@vN # pin-to-sha` reference with the full commit SHA before use (`actions/*` shown by major tag for readability).
