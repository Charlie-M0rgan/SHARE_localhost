import socket
import qrcode
import os
import subprocess

port = int(input("Enter the port: "))
host= "127.0.0.1"

def is_port_open(host, port):
    """
    Check if a specific port is open on the given host.
    Returns: True if port is open, False otherwise
    """
    # Create a TCP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # Set connection timeout to 1 second
    
    try:
        # Attempt to connect to the port
        sock.connect((host, port))
        sock.close()
        return True
    except Exception:
        # Connection failed, port is closed or unreachable
        return False

def get_local_ip():
    """
    """
    try:
        # Connect to an external server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # Google DNS server
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        # Fallback method if the first approach fails
        return socket.gethostbyname(socket.gethostname())

def create_qr(text, file_name="qrcode.png"):
    """
    """
    qr = qrcode.make(text)
    qr.save(file_name)
    print(f"The QR code saved to {file_name} successfully!")


def run_npm_dev(project_path: str):
    if not os.path.isdir(project_path):
        raise ValueError(f"'{project_path}' is not a valid directory")

    try:
        subprocess.run(
            ["npm.cmd", "run", "dev", "--", "--host"],
            cwd=project_path,
            check=True
        )
    except FileNotFoundError:
        raise RuntimeError("npm not found. Make sure Node.js and npm are installed.")

print(run_npm_dev("YOUr/PATH/HERE"))
link = (f"http://{get_local_ip()}:{port}")
print(link)
create_qr(link)