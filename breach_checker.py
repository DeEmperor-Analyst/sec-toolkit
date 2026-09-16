import requests
import hashlib
from colorama import Fore, Style, init
init()

def check_password(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    res = requests.get(url)
    
    hashes = (line.split(':') for line in res.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return int(count)
    return 0

if __name__ == "__main__":
    print(f"{Fore.CYAN}=== Password Breach Checker ==={Style.RESET_ALL}")
    pwd = input("Enter password to check: ")
    count = check_password(pwd)
    if count:
        print(f"{Fore.RED}[!] Found {count} times in data breaches!{Style.RESET_ALL}")
    else:
        print(f"{Fore.GREEN}[+] Safe! Not found in any known breach.{Style.RESET_ALL}")