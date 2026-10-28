import time
import random

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

print(RED + r"""
 ____   ___  __  __ ____  _____ ____  
| __ ) / _ \|  \/  | __ )| ____|  _ \ 
|  _ \| | | | |\/| |  _ \|  _| | |_) |
| |_) | |_| | |  | | |_) | |___|  _ < 
|____/ \___/|_|  |_|____/|_____|_| \_\
                                      
""" + RESET)

print(YELLOW + ">>> KUMERICAN WHATSAPP BOMBER v1 - PRANK MODE <<<" + RESET)
print(GREEN + "Note: This is FAKE prank! No real message sent! For fun only!" + RESET)
print("")

# Get friend name
target = input(CYAN + "Enter friend name to prank: " + RESET)
count = input(CYAN + "How many messages to bomb? (e.g 100): " + RESET)

print("")
print(YELLOW + f"Initializing attack on {target}..." + RESET)
time.sleep(1)

# Fake loading
for i in range(0, 101, 5):
    bar = "█" * (i//5) + "-" * (20 - i//5)
    print(f"\r{RED}Bombing {target} |{bar}| {i}%{RESET}", end="")
    time.sleep(0.15)
print("")

print("")
print(GREEN + "Connecting to WhatsApp servers..." + RESET)
time.sleep(1)
print(GREEN + "Bypassing encryption..." + RESET)
time.sleep(0.8)
print(GREEN + "Injecting messages..." + RESET)
time.sleep(0.8)

# Fake messages
messages = [
    f"KUMERICA TO THE WHOLE WIASE! - from Gunshot",
    f"You have been hacked by GUNSHOT!",
    f"{target} you dey owe me money!",
    f"Kumericans are taking over your phone!",
    "Pay $100 or your phone go explode! (joke)",
]

print("")
print(CYAN + f"--- Sending {count} messages to {target} ---" + RESET)
for j in range(5):
    msg = random.choice(messages)
    print(f"{GREEN}[SENT {j+1}/{count}] to {target}: {msg}{RESET}")
    time.sleep(0.3)

print("")
print(RED + "="*40 + RESET)
print(YELLOW + f"BOOM! {count} MESSAGES SENT TO {target}! 💣💥" + RESET)
print(RED + "="*40 + RESET)
print("")
print(CYAN + "Hahaha! E be prank! No message really sent! 😂" + RESET)
print(GREEN + "Show this screen to your friend make he fear! KUMERICA!" + RESET)
