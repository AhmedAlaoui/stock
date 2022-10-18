import logging

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LogisticRegression


def create_features(df_stock, nlags=30):
    df_resampled = df_stock.copy()
    df_resampled['diff close'] = df_resampled['close'].diff()
    df_resampled['out'] = df_resampled['diff close'].apply(lambda x: 'Sell' if x < 0 else 'Buy')
    lags_col_names = []
    for i in range(nlags + 1):
        df_resampled['lags_' + str(i)] = df_resampled['diff close'].shift(i)
        lags_col_names.append('lags_' + str(i))
    lags_col_names = lags_col_names + ['out']
    df = df_resampled[lags_col_names]
    print(df)
    df = df.dropna(axis=0)
    print(df)
    return df


def create_X_Y(df_lags):
    X = df_lags.drop('out', axis=1)
    Y = df_lags[['out']]
    return X, Y


class Stock_model(BaseEstimator, TransformerMixin):

    def __init__(self, data_fetcher):
        self.log = logging.getLogger()
        self.lr = LogisticRegression()
        self._data_fetcher = data_fetcher
        self.log.warning('here')

    def fit(self, X, Y=None):
        data = self._data_fetcher(X)
        df_features = create_features(data)
        df_features, Y = create_X_Y(df_features)
        self.lr.fit(df_features, Y)
        return self

    def predict(self, X, Y=None):
        print(X)
        data = self._data_fetcher(X, last=True)
        print(data)
        df_features = create_features(data)
        print(df_features)
        df_features, Y = create_X_Y(df_features)
        predictions = self.lr.predict(df_features)
        print(predictions)

        return predictions.flatten()[-1]
