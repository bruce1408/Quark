import http.server, json, os, sys

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'knowledge-graph.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=PROJECT_ROOT, **kwargs)

    def do_GET(self):
        if self.path == '/api/graph':
            try:
                with open(GRAPH_PATH) as f:
                    data = json.load(f)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps(data, ensure_ascii=False).encode())
                return
            except Exception as e:
                self.send_response(500)
                self.end_headers()
                self.wfile.write(str(e).encode())
                return
        return super().do_GET()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
    print(f'Dashboard: http://127.0.0.1:{port}/.understand-anything/dashboard.html')
    print(f'Graph API: http://127.0.0.1:{port}/api/graph')
    try:
        http.server.HTTPServer(('127.0.0.1', port), Handler).serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
