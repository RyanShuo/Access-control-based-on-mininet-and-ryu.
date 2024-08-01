import http.server
import socketserver
import threading

PORT1 = 8080
PORT2 = 9090

DIRECTORY1 = "site8080"
DIRECTORY2 = "site9090"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.directory = kwargs.pop('directory', None)
        super().__init__(*args, directory=self.directory, **kwargs)

def run_server(port, directory):
    handler = lambda *args, **kwargs: CustomHandler(*args, directory=directory, **kwargs)
    httpd = socketserver.TCPServer(("", port), handler)
    print(f"Serving on port {port}")
    httpd.serve_forever()

threading.Thread(target=run_server, args=(PORT1, DIRECTORY1)).start()
threading.Thread(target=run_server, args=(PORT2, DIRECTORY2)).start()


while True:
    pass