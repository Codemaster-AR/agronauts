import time
import os
from cinetext import cinetext_rainbow, cinetext_clear, cinetext_glitch, cinetext_pulse, cinetext_type
from colorama import Fore, Back, Style, init, deinit
import playsound3
import ez_background_music
from KeyboardGate import KeyboardGate
def wait (seconds):
    time.sleep(seconds)


def clear():
    # 'nt' means Windows, 'posix' covers Mac and Linux
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def show_logo():
    gate = KeyboardGate()
    gate.KeyboardGateDisable()
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Compact version: Fits standard terminal widths
    logo = r"""
  ___                 _   _             _       
 / _ \ __ _ _ __ ___ | \ | | __ _ _   _| |_ ___ 
/ /_\ / _` | '__/ _ \|  \| |/ _` | | | | __/ __|
/ /_\\ (_| | | | (_) | |\  | (_| | |_| | |_\__ \
\____/\__, |_|  \___/|_| \_|\__,_|\__,_|\__|___/ CLI
      |___/                                     
    """
    cinetext_type(logo, 0.005)
    time.sleep(0.25)
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if os.name == 'nt' else 'clear')
    cinetext_rainbow(logo, 75, 0.075)
    os.system('cls' if os.name == 'nt' else 'clear')
    cinetext_pulse(logo, 2, 0.05)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{Fore.GREEN}{logo}{Style.RESET_ALL}")
    cinetext_type ("v1.0.0 - AgroNauts Command Line Interface", 0.005)
    cinetext_type ("Type 'commands' to see a list of available commands.", 0.005)




clear()
wait(1)
show_logo()
loop = 1
while loop == 1:
    user_input = str(input("AgroNauts - Command: "))
    print ("Commands:")
    print ("setup    -    Setup your hardware and software (guide)")
    if user_input == "clear":
        clear()
    elif user_input in ["commands", "command", "option", "options"]:
        text = (f"{Style.BRIGHT}Commands: {Style.RESET_ALL}")
        cinetext_type(text, 0.04)
    elif user_input == "setup":
        print ("Setup: ")
