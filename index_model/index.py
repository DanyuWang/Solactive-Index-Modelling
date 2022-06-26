import pandas as pd
import numpy as np
import datetime as dt


class IndexModel:
    def __init__(self):
        self._prices = pd.read_csv(r'./data_sources/stock_prices.csv', index_col=0)
        self._prices.index = pd.to_datetime(self._prices.index, format='%d/%m/%Y')
        self._prices.sort_values('Date', inplace=True)

        self._universe = self._prices.columns
        self._weight = [0.5, 0.25, 0.25]
        self._num_compo = len(self._weight)
        self._base = 100

        # index values
        self._index = pd.Series(index=self._prices.index, name='index_level')

        pass

    def calc_index_level(self, start_date: dt.date, end_date: dt.date):
        """
        Calculate index value within given date range.
        :param start_date: start date of index
        :param end_date: end date of index
        """
        prices_grouped = self._prices[self._universe].reset_index().\
            groupby(pd.PeriodIndex(self._prices.index, freq='M'))
        last_day_prices = prices_grouped.last().drop('Date', axis=1)
        first_day_prices = prices_grouped.first().shift(-1).dropna()

        # select top 3 stocks based on their last month prices
        rank = pd.DataFrame(np.zeros((len(last_day_prices), self._num_compo)),
                            columns=range(1, self._num_compo+1),
                            index=last_day_prices.index)
        for i in last_day_prices.index:
            rank.loc[i, :] = last_day_prices.T.nlargest(self._num_compo, i).index.tolist()
        rank = rank.shift().dropna()

        self._index = self._index[start_date:end_date]
        self._index[0] = self._base

        # update index value monthly, from the first trading day of the month to the next first trading day.
        for name, group in prices_grouped:
            if name not in rank.index:
                continue

            if name in first_day_prices.index:
                price_month = group.append(first_day_prices.loc[name])
                price_month.set_index('Date', inplace=True)
            else:
                price_month = group.set_index('Date')

            # calculate the daily total return and cumulative return
            ret_month = price_month[rank.loc[name, :]].pct_change().replace(np.nan, 0) + 1
            ret_month = ret_month.cumprod()
            # index value = composition weight*beginning index value of three compositions*cumulative return
            self._index.update(self._index.update((self._index.dropna()[-1] * ret_month)@self._weight))

        pass

    def export_values(self, file_name: str):
        """
        Generate csv file for index value
        :param file_name: file directory and name
        """
        self._index.round(2).to_csv(file_name)

        pass
