### signal show
```Python
import mplfinance as mpf
import pandas as pd
import numpy as np


def get_signal(df):
    n = df.shape[0]
    ret = []
    for i in range(n):
        if i + 30 >= n:
            ret.append(np.nan)
            continue
        now = df.iloc[i, 3]
        mmin = df.iloc[i+1:i+30, 2].min()
        target = df.iloc[i+1:i+30, 2].max()
        if (mmin > now * 0.995) and (target >= now * 1.01):
            ret.append(df.iloc[i, 2])
        else:
            ret.append(np.nan)
    return ret


if __name__ == '__main__':
    print('signal show')
    df = pd.read_csv('./data.csv', index_col='Date')
    df.index = pd.to_datetime(df.index)
    signal = get_signal(df)
    apd = mpf.make_addplot(signal, type='scatter')
    mpf.plot(df, type='candle', mav=(5,10), addplot=apd)
```
