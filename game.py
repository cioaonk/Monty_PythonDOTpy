from asciimatics.event import KeyboardEvent
import input
import sys
import modes

class Game:
    def __init__(self):
        pass

    def loop(self, screen):
        mode = modes.MainMenu(screen)

        while True:
            input.update()
            event = screen.get_event()
            key = event.key_code if isinstance(event, KeyboardEvent) else None
            if key in ((ord('Q'), ord('q'))):
                sys.exit(0)
            mode.run()
            screen.refresh()
