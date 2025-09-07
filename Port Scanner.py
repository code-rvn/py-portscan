import socket

target = input("Enter the target IP or hostname: ")

start_port = 20
end_port = 1024

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")

for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break
    except socket.gaierror:
        print("Hostname could not be resolved.")
        break
    except socket.error:
        print("Could not connect to server.")
        break
