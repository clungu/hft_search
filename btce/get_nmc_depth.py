__author__ = 'Cristian Lungu'
__author__ = 'lungu.cristian@gmail.com'

import time
import urllib.request


while(time.time()) {
    content = urllib.request.urlopen("https://btc-e.com/api/2/ltc_btc/depth").read()
}
print(content)
