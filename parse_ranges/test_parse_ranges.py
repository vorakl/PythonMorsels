import unittest

from parse_ranges import parse_ranges


class ParseRangesTests(unittest.TestCase):

    """Tests for parse_ranges."""

    def test_three_ranges(self):
        self.assertEqual(
            list(parse_ranges('1-2,4-4,8-10')),
            [1, 2, 4, 8, 9, 10],
        )

    def test_with_spaces(self):
        self.assertEqual(
            list(parse_ranges('0-0, 4-8, 20-21, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 21, 43, 44, 45],
        )

    @unittest.expectedFailure
    def test_return_iterator(self):
        numbers = parse_ranges('0-0, 4-8, 20-21, 43-45')
        self.assertEqual(next(numbers), 0)
        self.assertEqual(list(numbers), [4, 5, 6, 7, 8, 20, 21, 43, 44, 45])
        self.assertEqual(list(numbers), [])
        numbers = parse_ranges('100-1000000000000')
        self.assertEqual(next(numbers), 100)

    @unittest.expectedFailure
    def test_with_individual_numbers(self):
        self.assertEqual(
            list(parse_ranges('0,4-8,20,43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )

    @unittest.expectedFailure
    def test_ignore_arrows(self):
        self.assertEqual(
            list(parse_ranges('0, 4-8, 20->exit, 43-45')),
            [0, 4, 5, 6, 7, 8, 20, 43, 44, 45],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)