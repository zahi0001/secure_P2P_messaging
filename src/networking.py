import socket

# Constants
HOST = 'localhost' 
PORT = 12345        

# Bob
def start_bob():
    bob_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bob_socket.bind((HOST, PORT))
    bob_socket.listen(1)
    print(f"Bob started and listening on {HOST}:{PORT}")
    
    conn, addr = bob_socket.accept()
    print(f"Connection established with {addr}")
    return conn

# Alice
def start_alice():
    alice_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    alice_socket.connect((HOST, PORT))
    print(f"Connected to the bob at {HOST}:{PORT}")
    return alice_socket


def send_message(conn, message):
    conn.sendall(message)
    print("Message sent.")


def receive_message(conn):
    data = conn.recv(1024) 
    print("Message received.")
    return data

