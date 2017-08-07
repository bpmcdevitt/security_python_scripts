#!/usr/bin/env python3
# do whoislookups from a list of domain names and output expired or not

import socket

class Whois(object):
	''' The Whois class which will handle all whois lookups via python'''
	
	def __init__(self):
		pass
	
	def iplookup(self, ip):

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
		s.connect(("whois.arin.net", 43))
		s.send(ip + "\r\n")

		response = ""
		while True:
			data = s.recv(4096)
			response += data
			if not data:
				break
		s.close()

		return response

	def domainlookup(self, domain):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("whois.verisign-grs.com", 43))
		s.send(ip + "\r\n")

		response = ""
		while True:
			data = s.recv(4096)
			response += data
			if not data:
				break
		s.close()

		return response
