import pandas as pd
import pandas_ta as ta
from candlestick import candlestick


def testhwmany(df,tstdf):

    df = df[:tstdf.name].iloc[::-1].tail(-1)

    ct = 0
    for ind in df.index:

            if(df['close'][ind]>tstdf['open']):
                break
            else:
                ct+=1
            
    return ct
        

prcDf1 = pd.read_excel('charts.xlsx')
prcDf1['date'] = pd.to_datetime(prcDf1['date'])
prcDf1 = prcDf1.set_index('date')
tsdf  = candlestick.bullish_engulfing(prcDf1, target="bullish_engulfing")
latestfr = tsdf[tsdf['bullish_engulfing'] == True].iloc[-1]


