"""Independent numerical examples for the IonTech notes, with no engine calls."""

from math import atan2, cos, degrees, dist, hypot, radians, sin, sqrt
import unittest


class IonTechMathTests(unittest.TestCase):
    def test_vector_displacement_normalization_and_sampling(self):
        start = (1, 2, 3)
        end = (4, 6, 3)
        displacement = tuple(b - a for a, b in zip(start, end))
        magnitude = sqrt(sum(axis**2 for axis in displacement))
        self.assertEqual(displacement, (3, 4, 0))
        self.assertEqual(dist(start, end), 5)
        self.assertEqual(hypot(displacement[0], displacement[2]), 3)
        unit = tuple(axis / magnitude for axis in displacement)
        self.assertEqual(unit, (0.6, 0.8, 0))
        self.assertEqual(tuple(a + 5*d for a, d in zip(start, unit)), end)
        self.assertEqual(tuple(axis / 0.5 for axis in displacement), (6, 8, 0))
        self.assertEqual(dist(start, start), 0)

    def test_yaw_pitch_rotation_and_local_offset(self):
        for yaw, expected in [(0, (-1, 2)), (90, (-2, -1)), (180, (1, -2)), (-90, (2, 1))]:
            with self.subTest(yaw=yaw):
                theta = radians(yaw)
                offset = (-2*sin(theta)-cos(theta), 2*cos(theta)-sin(theta))
                self.assertAlmostEqual(offset[0], expected[0])
                self.assertAlmostEqual(offset[1], expected[1])
        dx, dy, dz = -1, 1, 1
        self.assertAlmostEqual(degrees(atan2(-dx, dz)), 45)
        self.assertAlmostEqual(degrees(-atan2(dy, hypot(dx, dz))), -35.26438968)

    def test_curve_samples_and_ballistic_reference(self):
        arc = [(2*cos(radians(deg)), 2*sin(radians(deg))) for deg in range(0, 91, 30)]
        self.assertEqual(len(arc), 4)
        for point in arc:
            self.assertAlmostEqual(hypot(*point), 2)
        self.assertAlmostEqual(arc[-1][0], 0)
        self.assertAlmostEqual(arc[-1][1], 2)
        time = 0.5
        horizontal = 8*time
        vertical = 2*time - 0.5*8*time**2
        self.assertEqual((horizontal, vertical), (4, 0))

    def test_segment_catches_contact_between_samples(self):
        start, end, center = (0, 0), (2, 0), (1, 0.25)
        direction = tuple(b - a for a, b in zip(start, end))
        offset = tuple(c - a for a, c in zip(start, center))
        t = sum(a*b for a, b in zip(direction, offset)) / sum(axis**2 for axis in direction)
        t = max(0, min(1, t))
        closest = tuple(a + t*d for a, d in zip(start, direction))
        self.assertGreater(dist(start, center), 0.3)
        self.assertGreater(dist(end, center), 0.3)
        self.assertLess(dist(closest, center), 0.3)
        self.assertGreater(dist(closest, center), 0.2)

    def test_insertion_sort_using_stable_insertion_boundary(self):
        source = [(4, "first"), (-2, "negative"), (4, "second"), (1, "last")]
        result = []
        for value in source:
            position = len(result)
            while position > 0 and result[position - 1][0] > value[0]:
                position -= 1
            result.insert(position, value)
        self.assertEqual(result, sorted(source, key=lambda value: value[0]))
        self.assertEqual([label for key, label in result if key == 4], ["first", "second"])

    def test_barrage_parity_and_damage_percentage(self):
        self.assertEqual([2*(i % 2)-1 for i in range(4)], [-1, 1, -1, 1])
        self.assertEqual(100*15/20, 75)
