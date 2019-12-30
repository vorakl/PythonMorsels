from collections import deque
import unittest

from deep_flatten import deep_flatten


class DeepFlattenTests(unittest.TestCase):

    """Tests for deep_flatten."""

    def assertIterableEqual(self, iterable1, iterable2):
        self.assertEqual(list(iterable1), list(iterable2))

    def test_deep_lists(self):
        inputs = [0, [1, [2, 3]], [4]]
        outputs = [0, 1, 2, 3, 4]
        self.assertIterableEqual(deep_flatten(inputs), outputs)

    def test_tuples(self):
        inputs = (0, (1, (2, 3)), [4])
        outputs = [0, 1, 2, 3, 4]
        self.assertIterableEqual(deep_flatten(inputs), outputs)

    def test_deep_empty_list_with_tuple(self):
        self.assertIterableEqual(deep_flatten([[()]]), [])

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_other_iterables(self):
        self.assertIterableEqual(
            deep_flatten((n, (n**3, n**2)) for n in [2, 3]),
            [2, 8, 4, 3, 27, 9],
        )
        self.assertIterableEqual(deep_flatten([(1, 2), deque([3])]), [1, 2, 3])
        self.assertIterableEqual(
            deep_flatten(iter([n]) for n in [1, 2, 3]),
            [1, 2, 3]
        )

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_returns_iterator(self):
        self.assertEqual(next(deep_flatten([0, [1, [2, 3]]])), 0)

        squares = (n**2 for n in [1, 2, 3])
        self.assertEqual(next(deep_flatten(squares)), 1)
        # The below lines test that the incoming generator isn't exhausted.
        # It may look odd to test the squares input, but this is correct
        # because after 1 item has been consumed from the deep_flatten
        # iterator, squares should also only have 1 item consumed from it.
        try:
            self.assertEqual(next(squares), 4, "squares is partially consumed")
        except StopIteration:
            self.fail("The incoming squares iterator was fully consumed!")
        # When we consume another item from deep_flatten, it'll skip over 4!
        self.assertEqual(next(deep_flatten(squares)), 9)

        # If the above didn't work, this would really break
        from itertools import count
        squares = (n**2 for n in count())
        self.assertEqual(next(deep_flatten(squares)), 0)
        self.assertEqual(next(squares), 1)
        self.assertEqual(next(deep_flatten(squares)), 4)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_flatten_with_strings(self):
        inputs = [
            ['cats', ['carl', 'cate']],
            ['dogs', ['darlene', 'doug']],
        ]
        outputs = ['cats', 'carl', 'cate', 'dogs', 'darlene', 'doug']
        self.assertEqual(list(deep_flatten(inputs)), outputs)


if __name__ == "__main__":
    unittest.main(verbosity=2)