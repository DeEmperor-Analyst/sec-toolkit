# DeEmperor-Analyst | Sec-Toolkit - Day 8 - Pro Main Menu
import os, socket, sys
from concurrent.futures import ThreadPoolExecutor

def banner():
    print(r"""
 ____ ____ _____ _ _ _ _
| _ \| ___| |_ _|__ ___ | | | _(_) |_
| | | | _| | |/ _ \ / _ \| | |/ / | __|
| |_| | |___ | | (_) | (_) | | <| | |_
|____/|____| |_|\___/ \___/|_|_|\_\_|\__|
    By DeEmperor-Analyst | Day 8 - 80% Done
    GitHub: DeEmperor-Analyst/sec-toolkit
    """)

def port_scanner():
    print("\n=== Advanced Port Scanner ===")
    target = input("Target IP/domain [127.0.0.1]: ") or "127.0.0.1"
    ports = [21,22,23,25,53,80,110,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,8443]
    found = []
    def scan(p):
        try:
            s=socket.socket(); s.settimeout(0.6)
            s.connect((target,p))
            print(f"[+] {p} OPEN"); found.append(p); s.close()
        except: pass
    with ThreadPoolExecutor(max_workers=100) as ex: ex.map(scan, ports)
    print(f"\nDone! {target} -> Open: {found}")

def subdomain_finder():
    print("\n=== Subdomain Finder ===")
    domain = input("Enter domain (e.g. example.com): ") or "example.com"
    try:
        with open("subdomain_finder/wordlist.txt") as f:
            words=[w.strip() for w in f if w.strip()]
    except:
        words=["www","mail","ftp","admin","api","dev","test","blog"]
    print(f"Checking {len(words)} words for {domain}...")
    for w in words:
        sub=f"{w}.{domain}"
        try:
            socket.gethostbyname(sub)
            print(f"[+] Found: {sub}")
        except: pass

banner()
while True:
    print("\n[1] Advanced Port Scanner\n[2] Subdomain Finder\n[3] Exit")
    c=input("DeEmperor > ")
    if c=="1": port_scanner()
    elif c=="2": subdomain_finder()
    elif c=="3": print("Bye DeEmperor! 👑"); break
    else: print("Invalid, choose 1-3")