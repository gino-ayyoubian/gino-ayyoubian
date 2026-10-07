# 01 Audit

## Enumeration (public repos under `gino-ayyoubian`, none archived or forked)

| Repo | Lang | Created | Updated | Proposed name |
|---|---|---|---|---|
| gino-ayyoubian | - | 2026-05 | 2026-05 | keep (profile) |
| KKM-Digital-Ecosystem | TS | 2026-02 | 2026-07 | `kkm-platform/docs-digital-ecosystem` or `ai-*` |
| KKM-Enterprise---Digiral-Assets- | - | 2026-09 | 2026-09 | merge into Digital-Ecosystem, archive |
| kkm-ivr-daftareshoma | - | 2025-12 | 2025-12 | `kkm-client/svc-ivr-daftareshoma` |
| telegram-bot-framework | TS | 2026-05 | 2026-06 | `kkm-platform/lib-telegram-bot` |
| telegram-workflow-bot | TS | 2026-05 | 2026-05 | `kkm-platform/svc-telegram-workflow-bot` |
| Brand-Bible-Studio | TS | 2025-11 | 2026-05 | `kkm-client/web-brand-bible-studio` |

## Ownership and dependencies (hypothesis)
- Digital-Ecosystem and Enterprise-Digital-Assets overlap in vision.
- telegram-workflow-bot is likely a subset of telegram-bot-framework (workflow engine, state machine).
- All repos sit in a personal account: no teams, no CODEOWNERS.
- IVR and Brand-Bible-Studio are client products without shared libraries.

## Checklist (verify with admin access)
| Area | Expected gap | Action |
|---|---|---|
| Workflows/CI | none visible | adopt reusable workflows |
| Permissions | default token scope unknown | read-only default |
| Secrets | bot tokens, DB creds | environment secrets, OIDC, push protection |
| Branch protection | unknown | rulesets on `main` |
| Naming | mixed case, `---`, typo | taxonomy in 04 |
| Docs | profile README only confirmed | README, CONTRIBUTING, SECURITY, CODEOWNERS, ADRs |
| Deployment | unknown | containers + GitOps |

## Findings
- Duplicated logic: two Telegram repos; two digital-assets repos.
- Stale/orphan candidates: kkm-ivr-daftareshoma (~10 months idle), Enterprise-Digital-Assets (no content signals).
- Security gaps: no org boundary, no visible automation, possible secrets in public bot repos.
- Missing automation: Dependabot, CodeQL, release, container publish, docs site.

## Needed for a verified audit
Admin access to `KKM-International-Group`, or exports of `gh repo list`, rulesets, secrets metadata and workflows.
