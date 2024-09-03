from http.server import HTTPServer
from Handler.Tranding_handler import RequestHandler

host = "0.0.0.0"
port = 5000

if __name__ == "__main__":
    try:
        server = HTTPServer((host, port), RequestHandler)
        print(f"Starting server at http://{host}:{port}")
        server.serve_forever()
    except Exception as e:
        print(f"Failed to start server: {e}")