import socket

def banner_grab(ip, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((ip, port))
        s.send(b'HEAD / HTTP/1.0\r\n\r\n')
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner
    except:
        return "No banner"

print("=== SEC-TOOLKIT Tool 07 - Advanced Port Scanner ===")
target = input("Enter target IP (e.g., 8.8.8.8): ").strip()
ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 443, 445, 3306, 3389, 8080]

print(f"\nScanning {target}...\n")
for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((target, port))
    if result == 0:
        banner = banner_grab(target, port)
        print(f"[+] Port {port} OPEN - {banner[:80]}")
    sock.close()

print("\n> Scan Complete.")