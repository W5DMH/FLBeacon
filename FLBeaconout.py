#!/usr/bin/env python
import os
import time
import six

if six.PY2:
    import ConfigParser as configparser
else:
    import configparser
import sys

import pyfldigi
fldigi = pyfldigi.Client(hostname='127.0.0.1', port=7362)  # <-- Constructor call
#fldigi.rig.frequency = 14074650.000


parser = configparser.ConfigParser()
parser.read('FLBeacon.conf')

#print(parser.get('MessageConfig', 'Callsign1'))
#print(parser.get('MessageConfig', 'Callsign2'))
#print(parser.get('MessageConfig', 'Message'))
#print(parser.getint('MessageConfig', 'timer'))

callsign1Get = (parser.get('MessageConfig', 'Callsign1'))
callsign2Get = (parser.get('MessageConfig', 'Callsign2'))
messageGet = (parser.get('MessageConfig', 'message'))
timerGet = (parser.getint('MessageConfig', 'timer'))



#newbeaconVal = "./txbeacon.py -c 20 " + callsign2Get + " " + callsign2Get +" DE " + callsign1Get +" "+ callsign1Get +" "+ messageGet
#print(newbeaconVal)
messagevar = " " + callsign2Get + " " + callsign2Get +" de " + callsign1Get +" "+ callsign1Get +" "+ messageGet
#print(messagevar)
#fldigi.main.send(messagevar,timeout=45)

while True:
   fldigi.main.send(messagevar,timeout=45)
   print("sleeping") 
   time.sleep(timerGet)



