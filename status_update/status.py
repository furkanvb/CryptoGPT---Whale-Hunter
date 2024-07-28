import sqlite3
import telebot

#General Status Made as a Test
def getdatabase():
    con = sqlite3.connect("../whalehunter/db/database.db")
    cur = con.cursor()
    s = cur.execute("SELECT * FROM coins").fetchall()
    btctotal = 0
    btcstatus = "none"
    btcstatuscount = 0
    btctstatus = 0
    ethtotal = 0
    ethstatus = "none"
    ethstatuscount = 0
    ethtstatus = 0
    altlong = 0
    altshort = 0
    altstatus = "none"
    altshortt = 0
    altlongt = 0
    alttotal = 0
    for i in s:
        if (i[0] == 'BTCUSDT'):
            btctotal = i[2]
            btcstatuscount = i[3]
            btcstatus = i[4]
        elif (i[0] == 'ETHUSDT'):
            ethtotal = i[2]
            ethstatuscount = i[3]
            ethstatus = i[4]
        else:
            if (i[4] == 'long'):
                altlong += 1
                altlongt += i[2]
            elif (i[4] == 'short'):
                altshort += 1
                altshortt += i[2]
            
    if (btcstatuscount >= 4):
        if (btctotal >= 3000000000):
            if (btcstatus == 'short'):
                btctstatus = "Extremly"
            elif (btcstatus == 'long'):
                btctstatus = "Extremly"
        elif (btctotal >= 1500000000):
            if (btcstatus == 'short'):
                btctstatus = "High"
            elif (btcstatus == 'long'):
                btctstatus = "High"
        else:
            if (btcstatus == 'short'):
                btctstatus = "Medium"
            elif (btcstatus == 'long'):
                btctstatus = "Medium"
    elif (btcstatus >= 2):
        if (btctotal >= 1500000000):
            if (btcstatus == 'short'):
                btctstatus = "Extremly"
            elif (btcstatus == 'long'):
                btctstatus = "Extremly"
        elif (btctotal >= 1000000000):
            if (btcstatus == 'short'):
                btctstatus = "High"
            elif (btcstatus == 'long'):
                btcstatus = "High"
        else:
            if (btcstatus == 'short'):
                btctstatus = "Medium"
            elif (btcstatus == 'long'):
                btctstatus = "Medium"
    elif (btcstatus >= 1):
        if (btctotal >= 1000000000):
            if (btcstatus == 'short'):
                btctstatus = "Extremly"
            elif (btcstatus == 'long'):
                btctstatus = "Extremly"
        elif (btctotal >= 500000000):
            if (btcstatus == 'short'):
                btctstatus = "High Short"
            elif (btcstatus == 'long'):
                btctstatus = "High"
        else:
            if (btcstatus == 'short'):
                btctstatus = "Medium"
            elif (btcstatus == 'long'):
                btctstatus = "Medium"
    if (ethstatuscount >= 4):
        if (ethtotal >= 1500000000):
            if (ethstatus == 'short'):
                ethtstatus = "Extremly"
            elif (ethstatus == 'long'):
                ethtstatus = "Extremly"
        elif (ethtotal >= 1000000000):
            if (ethstatus == 'short'):
                ethtstatus = "High"
            elif (ethstatus == 'long'):
                ethtstatus = "High"
        else:
            if (ethstatus == 'short'):
                ethtstatus = "Medium"
            elif (ethstatus == 'long'):
                ethtstatus = "Medium"
    elif (ethstatuscount >= 2):
        if (ethtotal >= 1000000000):
            if (ethstatus == 'short'):
                ethtstatus = "Extremly"
            elif (ethstatus == 'long'):
                ethtstatus = "Extremly"
        elif (ethtotal >= 500000000):
            if (ethstatus == 'short'):
                ethtstatus = "High"
            elif (ethstatus == 'long'):
                ethtstatus = "High"
        else:
            if (ethstatus == 'short'):
                ethtstatus = "Medium"
            elif (ethstatus == 'long'):
                ethtstatus = "Medium"
    elif (ethstatuscount >= 1):
        if (ethtotal >= 500000000):
            if (ethstatus == 'short'):
                ethtstatus = "Extremly"
            elif (ethstatus == 'long'):
                ethtstatus = "Extremly"
        elif (ethtotal >= 250000000):
            if (ethstatus == 'short'):
                ethtstatus = "High "
            elif (ethstatus == 'long'):
                ethtstatus = "High"
        else:
            if (ethstatus == 'short'):
                ethtstatus = "Medium"
            elif (ethstatus == 'long'):
                ethtstatus = "Medium"

    if (altlong > altshort):
        altstatus = "Long"
        alttotal = altlongt
    elif (altshort > altlong):
        altstatus = "Short"
        alttotal = altshortt
    else:
        altstatus = "Long = Short"
        alttotal += altlongt + altshortt
    btctotal = "{:,.2f}".format(btctotal)
    ethtotal = "{:,.2f}".format(ethtotal)
    alttotal = "{:,.2f}".format(alttotal)
    if (btcstatus == 'long'):
        btcstatus = 'Long'
    elif (btcstatus == 'short'):
        btcstatus = 'Short'
    if (ethstatus == 'long'):
        ethstatus = 'Long'
    elif (ethstatus == 'Short'):
            ethstatus= 'Short'
        

    message = f"""
❗️ Crypto Status - CryptoGPT ❗️
👑	Bitcoin: {btcstatus}
💰 Total: {btctotal}$
🎚 Status: {btctstatus}

❗️ Etherium and Altcoins ❗️
💎 Etherium: {btcstatus}
💰 Total: {ethtotal}$
🎚 Status: {ethtstatus}

💲 Altcoins: {altstatus}
💰 Total: {alttotal}$
"""
    bot = telebot.TeleBot("BOTTOKEN")

    bot.edit_message_text(message,chat_id="CHATID",message_id=5)


getdatabase()