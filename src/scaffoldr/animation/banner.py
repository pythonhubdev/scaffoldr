import time
import sys

from scaffoldr.core.constants import ascii_art

# ANSI reset code
reset = "\033[0m"

# Cyan color
cyan = "\033[96m"

# Shine style: bold white
shine_style = "\033[1;97m"


class BannerAnimation:
    def __init__(self):
        # Dimensions
        self.HEIGHT: int = len(ascii_art)
        self.WIDTH: int = len(ascii_art[0])

        # Initialize self.STATE with spaces
        self.STATE: list[list[str]] = [[" "] * self.WIDTH for _ in range(self.HEIGHT)]
        self.is_true: bool = True

    def run(self):
        # Reveal animation: add columns from right to left, inserting at left and pushing right
        for col in range(self.WIDTH - 1, -1, -1):
            for row in range(self.HEIGHT):
                new_char = ascii_art[row][col]
                self.STATE[row].insert(0, new_char)
                self.STATE[row].pop()

            # Move cursor up if not first frame (to overwrite in place)
            if not self.is_true:
                sys.stdout.write(f"\033[{self.HEIGHT}A")
            else:
                self.is_true = False

            # Redraw the current self.STATE
            for row in range(self.HEIGHT):
                for char in self.STATE[row]:
                    sys.stdout.write(cyan + char + reset)
                sys.stdout.write("\n")
            sys.stdout.flush()
            time.sleep(0.02)  # Adjust speed here (slower for more visible flow)

        # Pause after full reveal
        time.sleep(1)

        # Move cursor up to prepare for shine animation (overwrites the static reveal)
        sys.stdout.write(f"\033[{self.HEIGHT}A")

        # Shine animation: sweep a highlight from left to right
        shine_width = 5  # Width of the shine highlight
        shine_speed = 0.02  # Speed of shine movement

        # For shine, use the final ascii_art (or self.STATE, which is now full)
        is_first = True
        for offset in range(self.WIDTH + shine_width):
            if not is_first:
                sys.stdout.write(f"\033[{self.HEIGHT}A")
            else:
                is_first = False

            # Redraw each line with shine applied
            for row in range(self.HEIGHT):
                for j in range(self.WIDTH):
                    char = self.STATE[row][j]
                    if offset - shine_width <= j < offset:
                        # Apply shine style
                        sys.stdout.write(shine_style + char + reset)
                    else:
                        # Cyan color
                        sys.stdout.write(cyan + char + reset)
                sys.stdout.write("\n")
            sys.stdout.flush()
            time.sleep(shine_speed)

        # Move cursor up and redraw without shine for final static
        sys.stdout.write(f"\033[{self.HEIGHT}A")
        for row in range(self.HEIGHT):
            for char in self.STATE[row]:
                sys.stdout.write(cyan + char + reset)
            sys.stdout.write("\n")
        sys.stdout.flush()
