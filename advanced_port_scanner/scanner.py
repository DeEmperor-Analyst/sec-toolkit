# DeEmperor Analyst - Advanced Port Scanner - Day 7
import socket
from concurrent.futures import ThreadPoolExecutor

print("=== DeEmperor Advanced Port Scanner ===")
target = input("Enter target (e.g. 127.0.0.1): ") or "127.0.0.1"
ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
open_ports = []

def scan(p):
    try:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect((target, p))
        print(f"[+] Port {p} OPEN")
        open_ports.append(p)
        s.close()
    except: pass

with ThreadPoolExecutor(max_workers=100) as ex:
    ex.map(scan, ports)

print(f"\nScan done for {target} | Found: {open_ports}")
print("Built by DeEmperor-Analyst | Day 7 - 70%")