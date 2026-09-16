import re
import hashlib
from getpass import getpass
from datetime import datetime

print("="*60)
print("SEC-TOOLKIT [Tool 3/10] - Password Strength Auditor")
print(" By DeEmperor-Analyst")
print("="*60)

def check_strength(password):
    score = 0
    feedback = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: feedback.append("Too short! Use 12+ chars")
    if re.search(r"[A-Z]", password): score += 1
    else: feedback.append("Add UPPERCASE letters")
    if re.search(r"[a-z]", password): score += 1
    else: feedback.append("Add lowercase letters")
    if re.search(r"[0-9]", password): score += 1
    else: feedback.append("Add numbers")
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 2
    else: feedback.append("Add special characters !@#$%")
    common = ["password", "123456", "qwerty", "admin", "letmein", "welcome"]
    if password.lower() in common:
        score = 0
        feedback.append("This is a TOP 10 hacked password!")
    return score, feedback

def hash_password(password):
    md5 = hashlib.md5(password.encode()).hexdigest()
    sha1 = hashlib.sha1(password.encode()).hexdigest()
    sha256 = hashlib.sha256(password.encode()).hexdigest()
    return md5, sha1, sha256

print("\nEnter password to audit:")
try:
    pwd = getpass("Password: ")
except:
    pwd = input("Password: ")

if not pwd:
    pwd = "Password123"

score, feedback = check_strength(pwd)
md5, sha1, sha256 = hash_password(pwd)

print("\n" + "-"*60)
print(f"STRENGTH SCORE: {score}/7")

if score <= 2:
    print("WEAK - Can be cracked in < 1 second!")
elif score <= 4:
    print("MEDIUM - Can be cracked in hours")
else:
    print("STRONG - Would take 100+ years to crack!")

if feedback:
    print("\nHow to improve:")
    for f in feedback:
        print(f" - {f}")

print("\n" + "-"*60)
print("Hashes (How hackers store it):")
print(f"MD5    : {md5}")
print(f"SHA1   : {sha1}")
print(f"SHA256 : {sha256[:32]}...")

print("\n" + "="*60)
print(f"Audit done at {datetime.now().strftime('%H:%M:%S')}")