import numpy as np
from polliwog.tri.functions import surface_normals
from scipy.spatial import cKDTree
from .vendor.triangles import bounds_tree


class MockTrimesh:
    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.triangles = vertices[faces]
        self.face_normals = surface_normals(self.triangles)
        self.triangles_tree = bounds_tree(self.triangles)
        self.kdtree = cKDTree(vertices.view(np.ndarray))
