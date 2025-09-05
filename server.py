from livereload import Server
PORT = 5500
server = Server()
server.watch('*.html')
server.watch('*.css')
server.watch('*.js')
print(f"Abre tu navegador en: \nhttp://localhost:{PORT}")
server.serve(root='.', port=PORT)
