import math
import unittest

from src import simulation

uncertainty = 0.00000000001
half_pi = math.pi / 2


class MyTestCase(unittest.TestCase):
    def test_calculate_3d_orientation_two_coord(self):
        results = simulation.calculate_3d_orientation((0, 0, 0), (0, 3, 4))
        self.assertEqual(results[0], 5)
        self.assertEqual(results[1], half_pi)
        results = simulation.calculate_3d_orientation((0, 0, 0), (0, 4, 3))
        self.assertEqual(results[0], 5)
        self.assertEqual(results[1], half_pi)
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 0, 4))
        self.assertEqual(results[0], 5)
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 4, 0))
        self.assertEqual(results[0], 5)
        results = simulation.calculate_3d_orientation((0, 0, 0), (4, 0, 3))
        self.assertEqual(results[0], 5)
        results = simulation.calculate_3d_orientation((0, 0, 0), (4, 3, 0))
        self.assertEqual(results[0], 5)

    def test_calculate_3d_orientation_negative_xz(self):
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 0, 3))
        self.assertEqual(results[1], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 0, -3))
        self.assertEqual(results[1], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (-3, 0, 3))
        self.assertEqual(results[1], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (-3, 0, -3))
        self.assertEqual(results[1], math.radians(45.0))

    def test_calculate_3d_orientation_negative_y(self):
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 3, 0))
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, -3, 0))
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (-3, 3, 0))
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (-3, -3, 0))
        self.assertEqual(results[2], math.radians(45.0))

        results = simulation.calculate_3d_orientation((0, 0, 0), (0, 3, 3))
        self.assertEqual(results[1], half_pi)
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (0, 3, -3))
        self.assertEqual(results[1], half_pi)
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (0, -3, 3))
        self.assertEqual(results[1], half_pi)
        self.assertEqual(results[2], math.radians(45.0))
        results = simulation.calculate_3d_orientation((0, 0, 0), (0, -3, -3))
        self.assertEqual(results[1], half_pi)
        self.assertEqual(results[2], math.radians(45.0))

    def test_calculate_3d_orientation_all_three_coord(self):
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 4, 12))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)
        results = simulation.calculate_3d_orientation((0, 0, 0), (3, 12, 4))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)
        results = simulation.calculate_3d_orientation((0, 0, 0), (4, 3, 12))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)
        results = simulation.calculate_3d_orientation((0, 0, 0), (4, 12, 3))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)
        results = simulation.calculate_3d_orientation((0, 0, 0), (12, 3, 4))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)
        results = simulation.calculate_3d_orientation((0, 0, 0), (12, 4, 3))
        self.assertTrue(13 - uncertainty < results[0] < 13 + uncertainty)


if __name__ == '__main__':
    unittest.main()
