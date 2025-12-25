import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()

# macros support (might use later)
keyboard.modules.append(Macros())

# pins used on the PCB (change if needed)
PINS = [
    board.D1,
    board.D2,
    board.D3,
    board.D4,
]

# direct pin setup (no matrix)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# simple test keymap
keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
    ]
]

if __name__ == "__main__":
    keyboard.go()
