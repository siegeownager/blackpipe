from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


def run(httpd):
    httpd.serve_forever()


class RequestHandler(BaseHTTPRequestHandler):
    """Class that implements a basic HTTP server"""

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World!')

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
run(httpd)
