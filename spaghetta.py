import colorama
from colorama import Fore, Back, Style
import time

colorama.init(autoreset=True)

# Funzione per stampare la ciotola e gli spagetti
def print_bowl():
    bowl = '''
           \\   /
            .-.
           |o o|
           |   |
           |   |
           -----
          '''
    print(Fore.YELLOW + bowl)
    print()

# Funzione per stampare il testo "MiKeOfficialTM" con colori arcobaleno
def print_rainbow_text(text):
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]
    interval = 0.2  # Intervallo di tempo tra i colori (in secondi)
    rainbow_text = ''

    for char in text:
        for color in colors:
            rainbow_text += color + char
            time.sleep(interval)
    print(rainbow_text)

# Stampa la ciotola e gli spagetti
print_bowl()
print()

# Stampa il testo "MiKeOfficialTM" con colori arcobaleno
text = "MiKeOfficialTM"
print_rainbow_text(text)
