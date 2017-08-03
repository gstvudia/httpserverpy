#!/usr/bin/python

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import urllib
import cgi

class HTTPHandler(BaseHTTPRequestHandler):
	
	user = 0
	balance = 0
	pin = 0
	result = 0
	
    def do_GET(self):
	
		if "/unlock" in self.path:
			
			self.send_response(200)
	
			self.send_header('Content-type','text/html')
			self.end_headers()
	
			qs = {}
			x,params = self.path.split('?')
			qs = urllib.parse.parse_qs(params)
			
			user = str(qs['user'])
			user = user.replace('[','').replace(']','').replace("'",'')
			
			balance = str(qs['balance'])
			balance = balance.replace('[','').replace(']','').replace("'",'')
			
			pin = str(qs['pin'])
			pin = user.pin('[','').replace(']','').replace("'",'')
			
			if int(balance) > 0:
				
				result = 1
				self.wfile.write(bytes(result, "utf8"))
				## result 1 means unlocked
			else:
				
				result = 0
				self.wfile.write(bytes(result, "utf8"))
				## result 0 means insuficient balance
		return

http_server=socketserver.TCPServer(("",8081), HTTPHandler)
print('Running Server...')
http_server.serve_forever()	