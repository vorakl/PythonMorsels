import unittest


from earliest import get_earliest


class GetEarliestTests(unittest.TestCase):

    """Tests for get_earliest."""

    def test_same_month_and_day(self):
        newer = "01/27/1832"
        older = "01/27/1756"
        self.assertEqual(get_earliest(newer, older), older)

    def test_february_29th(self):
        newer = "02/29/1972"
        older = "12/21/1946"
        self.assertEqual(get_earliest(newer, older), older)

    def test_smaller_month_bigger_day(self):
        newer = "03/21/1946"
        older = "02/24/1946"
        self.assertEqual(get_earliest(older, newer), older)

    def test_same_month_and_year(self):
        newer = "06/24/1958"
        older = "06/21/1958"
        self.assertEqual(get_earliest(older, newer), older)

    def test_invalid_date_allowed(self):
        newer = "02/29/2006"
        older = "02/28/2006"
        self.assertEqual(get_earliest(older, newer), older)

    def test_two_invalid_dates(self):
        newer = "02/30/2006"
        older = "02/29/2006"
        self.assertEqual(get_earliest(newer, older), older)

    # To test the Bonus part of this exercise, comment out the following line
    @unittest.expectedFailure
    def test_many_dates(self):
        d1 = "01/24/2007"
        d2 = "01/21/2008"
        d3 = "02/29/2009"
        d4 = "02/30/2006"
        d5 = "02/28/2006"
        d6 = "02/29/2006"
        self.assertEqual(get_earliest(d1, d2, d3), d1)
        self.assertEqual(get_earliest(d1, d2, d3, d4), d4)
        self.assertEqual(get_earliest(d1, d2, d3, d4, d5, d6), d5)


if __name__ == "__main__":
    unittest.main()
