**Repository Description:**

This GitHub repository contains a Python implementation of a multi-client chat application using sockets and multithreading. The project consists of two main components: `chatserver.py` for handling client connections and messages, and `chatclient.py` for client-side interaction. Clients can connect to the server, send messages to each other via the server, request the list of online clients, and maintain their online status through regular alive messages.

**Project Overview:**

- **chatserver.py:** This file represents the server-side implementation of the chat application. It creates a socket to handle client connections, manages client messages, maintains the list of online clients, and ensures proper communication between clients.

- **chatclient.py:** This file represents the client-side implementation. Clients can connect to the server, send messages to other clients, receive messages, request the list of online clients, and maintain their online status.

**How to Use:**

1. **Clone the Repository:**
   ```
   git clone https://github.com/MohammadAlmosallam/multi-threaded-server.git
   ```

2. **Run the Server:**
   ```
   python chatserver.py
   ```
   The server will start and listen for client connections.

3. **Run Clients:**
   ```
   python chatclient.py
   ```
   Clients can connect to the server by providing their unique ID.

4. **Interact with the Chat Application:**
   - Clients can send messages to other clients using the format `(client_id) message`.
   - Clients can request the list of online clients by typing `@List`.
   - Clients can disconnect from the server by typing `@Quit`.

**Project Structure:**

- **chatserver.py:** Contains the server-side code for handling client connections, messages, and online status management.
  
- **chatclient.py:** Contains the client-side code for connecting to the server, sending/receiving messages, and interacting with other clients.
  
- **README.md:** Contains detailed information about the project, how to set it up, and how to use it. It also provides an overview of the message formats and control commands.

Feel free to explore the code, contribute to the project, and provide feedback. Happy chatting! 🎉
