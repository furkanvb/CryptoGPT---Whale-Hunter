from data import getcoindata
import data_utils
from datetime import datetime
import database
from telegram import sendtelegram


def test():
    data = getcoindata("WLDUSDT","1m",1440)
    datacount = data.shape[0] - 1
    t = 0.0
    for i in range(10):
        p = data_utils.getvolpercent(data['Open'][datacount - i],data['Open'][datacount - i] - data['Close'][datacount - i]) * -1
        t += p
        print(t)

test()

def startbot(coinname):
    data = getcoindata(coinname,"1m",1440)
    rsi = data_utils.getrsi(data,7)

    if (rsi >= 70):
    
        signaltime = datetime.timestamp(datetime.now())
        lastsignaltime = database.getdatabasetime(coinname)
        oldtype = database.getsignaltype(coinname)

        if (lastsignaltime + 600 <= signaltime or oldtype == 'short'):
            volume = data_utils.getusdtvolume(data,1440)
            lastvol = data_utils.getusdtvolume(data,10)
            if (lastvol < 200000):
                return
            percent = data_utils.getvolpercent(volume,lastvol)
            price = data_utils.getlastprice(data)
            if (oldtype == 'short'):
                database.updatesignalcount(coinname,0)
                database.updatelastvol(coinname,0)
                database.updatesignaltype(coinname,"long")
            count = database.getsignalcount(coinname) + 1
            t_vol = round(database.getlastvol(coinname) + lastvol,2)
            sendtelegram(coinname,"{:,.2f}".format(lastvol),percent,price,"{:,.2f}".format(t_vol),count,'long')
            database.updatesignalcount(coinname,count)
            database.updatelastvol(coinname,t_vol)
            database.updatedatabasetime(coinname,signaltime)
    elif (rsi <= 30):
        signaltime = datetime.timestamp(datetime.now())
        lastsignaltime = database.getdatabasetime(coinname)
        oldtype = database.getsignaltype(coinname)
    
        if (lastsignaltime + 600 <= signaltime or oldtype == 'long'):
            volume = data_utils.getusdtvolume(data,1440)
            lastvol = data_utils.getusdtvolume(data,10)
            if (lastvol < 200000):
                return
            percent = data_utils.getvolpercent(volume,lastvol)
            price = data_utils.getlastprice(data)
            if (oldtype == 'long'):
                database.updatesignalcount(coinname,0)
                database.updatelastvol(coinname,0)
                database.updatesignaltype(coinname,"short")
            count = database.getsignalcount(coinname) + 1
            t_vol = round(database.getlastvol(coinname) + lastvol,2)
            sendtelegram(coinname,"{:,.2f}".format(lastvol),percent,price,"{:,.2f}".format(t_vol),count,'short')
            database.updatesignalcount(coinname,count)
            database.updatelastvol(coinname,t_vol)
            database.updatedatabasetime(coinname,signaltime)