#!/usr/bin/env -S poetry run python

import os
import click
from executor import execute


def python_source_files() -> list[str]:
    import glob

    include_paths = (
        glob.glob("*.py")
        + glob.glob("proximity/*.py")
        + glob.glob("proximity/**/*.py")
        + ["doc/"]
    )
    exclude_paths = glob.glob("proximity/vendor/*.py") + []
    return [x for x in include_paths if x not in exclude_paths]


@click.group()
def cli() -> None:
    pass


@cli.command()
def install() -> None:
    execute("poetry install --sync")


@cli.command()
def test() -> None:
    execute("pytest")


@cli.command()
def coverage() -> None:
    execute("pytest --cov=proximity")


@cli.command()
def coverage_report() -> None:
    execute("coverage html")
    execute("open htmlcov/index.html")


@cli.command()
def check_types() -> None:
    execute("mypy --show-error-codes proximity/")
    execute("mypy --show-error-codes dev.py")


@cli.command()
def lint() -> None:
    execute("flake8", *python_source_files())


@cli.command()
def black() -> None:
    execute("black", *python_source_files())


@cli.command()
def black_check() -> None:
    execute("black", "--check", *python_source_files())


@cli.command()
def doc() -> None:
    execute("rm -rf build/ doc/build/ doc/api/")
    execute("sphinx-build -W -b singlehtml doc doc/build")


@cli.command()
def doc_open() -> None:
    execute("open doc/build/index.html")


@cli.command()
def clean() -> None:
    execute("find . -name '*.pyc' -delete")
    execute("find . -name '__pycache__' -delete")


@cli.command()
def publish() -> None:
    execute("rm -rf dist/ build/")
    execute("poetry build")
    execute("twine upload dist/*")


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    cli()
