#!/usr/bin/env python3
"""
Preview server for Student Support Persona Cards.
Static file server — serves index.html, card.html, css/, and data/.
Run: python3 server.py
Visit: http://127.0.0.1:8766/
"""
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import os

BASE_DIR = Path(__file__).parent

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(BASE_DIR), **kwargs)

    def log_message(self, format, *args):
        print(f"  {self.address_string()} → {format % args}")

    def do_GET(self):
        # Route / to index.html
        if self.path == "/" or self.path == "":
            self.path = "/index.html"
        super().do_GET()

if __name__ == "__main__":
    port = 8766
    server = HTTPServer(("127.0.0.1", port), Handler)
    print(f"✦ Student Support Persona Cards")
    print(f"  Preview server running at http://127.0.0.1:{port}/")
    print(f"  Press Ctrl+C to stop.\n")
    server.serve_forever()
