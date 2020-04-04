from http.server import HTTPServer, BaseHTTPRequestHandler


def run(httpd):
    httpd.serve_forever()


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)


server_address = ('', 8000)
httpd = HTTPServer(server_address, RequestHandler)
run(httpd)