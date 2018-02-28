

def current(current_assets, current_liabilities):
    return current_assets/current_liabilities
    
def quick(cash, short_term_marketable_investments, receivables, current_liabilities):
    return (cash + short_term_marketable_investments + receivables) / current_liabilities
    
def cash_ratio(cash, short_term_marketable_investments, current_liabilities):
    return (cash + short_term_marketable_investments) / current_liabilities
    
def defensive_interval(cash, short_term_marketable_investments, receivables, daily_cash_expenditures):
    return (cash + short_term_marketable_investments + receivables) / daily_cash_expenditures
    
def receivables_turnover(total_revenue, average_receivables):
    return total_revenue / average_receivables
    
def days_sales_outstanding(number_of_days_in_period, inventory_turnover_ratio):
    return number_of_days_in_period / inventory_turnover_ratio
    
# def inventory_turnover...
