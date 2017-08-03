#!/usr/bin/env python3
# do whoislookups from a list of domain names and output expired or not

import socket

def ipwhois(ip):
	

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("whois.apnic.net", 43))
	s.send(ip + "\r\n")

	response = ""
	while True:
	    data = s.recv(4096)
	    response += data
	    if not data:
	        break
	s.close()

	print response

