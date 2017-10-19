#!/usr/bin/env python
# create a list of CVE for a given search term
# using the URL cvedetails.com 
# currently this will only retrieve the first 50 page results for a given
# vendor search 

# TO ADD:
# argeparse ability to give cmd line options for --all results, --page results
# implement requests sessions and add rate limit header - http://docs.python-requests.org/en/master/user/advanced/

from bs4 import BeautifulSoup
import requests
import re
import sys 

class Cve_search(object):

    def __init__(self):
        self.base_url = "http://www.cvedetails.com"
        self.cve_lookup_rel_url = '/cve/'
        self.search_url = "http://www.cvedetails.com/vendor-search.php?search="
        self.search_term = sys.argv[1]

    def usage(self):
        return

    def search(self):
        r = requests.get(self.search_url + self.search_term)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        for vuln_link_url in soup.find_all('a', attrs={ 'href' : re.compile("vulnerability-list")}):
            vuln_link_response = vuln_link_url.get('href')

        return vuln_link_response

    def list_of_cve(self):
        r = requests.get(self.base_url + self.search())
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        cve_numbers = []

        for link in soup.find_all('a', attrs={ 'href' : re.compile("CVE-")}):
            cve_string = link.get('href').strip('/cve/').encode('utf-8')
            cve_numbers.append(cve_string)

        return cve_numbers

    def lookup(self, cve_number):
        r = requests.get(self.base_url + self.cve_lookup_rel_url + cve_number)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')

        for link in soup.find_all('meta', attrs={ 'content' : re.compile("CVE-\d{4}-\d{4,7} :")}):
            return link.get('content')

cve = Cve_search()

def cve_summary_search():
    for cve_num in cve.list_of_cve():
        results = cve.lookup(cve_num) + "\n" 
    return results

print cve_summary_search()
