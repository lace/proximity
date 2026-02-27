import typing as t
import numpy as np
from polliwog.tri.functions import surface_normals
from scipy.spatial import cKDTree
from .vendor.triangles import bounds_tree

if t.TYPE_CHECKING:  # pragma: no cover
    from rtree.index import Index


class MockTrimesh:
    triangles_tree: "Index"

    def __init__(self, vertices: np.ndarray, faces: np.ndarray):
        self.vertices = vertices
        self.faces = faces
        self.triangles = vertices[faces]
        self.face_normals = surface_normals(self.triangles)
        self.referenced_vertices = np.zeros(len(self.vertices), dtype=bool)
        self.referenced_vertices[self.faces] = True
        self.triangles_tree = bounds_tree(self.triangles)  # type: ignore[no-untyped-call]
        self.kdtree = cKDTree(vertices.view(np.ndarray))
