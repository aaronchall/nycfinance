
from collections import namedtuple

def net_present_value(cashflows, discount_rate):
    return sum(cf/(1 + discount_rate)**i for i, cf in enumerate(cashflows))


CapitalSource = namedtuple('CapitalSource', 'name rate market_value debt')
CapitalSource.__doc__ = "rate is required rate of return for security, debt is T/F"

def capital_source(name, rate, market_value, debt=False):
    return CapitalSource(name, rate, market_value, debt)

def weighted_average_cost_of_capital(sources_of_capital, tax_rate=.30):
    """for each type of source of capital, sum(rates*marketvalue)/sum(marketvalue)
    each source has a rate and a market_value """
    soc = list(sources_of_capital)
    return (sum(cs.rate*cs.market_value*(1 - (tax_rate if cs.debt else 0))
                           for cs in soc)
           /sum(cs.market_value for cs in soc))




#def main():
if __name__ == '__main__':
    assert round(net_present_value([-35_000, 10_000, 27_000, 19_000], 0.12)) == 8_977

    ce = capital_source('common equity', .12, 46.6)
    pe = capital_source('preferred equity', .1, 10.3)
    ltd = capital_source('long term debt', .08, 35, debt=True)
    assert round(weighted_average_cost_of_capital([ce, pe, ltd]), 4) == .0934

# if __name__ == "__main__":
#    main()
