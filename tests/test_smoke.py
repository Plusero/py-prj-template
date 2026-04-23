import py_prj_template
from pathlib import Path


def test_version() -> None:
    assert py_prj_template.__version__ == "0.1.0"


def test_uv_lock_exists() -> None:
    """Ensure lockfile is present at repository root."""
    lockfile_path = Path("uv.lock")
    assert lockfile_path.exists()
