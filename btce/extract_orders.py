__author__ = 'Cristian Lungu'
__author__ = 'lungu.cristian@gmail.com'

import time
import json

'''
    {
        timestamp : 1234567890
        event: depth
        value: { ask ... }
    },
    {
        timestamp : 1234567891
        event: trade
        value: { trade ... }
    {

'''

class Depth:
    def __init__(self, depthImage):
        self.depth = depthImage

    def change(self, side, price, deltaSize):
        return

    def trade(self, side, price, quantity):
        return

for line in open("1393796251", "r"):
    event = json.loads(str(line.strip()).replace("'", "\""))
    if event['event'] == 'depth':
        print("{0} {1}".format('Depth', event['value']))
    elif event['event'] == 'trade':
        print("{0} {1}".format('Event', event['value']))