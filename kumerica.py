import time
import random
import os

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
RESET = "\033[0m"

def loading(text):
    print(YELLOW + text + RESET)
    for i in range(0, 101, 10):
        bar = "█" * (i//10) + "-" * (10 - i//10)
        print(f"\r{RED}|{bar}| {i}%{RESET}", end="")
        time.sleep(0.1)
    print("\n")

os.system('clear')
print(RED + r"""
 _  __ _   _ __  __ _____ ____  ___ ____    _    
| |/ /| | | |  \/  | ____|  _ \|_ _/ ___|  / \   
| ' / | | | | |\/| |  _| | |_) || | |     / _ \  
| . \ | |_| | |  | | |___|  _ < | | |___ / ___ \ 
|_|\_\ \___/|_|  |_|_____|_| \_\___\____/_/   \_\
                                                 
""" + RESET)
print(MAGENTA + ">>> KUMERICA OS v10 - BY GUNSHOT THE LEGEND <<<" + RESET)
print(GREEN + "KUMERICANS TO THE WHOLE WIASE!!!" + RESET)
print("")

code = input(CYAN + "Enter Kumerican Code: " + RESET)
if code != "kumerica":
    print(RED + "WRONG CODE! You be spy!" + RESET)
    exit()
loading("ACCESS GRANTED! Loading KUMERICA OS...")

while True:
    print(CYAN + "\n========== KUMERICA MAIN MENU ==========" + RESET)
    print("1. 🛡️  Scan Kumerica (Secure Check)")
    print("2. 🔑  Generate Kumerican Password")
    print("3. 💣  WhatsApp Bomber Prank")
    print("4. 📶  Wifi Scanner (Kumasi)")
    print("5. 📢  Kumerica Anthem")
    print("6. 🚪  Exit")
    print(CYAN + "=========================================" + RESET)
    
    choice = input(YELLOW + "Gunshot, choose 1-6: " + RESET)

    if choice == "1":
        loading("Scanning Kumerica Kingdom...")
        print(GREEN + "[OK] Kumasi - Secure - King dey" + RESET)
        print(GREEN + "[OK] Accra - Secure" + RESET)
        print(GREEN + "[OK] Takoradi - Secure" + RESET)
        print(GREEN + "[OK] Whole Wiase - KUMERICA DEY CONTROL!" + RESET)

    elif choice == "2":
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$"
        pw = "".join(random.choice(chars) for _ in range(8))
        print(GREEN + f"Your Kumerican Password: {pw}" + RESET)

    elif choice == "3":
        target = input(CYAN + "Friend name to prank: " + RESET)
        num = input(CYAN + "How many: " + RESET)
        print(RED + f"Bombing {target} with {num} messages..." + RESET)
        loading("Hacking WhatsApp")
        for i in range(5):
            print(GREEN + f"[SENT {i+1}/{num}] to {target}: You hacked by Gunshot!" + RESET)
            time.sleep(0.2)
        print(YELLOW + f"BOOM! {num} SENT TO {target}! FAKE PRANK 😂" + RESET)

    elif choice == "4":
        loading("Scanning Wifi around Kumasi...")
        wifis = ["Kumerica_Free_Wifi - Strong", "MTN_5G_Kumasi - Strong", "Gunshot_Hacker_Wifi - ULTRA", "Vodafone_Gh - Medium", "Gee_Wifi - Weak (Hacked)"]
        for w in wifis:
            print(GREEN + f"[FOUND] {w}" + RESET)
            time.sleep(0.3)

    elif choice == "5":
        print(MAGENTA + "\n🎵 KUMERICA! KUMERICA! TO THE WHOLE WIASE! 🎵" + RESET)
        print(MAGENTA + "🎵 WE ARE THE KINGS! KUMASI TO THE WORLD! 🎵\n" + RESET)

    elif choice == "6":
        print(YELLOW + "Exiting KUMERICA OS... Kumerica forever! 💛🖤💚" + RESET)
        break
    else:
        print(RED + "Wrong number! Choose 1-6!" + RESET)
