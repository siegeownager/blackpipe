from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import base64_handler
import decrypter
import home
import logging

home.home_generate()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def run(httpd):
    httpd.serve_forever()


class RequestHandler(BaseHTTPRequestHandler):
    """Class that implements a basic HTTP server"""

    def do_GET(self):
        """Handler for HTTP GET methods"""

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello World!')

    def do_POST(self):
        """Handler for HTTP POST methods"""

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)  # Body of the POST method
        self.send_response(200)
        self.end_headers()
        cipher_handler(body.decode('utf-8'))    # The cipher handler method is invoked
        response = BytesIO()
        response.write(b'Received!\n')
        self.wfile.write(response.getvalue())


def initialize():
    """Initialize the HTTP server"""

    server_address = ('', 8000)
    httpd = HTTPServer(server_address, RequestHandler)
    run(httpd)


def cipher_handler(body):
    """This function decodes and then decrypts the incoming base64 encoded PGP message"""

    ciphertext = base64_handler.base64_to_data(body)
    passphrase = 'testing'
    logging.debug(ciphertext)
    decrypted_text = decrypter.decrypt(ciphertext, passphrase)
    print(decrypted_text)


initialize()
