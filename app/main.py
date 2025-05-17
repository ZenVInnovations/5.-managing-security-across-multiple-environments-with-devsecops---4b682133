from http.server import SimpleHTTPRequestHandler, HTTPServer

PORT = 8000

Handler = SimpleHTTPRequestHandler
httpd = HTTPServer(("", PORT), Handler)

print(f"Serving at http://localhost:{PORT}")
httpd.serve_forever()
