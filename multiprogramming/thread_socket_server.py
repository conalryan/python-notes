#!/usr/bin/env python

import socket
import threading


class ClientHandler(threading.Thread):
    """
        A thread to handle one client request
    """
    
    def __init__(self, client_socket, client_address):
        super(ClientHandler, self).__init__()
        self._client_socket = client_socket
        self._client_address = client_address

    # The function that the thread runs
    def run(self):
        # Read from the client (bytes, not str)
        request = self._client_socket.recv(1024)

        # Create reply to send to client
        reply = request.upper()[::-1]

        # Send the reply to the client
        self._client_socket.sendall(reply)

        # Close the connection
        self._client_socket.close()


def setup():
    """
    Initialize the server socket
    :return:
    """
    # Close the socket
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Set some socket options
    serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # serv.setblocking(0)

    # Bing to local host and port 7777
    serv.bind((socket.gethostname(), 7777))

    # Start listening
    serv.listen(5)
    
    return serv


def main():
    """
    Main program
    :return:
    """
    serv = setup()

    # WARNING:
    # Need to add a counter to control how many threads are being created.
    # Otherwise we could get a Denial of Service Attack.
    #
    # Loop until program is killed
    while True:
        # Sleep until client request arrives
        (csock, addr) = serv.accept()

        # Create new thread to handle client
        handler = ClientHandler(csock, addr)

        # Start the new thread
        handler.start()

       
if __name__ == '__main__':
    main()

