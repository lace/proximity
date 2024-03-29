# proximity

[![version](https://img.shields.io/pypi/v/proximity?style=flat-square)][pypi]
[![python versions](https://img.shields.io/pypi/pyversions/proximity?style=flat-square)][pypi]
[![license](https://img.shields.io/pypi/l/proximity?style=flat-square)][pypi]
[![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen?style=flat-square)][coverage]
[![build](https://img.shields.io/circleci/project/github/lace/proximity/master?style=flat-square)][build]
[![code style](https://img.shields.io/badge/code%20style-black-black?style=flat-square)][black]

Mesh proximity queries based on [libspatialindex][] and [rtree][], extracted
from [Trimesh][].

[pypi]: https://pypi.org/project/proximity/
[coverage]: https://github.com/lace/proximity/blob/master/.coveragerc#L2
[build]: https://circleci.com/gh/lace/proximity/tree/master
[docs build]: https://proximity.readthedocs.io/en/latest/
[black]: https://black.readthedocs.io/en/stable/
[libspatialindex]: https://libspatialindex.org/
[rtree]: https://toblerity.org/rtree/
[trimesh]: https://trimsh.org/


## Development

First, [install Poetry][].

After cloning the repo, run `./bootstrap.zsh` to initialize a virtual
environment with the project's dependencies.

Subsequently, run `./dev.py install` to update the dependencies.

[install poetry]: https://python-poetry.org/docs/#installatio


## Acknowledgements

This code was extracted from [Trimesh][] by [Michael Dawson-Haggerty][mikedh].

[mikedh]: https://github.com/mikedh


## License

The project is licensed under the MIT license.
