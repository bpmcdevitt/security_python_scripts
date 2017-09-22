#!/usr/bin/env python
# this will be my all-in-one shodan tool
# https://shodan.readthedocs.io/en/latest/tutorial.html

import shodan
import sys
import creds


api = shodan.Shodan(creds.SHODAN_API_KEY)

# Wrap the request in a try/ except block to catch errors
try:
        # Search Shodan
        results = api.search(sys.argv[1])

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print 'IP: %s' % result['ip_str']
                print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e
