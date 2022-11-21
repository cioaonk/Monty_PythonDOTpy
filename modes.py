from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
import logging

import sys
from asciimatics.event import KeyboardEvent
import time

class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
    
    def run(self):
        effects = [
            Cycle(
                self.screen,
                FigletText("MontyPYthon"),
                self.screen.height // 2 - 8
            ),
            Cycle(
                self.screen,
                SpeechBubble("Press space to play"),
                self.screen.height - 3
            ),
            Stars(self.screen, 200)
        ]
        self.screen.play([Scene(effects, 5000)], repeat=False)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        self.screen.clear()
        self.screen.centre("Play (Enter)", self.screen.height - 6)
        self.screen.centre("Info (I)", self.screen.height - 5)
        self.screen.centre("Quit (Q)", self.screen.height - 4)
        self.screen.refresh()

        while True:
            key = self.screen.get_key()
            logging.warn(f"Key {key}, {type(key)}")
            if key in [ord('Q'), ord('q')]:
                sys.exit(0)
            elif key == 10: # enter key
                Level1(self.screen).run()
            elif key in [ord('I'), ord('i')]:
                InfoScreen(self.screen).run()
        
        self.screen.clear()

class InfoScreen:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        self.screen.clear()
        self.screen.print_at("Info. Press Q to quit or Enter to go back.", 0, 0)
        self.screen.refresh()

        while True:
            key = self.screen.get_key()
            logging.warn(f"Key {key}, {type(key)}")
            if key in [ord('Q'), ord('q')]:
                sys.exit(0)
            elif key == 10: # enter key
                MainMenu(self.screen).run()

class Level1:
    def __init__(self, screen):
        self.screen = screen
    
    def run(self):
        self.screen.clear()
        self.screen.print_at("Level1", 0, 0)
        self.screen.refresh()
