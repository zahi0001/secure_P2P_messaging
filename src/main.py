from networking import start_bob, start_client
from gui import setup_gui
import time

def main():
    print("Welcome to Secure P2P Messaging")
    choice = input("Run as Bob (b) or Alice (a): ").lower()


    if choice == 'b':
        print("Starting Bob...")
        connection = start_bob()  
        is_bob = True
    elif choice == 'a':
        print("Starting Alice...")
        time.sleep(1)  # Give the bob time to start
        connection = start_client()  # Start client
        is_bob = False
    else:
        print("Invalid choice. Please restart the program and choose 'b' or 'a'.")
        return

    # Launch the GUI
    setup_gui(connection, is_bob)

if __name__ == "__main__":
    main()
