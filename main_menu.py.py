import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("======================================")
    print("  CYBERSECURITY TOOLKIT - MAIN MENU")
    print("======================================")
    print("1. Port Scanner")
    print("2. Password Strength Checker")
    print("3. Phishing Link Detector")
    print("4. Hash Checker (VirusTotal)")
    print("5. Breach Checker")
    print("0. Exit")
    print("======================================")
    
    choice = input("Choose a tool (0-5): ")

    if choice == "1":
        os.system("python port_scanner.py")
    elif choice == "2":
        os.system("python password_checker.py")
    elif choice == "3":
        os.system("python phishing_detector.py")
    elif choice == "4":
        os.system("python hash_checker.py")
    elif choice == "5":
        os.system("python breach_checker.py")
    elif choice == "0":
        print("Goodbye! Stay secure!")
        break
    else:
        print("Invalid choice!")
    
    input("\nPress ENTER to return to menu...")