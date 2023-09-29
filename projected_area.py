import numpy as np
import shapely
import trimesh


def project_to_plane(points, plane_point, plane_normal):
    plane_normal = plane_normal / np.linalg.norm(plane_normal)

    # Find the rotation matrix to rotate to the XY plane so that that we end up
    # with a zero Z axis.
    rotmat = trimesh.geometry.plane_transform(plane_point, plane_normal)[:3,:3]

    # Project points onto the plane
    projected = (
        points -
        np.dot(points - plane_point, plane_normal)[:,np.newaxis] *
        plane_normal
    )

    # Rotate points to the XY points and discard the Z axis
    return (projected @ rotmat.T)[:,:-1]


def projected_area(mesh, plane_point, plane_normal):
    polygons = []
    for face in mesh.faces:
        vertices = np.array(mesh.vertices[face])
        projected = project_to_plane(vertices, plane_point, plane_normal)
        polygons.append(shapely.Polygon(projected))
    return shapely.union_all(polygons).area


if __name__ == '__main__':
    import argparse

    trimesh.util.attach_to_log()

    parser = argparse.ArgumentParser()
    parser.add_argument('mesh')
    args = parser.parse_args()

    mesh = trimesh.load(args.mesh)
    print('volume =', mesh.volume)
    print('approximate area =', mesh.volume**(2/3))

    print('surge X projected area =',
          projected_area(mesh, np.array([0,0,0]), np.array([1,0,0])))
    print('sway  Y projected area =',
          projected_area(mesh, np.array([0,0,0]), np.array([0,1,0])))
    print('heave Z projected area =',
          projected_area(mesh, np.array([0,0,0]), np.array([0,0,1])))
