import socket
import threading

clients = {}
clients_lock = threading.Lock()


def handle_client(client_socket, client_id):
    global clients
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')

            if not message:
                remove_client(client_id)
                break

            if message.startswith('@Quit'):
                remove_client(client_id)
                break
            elif message.startswith('@List'):
                send_client_list(client_socket)
            elif message.startswith('('):

                target_client_id, msg_content = parse_message(message)
                send_message(target_client_id, f'({client_id}) {msg_content}')
        except:

            remove_client(client_id)
            break


def parse_message(message):
    # Parse message and extract target client ID and message content
    # Implement your parsing logic here based on the given message format
    pass


def send_client_list(client_socket):
    global clients
    client_list = ', '.join(list(clients.keys()))
    client_socket.send(client_list.encode('utf-8'))


def send_message(target_client_id, message):
    global clients
    with clients_lock:
        if target_client_id in clients:
            target_client_socket = clients[target_client_id]
            target_client_socket.send(message.encode('utf-8'))
        else:
            print(f'Client {target_client_id} is not online.')


def remove_client(client_id):
    global clients
    with clients_lock:
        del clients[client_id]
        print(
            f'Client {client_id} disconnected. Online clients: {list(clients.keys())}')


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)

    print('Server listening on port 12345...')

    while True:
        client_socket, addr = server_socket.accept()
        client_id = client_socket.recv(1024).decode('utf-8')
        with clients_lock:
            clients[client_id] = client_socket
            print(
                f'Client {client_id} connected. Online clients: {list(clients.keys())}')
        client_handler = threading.Thread(
            target=handle_client, args=(client_socket, client_id))
        client_handler.start()


if __name__ == "__main__":
    main()
