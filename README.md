# py-prj-template

Python project layout using [uv](https://docs.astral.sh/uv/) for environments and lockfiles, [`pyproject.toml`](pyproject.toml) for metadata and tools, [pre-commit](https://pre-commit.com/) for git hooks, and [pytest](https://pytest.org/) for tests.

## Bootstrap

```bash
uv sync --all-groups
uv run pre-commit install
uv run pytest
```

After copying the template, rename the `py-prj-template` project and the `py_prj_template` package in `pyproject.toml`, the `py_prj_template/` directory, and imports/tests.

## Layout

- `py_prj_template/` — installable package (mirrors a `modules/`-style layout in application repos).
- `tests/` — pytest suite; `pythonpath` is set so imports match a flat package layout.

Lockfile: [`uv.lock`](uv.lock) (commit it for reproducible installs).
