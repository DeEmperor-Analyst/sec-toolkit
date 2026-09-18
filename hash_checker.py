import hashlib
import os

print("=== FILE HASH CHECKER ===")

file_path = input("Enter file path to check: ").strip().replace('"', '')

if not os.path.isfile(file_path):
    print(f"File not found: {file_path}")
    input("Press Enter to close...")
    exit()

print("\nCalculating hashes...")

with open(file_path, "rb") as f:
    data = f.read()
    md5 = hashlib.md5(data).hexdigest()
    sha1 = hashlib.sha1(data).hexdigest()
    sha256 = hashlib.sha256(data).hexdigest()

print(f"\nFile: {os.path.basename(file_path)}")
print(f"MD5:    {md5}")
print(f"SHA1:   {sha1}")
print(f"SHA256: {sha256}")

print("\nYou can use these hashes to check on VirusTotal.")
input("\nPress Enter to close...")