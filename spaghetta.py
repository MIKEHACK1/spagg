import os
import time

# Funzione per pulire il terminale
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Funzione per generare il testo della sfera
def generate_sphere_text():
    sphere_text = []
    radius = 10
    for y in range(-radius, radius + 1):
        line = ''
        for x in range(-radius, radius + 1):
            distance = (x ** 2 + y ** 2) ** 0.5
            if distance <= radius:
                line += 'O'
            else:
                line += ' '
        sphere_text.append(line)
    return sphere_text

# Funzione per stampare il testo della sfera
def print_sphere_text(sphere_text, offset):
    clear_terminal()
    for line in sphere_text:
        print(' ' * offset + line)

# Funzione per eseguire il loop del movimento della sfera
def sphere_bounce_loop():
    sphere_text = generate_sphere_text()
    max_offset = os.get_terminal_size().columns - len(sphere_text[0])
    direction = 1
    offset = 0

    while True:
        print_sphere_text(sphere_text, offset)
        offset += direction
        if offset >= max_offset or offset <= 0:
            direction *= -1
        time.sleep(0.05)

# Esegui il loop del movimento della sfera
sphere_bounce_loop()
