import time
import random
import sys

spinner = ['|', '/', '-', '\\']
colors = [
    'Red 🔴',
    'Blue 🔵',
    'Green 🟢',
    'Yellow 🟡',
    'Purple 🟣',
    'Pink 🌸',
    'Orange 🟠',
    'Brown 🟤',
    'Black ⚫',
    'White ⚪',
    'Cyan 🧊',
    'Magenta 💖',
    'Lime 💚',
    'Turquoise 🦚',
    'Gold 🪙',
    'Silver 🪞',
    'Maroon 🧣',
    'Navy 🛳️',
    'Beige 🏜️',
    'Olive 🫒'
]

print("Welcome to the Color Spinner Game!")
input("Press Enter to spin and get a color...")

for _ in range(12):
    for symbol in spinner:
        sys.stdout.write('\rSpinning... ' + symbol)
        sys.stdout.flush()
        time.sleep(0.1)

chosen_color = random.choice(colors)
print(f"\n🌈 You got: {chosen_color}")
