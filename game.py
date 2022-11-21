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
        modes.TitleScreen(screen).run()
        screen.clear()

        modes.MainMenu(screen).run()
