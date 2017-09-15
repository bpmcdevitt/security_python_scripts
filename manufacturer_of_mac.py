#!/usr/bin/env python
# this will use the macvendors.com api to retrieve the manufacturer of the
# given mac address

import sys
import requests

macID = sys.argv[1]

try :
    r = requests.get('https://api.macvendors.com/' + macID)
    print(r.text) 
except:
    print 'There was an error that occurred.' 

