import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 65432))
server_socket.listen()

print("Servidor esperando conexiones...")
connection, address = server_socket.accept()

with connection:
    print(f"Conectado a {address}")
    with open('imagen_recibida.jpg', 'wb') as image:
        while True:
            data = connection.recv(4096)
            if not data:
                break
            image.write(data)
    print("La imagen ha sido recibida y guardada.")
# \\\