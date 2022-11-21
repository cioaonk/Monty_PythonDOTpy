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
        self.screen.print_at("In MainMenu", 0, 0)
        self.screen.refresh()

        while True:
            key = self.screen.get_key()
            if key in [ord('Q'), ord('q')]:
                sys.exit(0)
