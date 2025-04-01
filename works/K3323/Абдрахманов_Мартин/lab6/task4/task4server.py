import socket
import threading
import time
import queue

# entering = []
# leaving = []
# messages = []

clients = {}

# Клиентская структура
class Client:
    def __init__(self, name, conn, ch):
        self.name = name
        self.conn = conn
        self.ch = ch

# Функция для объявления списка клиентов
def announce_clients():
    while True:
        time.sleep(10)
        client_names = [client.name for client in clients.values()]
        announcement = "List of online users: \n" + "\n".join(client_names) + "\n"
        for client in clients.values():
            client.ch.put(announcement)

# Обработчик подключения клиента
def handle_client(conn, ch):
    try:
        conn.send(b"Enter your name: ")
        name = conn.recv(1024).decode().strip()
        if not name:
            name = conn.getpeername()[0]  # Используем IP-адрес, если имя не введено
        conn.send(f"You are {name}\n".encode())

        client = Client(name, conn, ch)
        clients[name] = client

        # Уведомляем других клиентов о новом подключении
        broadcast(f"{name} has arrived", name)

        # Таймер для разрыва соединения через 5 минут
        timeout_timer = threading.Timer(300, lambda: disconnect_client(name))
        timeout_timer.start()

        # Работа с сообщениями
        while True:
            msg = conn.recv(1024).decode().strip()
            if msg:
                broadcast(f"{name}: {msg}", name)
                timeout_timer.cancel()
                timeout_timer = threading.Timer(300, lambda: disconnect_client(name))
                timeout_timer.start()
            else:
                break
    finally:
        disconnect_client(name)

# Функция для широковещательной передачи сообщений всем клиентам
def broadcast(message, sender_name=None):
    for client in clients.values():
        if sender_name != client.name:
            try:
                client.conn.send(message.encode())
            except:
                pass


def disconnect_client(name):
    if name in clients:
        client = clients.pop(name)
        client.conn.send(f"You have been disconnected due to inactivity\n".encode())
        broadcast(f"{name} has left", name)
        client.conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8000))
    server_socket.listen(5)

    print("Server is running on port 8000...")

    # Поток для объявлений онлайн пользователей
    threading.Thread(target=announce_clients, daemon=True).start()

    while True:
        conn, addr = server_socket.accept()
        print(f"New connection from {addr}")
        ch = queue.Queue()
        threading.Thread(target=handle_client, args=(conn, ch), daemon=True).start()

if __name__ == "__main__":
    start_server()
