from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

HOST = "192.168.0.102"
PORT = 9999

class SylHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body style[background=black;c]><h1>AAAAAAAA</h1></body></html>", "utf-8"))


server = HTTPServer((HOST, PORT), SylHTTP)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="./server.pem")

server.socket = context.wrap_socket(server.socket,server_side=True)



print("Server open")

server.serve_forever()
server.server_close()

print("Server closed")

