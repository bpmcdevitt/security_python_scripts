#!/usr/bin/env python3
# do whoislookups from a list of domain names and output expired or not

import socket 
import re

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

'''Instantiate the class to make ourselves an object to work with'''
whois = Whois()

def domain_list(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    return content

if __name__ == '__main__':

    response = ""
    filename = 'domainlist.txt'

    for domain in domain_list(filename):
        response += whois.domainlookup(domain)

    try:
        expired_date = re.findall('Registry Expiry Date:.*', response)
    except AttributeError:
        expired_date = ''

    for domain, expiration in zip(domain_list(filename), expired_date):
        print domain + '\t' + expiration

