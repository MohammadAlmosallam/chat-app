import socket
import threading
import time

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        print(message)

# Function to send alive messages to the server at regular intervals
def send_alive_messages(client_socket):
    while True:
        time.sleep(10)  # Send alive message every 10 seconds
        client_socket.send('Alive'.encode('utf-8'))

# The main function
def main():
    # Create a client socket and connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Get the client's ID and send it to the server
    client_id = input("Enter your ID: ")
    client_socket.send(client_id.encode('utf-8'))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(
        target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Start a thread to send alive messages to the server
    alive_thread = threading.Thread(
        target=send_alive_messages, args=(client_socket,))
    alive_thread.start()

    while True:
        # Continuously read user input and send it to the server
        message = input()
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
