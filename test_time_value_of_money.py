

import unittest
from time_value_of_money import (net_present_value, weighted_average_cost_of_capital,
                                capital_source)

class Tests(unittest.TestCase):

    def test_net_preset_value(self):
        self.assertAlmostEqual(
            net_present_value([-35_000, 10_000, 27_000, 19_000], 0.12),
            8_977,
            places=0)

    def test_weighted_average_cost_of_capital(self):
        ce = capital_source('common equity', .12, 46.6)
        pe = capital_source('preferred equity', .1, 10.3)
        ltd = capital_source('long term debt', .08, 35, debt=True)
        self.assertAlmostEqual(
            weighted_average_cost_of_capital([ce, pe, ltd]),
            .0934,
            places=4)

def main():
    unittest.main(exit=False)

if __name__ == '__main__':
    main()

