from http.server import HTTPServer, CGIHTTPRequestHandler
import webbrowser

webbrowser.open ('http://localhost:8000/', new=2)
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()
