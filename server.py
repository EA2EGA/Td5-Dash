import http.server
 
Handler = http.server.SimpleHTTPRequestHandler
 
def run():
  print('starting server...')
 
  # Server settings
  # Choose port 8080, for port 80, which is normally used for a http server, you need root access
  server_address = ('127.0.0.1', 8080)
  http.server.httpd = http.server.HTTPServer(server_address, Handler)
  print('running server...')
  http.server.httpd.serve_forever()
 
 
run()