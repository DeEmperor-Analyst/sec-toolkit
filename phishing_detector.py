import re
from urllib.parse import urlparse

def check_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed = urlparse(url)
    domain = parsed.netloc
    full_url = parsed.geturl()
    
    score = 0
    print(f"\n[*] Checking: {full_url}")
    print(f"[*] Domain: {domain}\n")

    if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', domain):
        print("[DANGER] Uses IP address - HIGH RISK")
        score += 3
    if "@" in full_url:
        print("[DANGER] Contains @ symbol - HIGH RISK")
        score += 3
    if len(full_url) > 75:
        print(f"[WARNING] URL too long ({len(full_url)} chars)")
        score += 2
    if parsed.scheme != "https":
        print("[WARNING] Not using HTTPS")
        score += 1
    if domain.count('.') > 3:
        print("[WARNING] Too many dots/subdomains")
        score += 2
    if '-' in domain:
        print("[INFO] Hyphen in domain - can be suspicious")
        score += 1

    print(f"\n--- Risk Score: {score} ---")
    if score >= 5:
        print("VERDICT: LIKELY PHISHING - DO NOT CLICK!")
    elif score >= 3:
        print("VERDICT: SUSPICIOUS - Be careful")
    else:
        print("VERDICT: LOOKS SAFE")

print("=== TOOL 04: Phishing URL Detector ===")
while True:
    link = input("\nEnter URL to scan (or type exit): ").strip()
    if link.lower() == 'exit':
        break
    if link:
        check_url(link)