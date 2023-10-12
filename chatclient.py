import socket
import threading
import time


def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)


def send_alive_messages(client_socket):
    while True:
        time.sleep(10)  # Send alive message every 10 seconds
        client_socket.send('Alive'.encode('utf-8'))


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    client_id = input("Enter your ID: ")
    client_socket.send(client_id.encode('utf-8'))

    receive_thread = threading.Thread(
        target=receive_messages, args=(client_socket,))
    receive_thread.start()

    alive_thread = threading.Thread(
        target=send_alive_messages, args=(client_socket,))
    alive_thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))


if __name__ == "__main__":
    main()
