import sqlite3


def getdatabasetime(coinname):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    a = cursor.execute(f"SELECT lastwar FROM coins WHERE coinname = '{coinname}';").fetchone()
    cursor.close()
    data.close()
    return int(a[0])



def updatedatabasetime(coinname,newtime):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    cursor.execute(f"UPDATE coins SET lastwar = {newtime} WHERE coinname = '{coinname}';")
    data.commit()
    cursor.close()
    data.close()

def getsignalcount(coinname):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    a = cursor.execute(f"SELECT signalcount FROM coins WHERE coinname = '{coinname}';").fetchone()
    cursor.close()
    data.close()
    return int(a[0])

def getsignaltype(coinname):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    a = cursor.execute(f"SELECT signaltype FROM coins WHERE coinname = '{coinname}';").fetchone()
    cursor.close()
    data.close()
    return a[0]

def updatesignaltype(coinname,newtype):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    cursor.execute(f"UPDATE coins SET signaltype = '{newtype}' WHERE coinname = '{coinname}';")
    data.commit()
    cursor.close()
    data.close()

def updatesignalcount(coinname,newcount):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    cursor.execute(f"UPDATE coins SET signalcount = {newcount} WHERE coinname = '{coinname}';")
    data.commit()
    cursor.close()
    data.close()


def getlastvol(coinname):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    a = cursor.execute(f"SELECT lastvol FROM coins WHERE coinname = '{coinname}';").fetchone()
    cursor.close()
    data.close()
    return int(a[0])

def updatelastvol(coinname,newvol):
    data = sqlite3.connect("db/database.db")
    cursor = data.cursor()
    cursor.execute(f"UPDATE coins SET lastvol = {newvol} WHERE coinname = '{coinname}';")
    data.commit()
    cursor.close()
    data.close()