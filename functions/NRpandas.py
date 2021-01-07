import pandas as pd

def findNaN(_pandas_series, MODE = "RETURN_INDEX"):
    if MODE == "RETURN_INDEX":
        return _pandas_series[_pandas_series.isnull()].index
    elif MODE == "RETURN_REMOVED":
        removed = _pandas_series.drop(_pandas_series[_pandas_series.isnull()].index)
        return removed.reset_index()


