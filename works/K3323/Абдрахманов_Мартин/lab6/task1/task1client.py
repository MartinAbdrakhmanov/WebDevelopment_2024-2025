import socket

def client_hello():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.sendto(b"Hello, server", ("localhost", 8888))
    response, _ = client_socket.recvfrom(1024)
    print(f"Ответ сервера: {response.decode()}")

if __name__ == '__main__':
    client_hello()