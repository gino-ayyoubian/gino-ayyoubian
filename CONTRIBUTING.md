# Contributing

Thanks for helping improve this profile and its GitHub governance examples.

## Before opening a pull request

- Keep changes focused and explain their purpose.
- Do not add personal or operational claims without owner confirmation.
- Treat the enterprise model as a proposal; do not imply that example controls
  are enabled on GitHub.
- Replace template placeholders and verify that example permissions fit the
  consuming repository.
- Do not include credentials, tokens, or private repository details.

## Validation

Run the documentation checker tests and link check from the repository root:

```sh
python3 -m unittest discover -s tests
python3 scripts/check_docs.py
```

Workflow examples should be reviewed for valid syntax, immutable action
references, and least-privilege permissions. They are examples and are not
executed by this repository's CI.

## Pull requests

Use the pull request template and include the validation performed. Signed
commits or required reviews apply only if the corresponding repository settings
are enabled.
