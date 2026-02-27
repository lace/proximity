#!/usr/bin/env -S poetry run python

import glob
import os
import click
import sh


def python_source_files() -> list[str]:
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
    sh.poetry("install", "--sync", "--extras", "doc", _fg=True)


@cli.command()
def test() -> None:
    sh.pytest(_fg=True)


@cli.command()
def coverage() -> None:
    sh.pytest("--cov=proximity", _fg=True)


@cli.command()
def coverage_report() -> None:
    sh.coverage("html", _fg=True)
    sh.open("htmlcov/index.html", _fg=True)


@cli.command()
def check_types() -> None:
    sh.mypy("--show-error-codes", "proximity/", _fg=True)
    sh.mypy("--show-error-codes", "dev.py", _fg=True)


@cli.command()
def lint() -> None:
    sh.flake8(*python_source_files(), _fg=True)


@cli.command()
def black() -> None:
    sh.black(*python_source_files(), _fg=True)


@cli.command()
def black_check() -> None:
    sh.black("--check", *python_source_files(), _fg=True)


@cli.command()
def doc() -> None:
    sh.rm("-rf", "build/", "doc/build/", "doc/api/", _fg=True)
    sh.Command("sphinx-build")("-W", "-b", "singlehtml", "doc", "doc/build", _fg=True)


@cli.command()
def doc_open() -> None:
    sh.open("doc/build/index.html", _fg=True)


@cli.command()
def clean() -> None:
    sh.find(".", "-name", "*.pyc", "-delete", _fg=True)
    sh.find(".", "-name", "__pycache__", "-delete", _fg=True)


@cli.command()
def publish() -> None:
    sh.rm("-rf", "dist/", "build/", _fg=True)
    sh.poetry("build", _fg=True)
    sh.twine("upload", *glob.glob("dist/*"), _fg=True)


if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    cli()
