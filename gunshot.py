import time
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def loading(text="Loading"):
    for i in range(0, 101, 20):
        print(f"\r{CYAN}{text}... {i}%{RESET}", end="")
        time.sleep(0.3)
    print("")

print(GREEN + r"""
  ____ _   _ _   _ ____  _   _  ___ _____ 
 / ___| | | | \ | / ___|| | | |/ _ \_   _|
| |  _| | | |  \| \___ \| |_| | | | || |  
| |_| | |_| | |\  |___) |  _  | |_| || |  
 \____|\___/|_| \_|____/|_| |_|\___/ |_|  
""" + RESET)

print(YELLOW + ">>> KUMERICAN HACKER MODE LEVEL 5 <<<" + RESET)

# PASSWORD - Only Kumericans know am
password = input(GREEN + "Enter Kumerican Code: " + RESET)

if password != "kumerica":
    print(RED + "ACCESS DENIED! You no be Kumerican!" + RESET)
    exit()
else:
    print(GREEN + "ACCESS GRANTED!" + RESET)
    loading("Activating Kumerican Power")

print("")
print(CYAN + "Welcome Gunshot! Kumericans to the whole wiase!" + RESET)
print("")

# MENU
while True:
    print(YELLOW + "--- MENU ---" + RESET)
    print("1. Scan Kumerica (Secure Check)")
    print("2. Generate Password")
    print("3. Kumerican Message")
    print("4. Exit")
    
    choice = input(GREEN + "Choose 1-4: " + RESET)

    if choice == "1":
        loading("Scanning Kumerica")
        print(GREEN + "[OK] Kumasi - Secure" + RESET)
        print(GREEN + "[OK] Accra - Secure" + RESET)
        print(GREEN + "[OK] Whole Wiase - Kumerica dey control!" + RESET)
        print("")
    elif choice == "2":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#"
        pw = "".join(random.choice(chars) for _ in range(8))
        print(CYAN + f"Your Kumerican Password: {pw}" + RESET)
        print("")
    elif choice == "3":
        print(RED + "KUMERICANS TO THE WHOLE WIASE!!! 🌍🔥" + RESET)
        print("")
    elif choice == "4":
        print(YELLOW + "Exiting... Kumerica forever!" + RESET)
        break
    else:
        print(RED + "Wrong choice! Try 1-4" + RESET)
