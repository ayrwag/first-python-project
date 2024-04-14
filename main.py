from http.server import HTTPServer, BaseHTTPRequestHandler


HOST = "localhost"
PORT = 9999
# Step 1. Receive an MP3 file
class WhispherHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()

		self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>","utf-8"))


server = HTTPServer((HOST,PORT), WhispherHTTP)
print("Server now running on",HOST+":"+str(PORT)+"...")

server.serve_forever()
server.server_close()
print("Server stopped...")
# Step 2. Pass it to "whisper" package

# Step 3. Return a JSON text transcript