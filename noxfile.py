import nox

PYPROJECT = nox.project.load_toml("pyproject.toml")
MAX_PYTHON_VERSION = "3.13"
PYTHON_VERSIONS = nox.project.python_versions(PYPROJECT, max_version=MAX_PYTHON_VERSION)

nox.options.default_venv_backend = "uv"


@nox.session(python=PYTHON_VERSIONS, reuse_venv=True)
def tests(session: nox.Session) -> None:
    session.install(".", "pytest")
    session.run("pytest")


@nox.session(python=MAX_PYTHON_VERSION, reuse_venv=True)
def lint(session: nox.Session) -> None:
    session.install("ruff")
    session.run("ruff", "check", "--fix")


@nox.session(python=MAX_PYTHON_VERSION, reuse_venv=True)
def types(session: nox.Session) -> None:
    session.install("mypy")
    session.run("mypy", "src/arrowquality", "tests", "--strict")
