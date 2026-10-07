# 04 Repository taxonomy

Names: lowercase kebab-case, `<prefix>-<domain>-<name>`.

| Prefix | Use |
|---|---|
| `svc-` | backend services |
| `web-` | frontend systems |
| `infra-` | infrastructure |
| `ops-` | operational tooling |
| `lib-` | shared libraries |
| `ai-` | AI systems |
| `exp-` | experiments |
| `docs-` | documentation portals (e.g. `docs-kg` knowledge graph) |

Every repo has a `catalog-info.yaml` (Backstage-style) feeding the knowledge graph.

| Org | Holds |
|---|---|
| kkm-core | core business systems |
| kkm-platform | shared platform services and libs |
| kkm-infra | IaC, GitOps, actions, runners |
| kkm-research | research, `exp-*` |
| kkm-ai | AI systems |
| kkm-client | client-facing products |
| kkm-archive | retired repos |
