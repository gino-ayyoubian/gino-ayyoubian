# Repository taxonomy

Use descriptive repository names that remain understandable outside a single
organization. A proposed pattern is `<type>-<domain>-<name>` in lowercase
kebab-case, but do not rename existing repositories solely to match it.

| Prefix | Intended use | Example |
|---|---|---|
| `svc-` | Backend service | `svc-telemetry-ingest` |
| `web-` | Web application | `web-operations-portal` |
| `infra-` | Infrastructure or deployment configuration | `infra-observability` |
| `ops-` | Operational tooling | `ops-release-tools` |
| `lib-` | Shared library | `lib-event-schema` |
| `ai-` | AI/ML system | `ai-document-assistant` |
| `exp-` | Time-bounded experiment | `exp-forecasting-model` |
| `docs-` | Documentation product | `docs-platform-handbook` |

Prefer a clear, unique name over a prefix when the repository has an established
audience or product identity. Avoid encoding a temporary team name in a
repository name.

## Metadata

For maintained repositories, document:

- A concise purpose in the repository description and README.
- An accountable owner and support contact.
- Lifecycle (`experimental`, `active`, or `deprecated`) when agreed by the
  maintainer.
- Technology or domain topics that help people find the project.

`catalog-info.yaml` is optional. Add it only when a catalog such as Backstage is
operated and has an assigned metadata owner. Keep its owner, lifecycle, type,
and tags synchronized with the repository's actual operating model.

## Organization boundaries

The organization names in [the target architecture](02-target-architecture.md)
are suggestions. Confirm governance, billing, identity, compliance, and
operational ownership before creating organizations or moving repositories.
