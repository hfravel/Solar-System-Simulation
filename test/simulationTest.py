import unittest
from src import simulation


class MyTestCase(unittest.TestCase):
    def test_calculate_distance_and_orientation(self):
        results = simulation.calculate_distance_and_orientation((0,0,0), (3,0,4))

        self.assertEqual(results[0], 5)


if __name__ == '__main__':
    unittest.main()
