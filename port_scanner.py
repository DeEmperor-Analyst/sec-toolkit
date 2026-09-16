import socket
from colorama import Fore, Style, init
init()

def scan_port(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((host, port))
        s.close()
        return True
    except:
        return False

if __name__ == "__main__":
    print(f"{Fore.CYAN}=== Port Scanner ==={Style.RESET_ALL}")
    target = input("Enter website or IP: ")
    print(f"Scanning {target}...")
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 443, 3306]
    
    for port in common_ports:
        if scan_port(target, port):
            print(f"{Fore.GREEN}[+] Port {port} is OPEN{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}[-] Port {port} is CLOSED{Style.RESET_ALL}")