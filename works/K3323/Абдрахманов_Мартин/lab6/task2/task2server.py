import socket
import math

def handle_conn(conn):
    with conn:
        while True:
            try:
                data = conn.recv(1024).decode().strip()
                if not data:
                    break
                
                parts = data.split()
                if len(parts) < 2:
                    print("Неверный формат данных")
                    continue
                
                try:
                    a = int(parts[0])
                    b = int(parts[1])
                except ValueError:
                    print("Ошибка преобразования чисел")
                    continue
                
                c = math.hypot(a, b)
                ans = f"c = {c}\n"

                conn.sendall(ans.encode())

            except Exception as e:
                print(f"Ошибка: {e}")
                break

def main():
    host = "localhost"
    port = 8080
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Сервер запущен на {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Подключение от {addr}")
            handle_conn(conn)

if __name__ == "__main__":
    main()
