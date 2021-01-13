import pandas as pd
import numpy as np
def findNaN(_pandas_series, flag = "RETURN_INDEX"):
    if flag == "RETURN_INDEX":
        return _pandas_series[_pandas_series.isnull()].index
    elif flag == "RETURN_REMOVED":
        removed = _pandas_series.drop(_pandas_series[_pandas_series.isnull()].index)
        return removed.reset_index()


def movmean(_pandas_series, window_size, flag = "SHRINK"):
    if flag == "NO_PADDING":
        return _pandas_series.rolling(window=window_size).mean()
    elif flag == "Z_PADDING":
        filtered = _pandas_series.rolling(window=window_size).mean()
        filtered.drop(np.nan)
        return filtered
    elif flag == "SHRINK":
        def shrinking(filtered_series, window_size):
            if window_size == 1 :
                return filtered_series
            else:
                mean_val = filtered_series.iloc[:window_size].mean()
                filtered_series.iloc[window_size-1] = mean_val
                return shrinking(filtered_series, window_size -1 )

        filtered = _pandas_series.rolling(window=window_size).mean()
        filtered[:window_size] = _pandas_series.iloc[:window_size]
        filtered = shrinking(filtered, window_size - 1)
        return filtered
        




