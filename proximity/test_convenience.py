from lacecore import shapes
import numpy as np
from .convenience import faces_nearest_to_points


def test_faces_nearest_to_points():
    mesh = shapes.cube(np.zeros(3), 3.0)
    query_points = np.array([[0.25, 0.25, -0.4], [3.1, 0.6, 3.05]])
    face_indices, closest_points = faces_nearest_to_points(
        vertices=mesh.v, faces=mesh.f, query_points=query_points, ret_points=True
    )

    np.testing.assert_array_equal(face_indices, np.array([5, 6]))
    np.testing.assert_array_almost_equal(
        closest_points, np.array([[0.25, 0.25, 0.0], [3.0, 0.6, 3.0]])
    )
