import socket

def server_hello():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 8888))
    print("Cервер запущен на порту 8888")

    while True:
        message, client_address = server_socket.recvfrom(1024)
        print(f"Получено сообщение: {message.decode()} от {client_address}")
        server_socket.sendto(b"Hello, client", client_address)

if __name__ == '__main__':
    server_hello()