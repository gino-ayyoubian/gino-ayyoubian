# Enterprise GitHub Model (KKM)

This directory contains a **proposed reference model** for repository
governance, architecture, metadata, and reusable GitHub Actions. It is not a
statement that the proposed organizations, controls, or workflows are already
deployed.

## Contents

- [01 — Repository inventory and baseline](01-audit.md)
- [02 — Target architecture](02-target-architecture.md)
- [03 — Governance baseline](03-governance.md)
- [04 — Repository taxonomy](04-taxonomy.md)
- [05 — Adoption roadmap](05-roadmap.md)
- [Repository templates](templates/)
- [Reusable workflow examples](actions-framework/)

## Using the examples

Treat templates as starting points. Replace every placeholder, remove
language-specific configuration that does not apply, and review permissions,
ownership, secrets, and deployment assumptions before adoption. Reusable
workflows must be published to a maintained repository and referenced by an
immutable commit SHA before callers use them.

The inventory is a dated snapshot of public repository metadata only. It does
not cover private repositories or imply that repositories have been inspected
for source code, secrets, workflows, or business ownership. See the limitations
recorded in [the audit](01-audit.md).
