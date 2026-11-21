# Reusable workflow examples

These workflows are reference examples, not active workflows in this
repository. They are stored under `workflows/` and must be reviewed, tested,
and moved to a maintained repository's `.github/workflows/` directory before
they can be called.

The third-party actions below use immutable commit SHAs. Recheck upstream
releases, provenance, and compatibility before updating a pin. Reusable
workflow callers should also pin the reusable workflow to a commit SHA rather
than a movable branch or tag.

All workflows use least-privilege token permissions, elevated per job where
needed. Cloud deployments additionally require a narrowly scoped OIDC trust
policy and an appropriately protected GitHub environment. Never pass an
arbitrary command as a workflow input; the deployment example accepts a
repository-relative script path instead.

The Node.js build and test examples expect a `package-lock.json`. The
infrastructure workflow expects OpenTofu configuration. Select only workflows
that match the consuming repository.
