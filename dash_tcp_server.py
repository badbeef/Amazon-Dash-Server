"""
This is a very simple TCP server that does not use SSL. It simply completes
the 3-way handshake and closes the connection.
"""
import SocketServer, SimpleHTTPServer

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
	print 'incoming ', self.client_address[0]
	self.request.close()
	# run your custom code

if __name__ == "__main__":
    # Create the server, binding to localhost on port 443
    server = SocketServer.TCPServer(("", 443), MyTCPHandler)
    server.serve_forever()
