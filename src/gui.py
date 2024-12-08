import tkinter as tk
from tkinter import scrolledtext
from encryption import generate_key, encrypt_message, decrypt_message
from networking import start_bob, start_alice, send_message, receive_message

# Shared Password (for testing)
SHARED_PASSWORD = "securepassword123"

# GUI Implementation
def setup_gui(connection, is_bob):
    # Generate a key from the shared password
    key = generate_key(SHARED_PASSWORD)

    # Functions for sending and receiving messages
    def send():
        plaintext = message_input.get()
        if plaintext:
            # Encrypt the message
            encrypted_message = encrypt_message(plaintext, key)
            # Send the encrypted message
            send_message(connection, encrypted_message)
            # Display the sent ciphertext
            chat_output.insert(tk.END, f"Sent (Ciphertext): {encrypted_message}\n")
            message_input.delete(0, tk.END)  # Clear the input field

    def receive():
        # Receive an encrypted message
        encrypted_message = receive_message(connection)
        # Decrypt the message
        decrypted_message = decrypt_message(encrypted_message, key)
        # Display the received ciphertext and plaintext
        chat_output.insert(tk.END, f"Received (Ciphertext): {encrypted_message}\n")
        chat_output.insert(tk.END, f"Decrypted: {decrypted_message}\n")

    # Create the main window
    root = tk.Tk()
    root.title("Secure P2P Messaging")

    # Input field for typing messages
    message_input = tk.Entry(root, width=50)
    message_input.pack(pady=5)

    # Send and Receive buttons
    send_button = tk.Button(root, text="Send", command=send)
    send_button.pack(side=tk.LEFT, padx=10)

    receive_button = tk.Button(root, text="Receive", command=receive)
    receive_button.pack(side=tk.LEFT, padx=10)

    # Scrolled text box for displaying chat history
    chat_output = scrolledtext.ScrolledText(root, width=60, height=20, state='normal')
    chat_output.pack(pady=10)

    # Add a label to show the mode (Bob or Alice)
    mode_label = tk.Label(root, text="Running as Bob" if is_bob else "Running as Alice")
    mode_label.pack(pady=5)

    # Run the GUI loop
    root.mainloop()

