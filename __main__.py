import multiprocessing
import sys
from enum import Enum
from time import sleep

import pyautogui

from nosleep.systray import systray_icon


class WakeupMode(Enum):
    MOUSE = 1
    BUTTON = 2


WAKEUP_IN_SECONDS = 10


if __name__ == "__main__":
    icon = systray_icon()
    loop = True
    p = multiprocessing.Process(target=icon.run)
    p.start()

    print("Insert wake up mode - Mouse (1) / Button (2)")
    # mode = int(input("Wake up mode: "))
    mode = 2
    if mode == WakeupMode.MOUSE.value:
        print(f"Mouse movement every {WAKEUP_IN_SECONDS} seconds")
    elif mode == WakeupMode.BUTTON.value:
        print(f"Click shift keyboard every {WAKEUP_IN_SECONDS} seconds")

    while loop:
        try:
            if mode == WakeupMode.MOUSE.value:
                pyautogui.move(0, 1)
                pyautogui.move(0, -1)
            elif mode == WakeupMode.BUTTON.value:
                pyautogui.press("shift")
            else:
                sys.exit(1)
            sleep(WAKEUP_IN_SECONDS)
        except KeyboardInterrupt:
            print("Exit")
            p.terminate()
            loop = False
            sys.exit(1)
    sys.exit(1)
