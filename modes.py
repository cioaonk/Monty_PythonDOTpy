from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText, SpeechBubble
from asciimatics.scene import Scene
import logging
import sys
import curses
import time

from resources.characters import PLAYER as player

ESC = 27
ENTER = 10
QUIT = 113
MOVE_SPEED = 2

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
            if key is not None:
                logging.warn(f"Key {key}, {type(key)}")

            if key in [ord('Q'), ord('q')] or key == ESC:
                sys.exit(0)
            elif key == ENTER:
                return
            elif key in [ord('I'), ord('i')]:
                InfoScreen(self.screen).run()
                return

class InfoScreen:
    def __init__(self, screen):
        self.screen = screen

    def run(self):
        self.screen.clear()
        self.screen.print_at("Info. Press Q to quit or Enter to go back.", 0, 0)
        self.screen.refresh()

        while True:
            key = self.screen.get_key()
            if key is not None:
                logging.warn(f"Key {key}, {type(key)}")

            if key in [ord('Q'), ord('q')] or key == ESC:
                sys.exit(0)
            elif key == ENTER:
                MainMenu(self.screen).run()
                return

class Level1:
    def __init__(self, screen):
        self.screen = screen

        self.player_x = 2
        self.player_y = 12
    
    def run(self):
        curses.initscr()
        win = curses.newwin(int(self.screen.height * 3 / 4), self.screen.width, 0, 0)
        win.keypad(1)
        curses.noecho()
        curses.curs_set(0)
        win.border(0)
        win.nodelay(1)

        while True:
            key = -1
            event = win.getch()
            if event != -1:
                key = event
            else:
                time.sleep(0.1)
                continue

            if key == ESC or key == QUIT:
                sys.exit(0)
            
            elif key == curses.KEY_RIGHT:
                self.player_x += 1 * MOVE_SPEED
            elif key == curses.KEY_LEFT:
                self.player_x += -1 * MOVE_SPEED
            elif key == curses.KEY_UP:
                self.player_y += -1 * MOVE_SPEED
            elif key == curses.KEY_DOWN:
                self.player_y += 1 * MOVE_SPEED

            # check valid before displaying
            self.display(win, player, self.player_x, self.player_y)

            time.sleep(0.1)
            

    def display(self, win, object, x, y):
        win.erase()
        win.border(0)
        for y, line in enumerate(object.splitlines(), y):
            win.addstr(y, x, line)
