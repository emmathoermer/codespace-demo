from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"这是一个codespace测试页面！")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), Handler)
    print("Server running on port 8000...")
    server.serve_forever()
