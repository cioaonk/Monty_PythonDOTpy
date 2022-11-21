from asciimatics.event import KeyboardEvent
import sys
import logging

import modes

class Game:
    def __init__(self):
        logging.basicConfig(filename="debug.log", encoding='utf-8', level=logging.DEBUG)
        logging.debug("Starting game...")

    def play(self, screen):
        screen.set_title("MontyPYthon")
        mode = modes.TitleScreen(screen)
        mode.run()
        screen.clear()

        mode = modes.MainMenu(screen)
        mode.run()
