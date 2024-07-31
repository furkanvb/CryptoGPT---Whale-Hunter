from data import getcoindata
import pandas_ta as ta


def getrsi(data,len):
    rsi = ta.rsi(data['Close'],len)
    return rsi[data.shape[0] - 1]

def getvolume(data,len):
    volume = 0
    datacount = data.shape[0]
    for i in range(len):
        volume += data['Volume'][datacount - 1 - i]
    return round(volume, 2)

def getusdtvolume(data,len):
    volume = 0
    datacount = data.shape[0]
    for i in range(len):
        volume += (data['Volume'][datacount - 1 - i] * data['Close'][datacount - 1 - i])
    return round(volume, 2)

def getlastprice(data):
    return (data['Close'][data.shape[0] - 1])

def getvolpercent(volume,lastvolume):
    percent = ((lastvolume / (volume)) * 100)
    return round(percent, 2)
