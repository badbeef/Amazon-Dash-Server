"""
This is the fake SSL server that fools Amazon Dash button to make it believe
this is its mothership. You need the cert.pem file.
"""
import BaseHTTPServer, SimpleHTTPServer, ssl

class MyHTTPHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(s):
	print 'GET', s.path

    def do_POST(s):
	print 'POST', s.path

if __name__ == "__main__":
    # Create the server, binding to localhost on port 443
    httpd = BaseHTTPServer.HTTPServer(('', 443), MyHTTPHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, certfile='cert.pem', 
				    server_side=True)
    httpd.serve_forever()
