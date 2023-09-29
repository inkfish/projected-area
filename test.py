import unittest

import numpy as np
import trimesh

from projected_area import projected_area


trimesh.util.attach_to_log()


class ProjectedAreaTests(unittest.TestCase):
    def test_cube(self):
        mesh = trimesh.load('./models/cube.stl')
        expected_yz_area = 1.0  # s^2
        expected_xz_area = 1.0  # s^2
        expected_xy_area = 1.0  # s^2

        yz_area = projected_area(mesh, np.array([0,0,0]), np.array([1,0,0]))
        xz_area = projected_area(mesh, np.array([0,0,0]), np.array([0,1,0]))
        xy_area = projected_area(mesh, np.array([0,0,0]), np.array([0,0,1]))

        np.testing.assert_allclose(yz_area, expected_yz_area)
        np.testing.assert_allclose(xz_area, expected_xz_area)
        np.testing.assert_allclose(xy_area, expected_xy_area)

    def test_cylinder(self):
        mesh = trimesh.load('./models/cylinder.stl')
        expected_yz_area = 4.0  # 2rh
        expected_xz_area = 4.0  # 2rh
        expected_xy_area = np.pi # pi r^2

        yz_area = projected_area(mesh, np.array([0,0,0]), np.array([1,0,0]))
        xz_area = projected_area(mesh, np.array([0,0,0]), np.array([0,1,0]))
        xy_area = projected_area(mesh, np.array([0,0,0]), np.array([0,0,1]))

        np.testing.assert_allclose(yz_area, expected_yz_area)
        np.testing.assert_allclose(xz_area, expected_xz_area)
        np.testing.assert_allclose(xy_area, expected_xy_area, rtol=1e-02)

    def test_rectangular_prism(self):
        mesh = trimesh.load('./models/rectangular-prism.stl')
        expected_yz_area = 1.0  # hd
        expected_xz_area = 2.0  # wh
        expected_xy_area = 2.0  # wd

        yz_area = projected_area(mesh, np.array([0,0,0]), np.array([1,0,0]))
        xz_area = projected_area(mesh, np.array([0,0,0]), np.array([0,1,0]))
        xy_area = projected_area(mesh, np.array([0,0,0]), np.array([0,0,1]))

        np.testing.assert_allclose(yz_area, expected_yz_area)
        np.testing.assert_allclose(xz_area, expected_xz_area)
        np.testing.assert_allclose(xy_area, expected_xy_area)

    def test_sphere(self):
        mesh = trimesh.load('./models/sphere.stl')
        expected_yz_area = expected_xz_area = expected_xy_area = np.pi  # pi r^2

        yz_area = projected_area(mesh, np.array([0,0,0]), np.array([1,0,0]))
        xz_area = projected_area(mesh, np.array([0,0,0]), np.array([0,1,0]))
        xy_area = projected_area(mesh, np.array([0,0,0]), np.array([0,0,1]))

        np.testing.assert_allclose(yz_area, expected_yz_area, rtol=1e-02)
        np.testing.assert_allclose(xz_area, expected_xz_area, rtol=1e-02)
        np.testing.assert_allclose(xy_area, expected_xy_area, rtol=1e-02)


if __name__ == '__main__':
    unittest.main()
