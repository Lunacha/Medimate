from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO


class MediServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        file_content = self.rfile.read(content_length)
        print(file_content)
        self.send_response(200, 'OK')


serv = HTTPServer(('localhost', 8080), MediServer)
serv.serve_forever()
