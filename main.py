from asciimatics.screen import Screen
import signal
import sys

from game import Game

def signalHandler():
    sys.exit(0)

def main(screen):
    signal.signal(signal.SIGINT, signalHandler)
    game = Game()
    game.play(screen)

if __name__ == "__main__":
    Screen.wrapper(main, unicode_aware=True)
