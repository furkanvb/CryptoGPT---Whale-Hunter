import pandas as pd
from ccxt import binanceusdm
import requests
import json

def getcoindata(coinname, time, limit):
    try:
        binance = binanceusdm()
        data = binance.fetch_ohlcv(coinname, time, limit=limit)
    except Exception as exp:
        print(f"Coinname:{coinname} {exp}")
    pddata = pd.DataFrame(data=data,columns=("Time", "Open", "High", "Low", "Close", "Volume"))
    return pddata
    
def getcoinlist(savename):
    url = "https://www.binance.com/bapi/futures/v1/public/future/common/symbol-config-info"
    req = requests.post(url,json={})
    req = json.loads(req.text)
    with open(savename,'a+') as save:
        for i in req['data']['configInfoList']:
            save.write(i['symbol'] + '\n')
