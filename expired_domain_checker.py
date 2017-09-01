#!/usr/bin/env python3
# do whoislookups from a list of domain names and output expired or not

import socket 

class Whois(object):
    ''' The Whois class which will handle all whois lookups via python'''
    def lookup(self, query, remote):
        '''Perform a lookup against remote for query'''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((remote, 43))
        s.send(query + "\r\n")

        response = ""
        while True:
            data = s.recv(4096)
            response += data
            if not data:
                break
        s.close()
        return response

    def domainlookup(self, domain):
        '''Perform a domain lookup'''
        return self.lookup(domain, "whois.verisign-grs.com")

    def iplookup(self, ip):
        '''Perform an ip lookup'''
        return self.lookup(ip, "whois.arin.net")

whois = Whois()
print(whois.domainlookup('google.com'))
