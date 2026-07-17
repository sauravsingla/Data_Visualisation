# Contributing

Thank you for improving this visualisation reference.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[all,dev]"
ruff check .
pytest --cov=dataviz_reference
```

## Contribution standards

Every reusable chart should:

1. Answer a clear analytical question.
2. Validate required columns and data types.
3. Return a figure object instead of calling `show()`.
4. Work with deterministic example data.
5. Include tests for successful and invalid inputs.
6. Use accessible labels, scales, and colour choices.
7. Document the intended interpretation and limitations.

Keep commits focused and written in plain language. Avoid mixing unrelated refactors, examples, and documentation in one commit.

## Pull requests

Describe the problem, the visualisation choice, accessibility considerations, validation performed, and commands used to test the change. Include screenshots only when they help reviewers evaluate visual output.
