import socket
import json
import base64

# Server setup
host = "0.0.0.0"
port = 2021
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            data = b""
            while True:
                chunk = conn.recv(1024)
                if not chunk:
                    break
                data += chunk
    
            # Parse the JSON data
            try:
                received_data = json.loads(data.decode())
                if received_data["type"] == "blockchain_file":
                    filename = received_data["filename"]
                    file_data = received_data["file_data"]
                    # Now you can save 'file_data' to a file with the given 'filename'
                    with open(filename, "wb") as f:
                        f.write(base64.b64decode(file_data.encode()))
                    print(f"Received and saved file: {filename}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
