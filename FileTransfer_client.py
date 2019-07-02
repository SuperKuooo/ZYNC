import socket
import time
import os
import socket_library as sl


def main():
    print("Running client...")
    s = sl.client()
    while s.establish_client_connection():
        reconnect_time = 3
        print("Error: Failed to establish client")
        print("Retrying in " + str(reconnect_time) + " seconds...")
        time.sleep(reconnect_time)

    # s.send_string("client is ready")
    # s.send_image(os.path.join(os.getcwd(), "image.jpg"))

    s.send_zip(os.path.join.(getcwd(), "ship.tgz"), True)
    s.close()
    return 0


if __name__ == "__main__":
    main()
