import socket
import time
import socket_library as sl

def main():
    print("Initializing...")
    s = sl.client()
    while s.establish_client_connection():
        reconnect_time = 3
        print("Error: Failed to establish client")
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)

    s.send_string("client is ready")
    s.close()
    return 0

if __name__ == "__main__":
    main()
