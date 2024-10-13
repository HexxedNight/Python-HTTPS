from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

HOST = "192.168.0.1"
PORT = 9999

class SylHTTP(BaseHTTPRequestHandler):
    def do_get(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>AAAAAAAA</h1></body></html>, "utf-8")) 

server = HTTPServer((host, port), SylHTTP)

print("Server open")

server.serve_forever()
server.server_close()

print("Server closed")
