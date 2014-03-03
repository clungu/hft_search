__author__ = 'Cristian Lungu'
__author__ = 'lungu.cristian@gmail.com'

import time
import json

class Depth(object):
    asks = None;


lines = [json.loads(line.strip().decode("utf-8")) for line in open("file", "r")]
