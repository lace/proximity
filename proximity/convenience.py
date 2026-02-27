import typing as t
import numpy as np
from vg.compat import v2 as vg
from .mock_trimesh import MockTrimesh
from .vendor.proximity import closest_point


@t.overload
def faces_nearest_to_points(  # noqa: E704
    vertices: np.ndarray,
    faces: np.ndarray,
    query_points: np.ndarray,
    ret_points: t.Literal[True],
) -> tuple[np.ndarray, np.ndarray]: ...  # pragma: no cover


@t.overload
def faces_nearest_to_points(  # noqa: E704
    vertices: np.ndarray,
    faces: np.ndarray,
    query_points: np.ndarray,
    ret_points: t.Literal[False],
) -> np.ndarray: ...  # pragma: no cover


@t.overload
def faces_nearest_to_points(
    vertices: np.ndarray,
    faces: np.ndarray,
    query_points: np.ndarray,
) -> np.ndarray:
    ...  # pragma: no cover


def faces_nearest_to_points(
    vertices: np.ndarray,
    faces: np.ndarray,
    query_points: np.ndarray,
    ret_points: bool = False,
) -> t.Union[np.ndarray, tuple[np.ndarray, np.ndarray]]:
    """
    Find the triangular faces on a mesh which are nearest to the given query
    points.

    Args:
        vertices (np.arraylike): The vertices of a mesh, as `kx3`.
        faces (np.arraylike): The face indices of a mesh, as `kx3`.
        query_points (np.arraylike): The points to query, with shape `kx3`
        ret_points (bool): When `True`, return both the indices of the
            nearest faces and the closest points to the query points, which
            are not necessarily vertices. When `False`, return only the
            face indices.

    Returns:
        object: Face indices as `kx1 np.ndarray`, or when `ret_points`
        is `True`, a tuple also including the coordinates of the closest points
        as `kx3 np.ndarray`.
    """
    vg.shape.check(locals(), "vertices", (-1, 3))
    vg.shape.check(locals(), "faces", (-1, 3))
    vg.shape.check(locals(), "query_points", (-1, 3))

    trimesh = MockTrimesh(vertices=vertices, faces=faces)
    closest_points, _, face_indices = closest_point(trimesh, query_points)  # type: ignore[no-untyped-call]
    return (face_indices, closest_points) if ret_points else face_indices
