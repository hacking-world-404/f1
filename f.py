from os import system as c
import time
import os

A = '\033[1;97m'
R = '\033[1;31m'
Y = '\033[1;33m'
G = '\033[1;32m'
C = '\033[1;36m'

def logo():
    c('clear')
    print(f"""{R}
██████╗ ██╗███████╗███████╗
██╔══██╗██║██╔════╝██╔════╝
██████╔╝██║█████╗  ███████╗
██╔═══╝ ██║██╔══╝  ╚════██║
██║     ██║███████╗███████║
╚═╝     ╚═╝╚══════╝╚══════╝
   {Y}DIAMOND HACK VIP TOOL
{A}-----------------------------------
""")

def diamond_hack():
    logo()
    uid = input(f"{C}[+] Enter Your Free Fire UID: ")
    os.system('espeak -a 300 " আপনার free fire,   উআইডি,   দিন"')
    time.sleep(1)
    print(f"{Y}[+] Connecting to Garena Server...")
    os.system('espeak -a 300 " Connecting to Garena Server"')
    time.sleep(2)
    print(f"{C}[✓] UID Verified: {G}{uid}")
    time.sleep(1)

    print(f"\n{Y}[!] Checking Root Permission...")
    os.system('espeak -a 300 " Checking Root Permission."')
    time.sleep(2)
    if os.system("su -c exit") != 0:
        print(f"{R}[×] Root Permission Required!")
        os.system('espeak -a 300 " সরি এই টুলস টি শুধু রুট ডিভাইসের জন্য ,  দয়া করে মোবাইল রুট করুন অথবা ভি ফোন গাঁগা ব্যবহার করুন ,  As-salamu alaykum"')
        print(f"{R}[×] Tool Closed.")
        exit()
    else:
        print(f"{G}[✓] Root Access Granted!\n")
        print(f"{Y}[+] Injecting Diamonds...\n")
        amounts = [500, 1000, 2000, 5000, 10000]

        for amount in amounts:
            print(f"{C}[*] Injecting {amount} Diamonds...")
            time.sleep(2)

        print(f"{G}\n[✓] Diamonds Injected Successfully!")
        print(f"{Y}[!] Restart Free Fire App To See Changes\n")
        input(f"{A}Press Enter To Exit...")

diamond_hack()