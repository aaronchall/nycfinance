class BalanceSheet:
    """
    >>> bs = BalanceSheet(current_assets=5000, current_liabilities=4000, retained_earnings=...)
    >>> print(bs)
            Assets     =   Liabilities    +   Owner's Equity
    Current     5000     Current    4000      Retained Earnings   6000
    Long-term  20000     Long-term 10000      Common Stock        5000
    Net        25000     Net       14000      Total              11000    
    ================    ================      ========================
    >>> print(bs.detailed)
    ... # every line item
    """
    @property
    def total_assets(self):
        """bs.total_assets -> total_assets if have it, else -> sum of current and long-term assets."""
        if not hasattr(self, '_total_assets'):
            self._total_assets = self.current_assets + self.long_term_assets
        return self._total_assets

    @total_assets.setter
    def total_assets(self, value):
        """setting may invalidate the otherwise dependencies"""
        self._total_assets = value
        
    @total_assets.deleter
    def total_assets(self):
        """delete to invalidate"""
        del self._total_assets
        
    @property
    def current_assets(self):
        if not hasattr(self, '_current_assets'):
            self._current_assets = (
              self.cash + self.marketable_securities + self.accounts_receivable +
              self.inventory + self.prepaid_expenses)
        return self._current_assets

    @current_assets.setter
    def current_assets(self, value):
        """setting may invalidate the otherwise dependencies"""
        self._current_assets = value
        
    @current_assets.deleter
    def current_assets(self):
        """delete to invalidate"""
        del self._current_assets
        
        

