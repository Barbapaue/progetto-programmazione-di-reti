import base64
import json
import socketserver
from socketserver import ThreadingMixIn
from typing import Tuple
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, HTTPServer
import html


class WebServer(BaseHTTPRequestHandler):
    key = ''

    def __init__(self, request: bytes, client_address: Tuple[str, int], s: socketserver.BaseServer):
        self.set_auth_root()
        super().__init__(request, client_address, s)

    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header(
            'WWW-Authenticate', 'Basic realm="Demo Realm"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        key = self.get_auth_key()

        if self.headers.get('Authorization') is None:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'No auth header received'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

        elif self.headers.get('Authorization') == 'Basic ' + str(key):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(
                (html.header() + html.hospitalFeatureTitle() + html.hospitalFeature() + html.footer()).encode())

        else:
            self.do_AUTHHEAD()

            response = {
                'success': False,
                'error': 'Invalid credentials'
            }

            self.wfile.write(bytes(json.dumps(response), 'utf-8'))

    def _parse_GET(self):
        get_vars = parse_qs(urlparse(self.path).query)
        return get_vars

    def set_auth_root(self, username='root', password='root'):
        self.key = base64.b64encode(
            bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')

    def get_auth_key(self):
        return self.key


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


def run():
    server = ThreadedHTTPServer(('localhost', 8080), WebServer)
    try:
        print('Starting server, use <Ctrl-C> to stop')
        server.serve_forever()
        server.daemon_threads = True
        server.allow_reuse_address = True
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == '__main__':
    run()

