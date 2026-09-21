import socket

with open("wordlist.txt", "r") as f:
    words = [line.strip() for line in f]

domain = input("Enter domain (e.g. google.com): ")
print(f"\nScanning {domain} with {len(words)} words...\n")

for word in words:
    sub = f"{word}.{domain}"
    try:
        ip = socket.gethostbyname(sub)
        print(f"[FOUND] {sub} -> {ip}")
    except:
        pass

print("\nDone!")