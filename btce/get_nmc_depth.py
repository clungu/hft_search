__author__ = 'Cristian Lungu'
__author__ = 'lungu.cristian@gmail.com'

import time
import json
import urllib.request

from datetime import datetime


'''
    {
        timestamp : 1234567890
        event: depth
        value: { ask ... }
    }
        timestamp : 1234567891
        event: trade
        value: { trade ... }
    {

'''
def writeDepthEvent(file, lastContent) :
    try:
        content = json.loads(urllib.request.urlopen("https://btc-e.com/api/2/ltc_btc/depth").read().decode("utf-8"))
        if lastContent != content :
            file.write(str({
                "timestamp" : time.time(),
                "event" : "depth",
                "value" : content
            })+"\n")
        return content
    except:
        pass

def writeTradeEvents(file, lastTrades) :
    try:
        trades = json.loads(urllib.request.urlopen("https://btc-e.com/api/2/ltc_btc/trades").read().decode("utf-8"))
        for trade in reversed(trades):
            if trade not in lastTrades:
                print(trade)
                file.write(str({
                    "timestamp" : time.time(),
                    "event" : "trade",
                    "value" : trade
                })+"\n")
        return trades
    except:
        pass

start = time.time()
content = json.loads("{}")
trades = json.loads("[] ")
data = open(str(int(time.time())), "w")
while time.time() - start < 100000 :
    content = writeDepthEvent(data, content)
    trades = writeTradeEvents(data, trades)