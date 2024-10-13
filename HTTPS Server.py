from http.server import HTTPServer, BaseHTTPRequestHandler


class SylHTTP(BaseHTTPRequestHandler):
    def do_get(self)
    self.send_response(200)
    self.send_header("content-type", "text/html")
    self.end:headers

    self.wfile.write(bytes(SylHTTP)) 

