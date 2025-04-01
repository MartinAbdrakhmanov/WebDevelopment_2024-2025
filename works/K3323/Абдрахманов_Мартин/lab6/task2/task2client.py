import socket

def main():
    host = "localhost"
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        while True:
            numbers = input("Введите два числа через пробел (или 'exit' для выхода): ")
            if numbers.lower() == "exit":
                break
            
            client_socket.sendall((numbers + "\n").encode())

            data = client_socket.recv(1024).decode().strip()
            print(f"Ответ от сервера: {data}")

if __name__ == "__main__":
    main()
