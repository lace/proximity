def faces_nearest_to_points(mesh, query_points, ret_points=False):
    """
    Find the triangular faces on a mesh which are nearest to the given query
    points.

    Args:
        query_points (np.arraylike): The points to query, with shape `kx3`
        ret_points (bool): When `True`, return both the indices of the
            nearest faces and the closest points to the query points, which
            are not necessarily vertices. When `False`, return only the
            face indices.

    Returns:
        object: face indices as `kx1 np.ndarray`, or when `ret_points`
        is `True`, a tuple also including the coordinates of the closest points
        as `kx3 np.ndarray`.
    """
    import trimesh

    trimesh_mesh = trimesh.Trimesh(vertices=mesh.v, faces=mesh.f)
    closest_points, _, face_indices = trimesh_mesh.nearest.on_surface(query_points)
    return (face_indices, closest_points) if ret_points else face_indices
