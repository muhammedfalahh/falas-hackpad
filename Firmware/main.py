import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros

keyboard = KMKKeyboard()
keyboard.modules.append(Macros())

PINS = [
    board.D0,
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
    ]
]

if __name__ == "__main__":
    keyboard.go()