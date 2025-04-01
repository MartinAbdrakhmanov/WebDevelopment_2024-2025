import socket
import threading

def receive_messages(conn):
    """Получает сообщения от сервера и выводит их на экран."""
    while True:
        try:
            message = conn.recv(1024).decode().strip()
            if message:
                print(message)
        except Exception as e:
            print(f"Ошибка при получении сообщения: {e}")
            break

def send_messages(conn):
    """Отправляет сообщения на сервер."""
    while True:
        message = input() 
        if message:
            conn.send(message.encode())  

def start_client():
    """Запуск клиента, подключение к серверу и управление потоками."""
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect(("localhost", 8000))  

    threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

    threading.Thread(target=send_messages, args=(conn,), daemon=True).start()

    while True:
        pass

if __name__ == "__main__":
    start_client()
