#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pusheen-sl

COPYRIGHT (c) 2016 tryton-vanmeer

GNU GENERAL PUBLIC LICENSE
   Version 3, 29 June 2007

pusheen-sl is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pusheen-sl is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "tryton-vanmeer"
__copyright__ = "Copyright 2016, Tryton Van Meer"
__credits__ = ["tryton-vanmeer"]
__license__ = "GPLv3"


from time import sleep
import curses


PUSHEEN_LINES = """
   ▐▀▄       ▄▀▌   ▄▄▄▄▄▄▄
   ▌  ▀▄▄▄▄▄▀  ▐▄▀▀ ██ ██ ▀▀▄
  ▐    ▀ ▀ ▀                 ▀▄
  ▌               ▄            ▀▄
▀█   █   █   █   ▀               ▌
▀▌      ▀ ▀      ▀▀              ▐   ▄▄
▐                                 ▌▄█ █
▐                                 █ █▀
▐                                 █▀
▐                                 ▌
 ▌                               ▐
 ▐                               ▌
  ▌                             ▐
  ▐▄                           ▄▌
""".splitlines()

PUSHEEN_MAX = 39

PUSHEEN_FEET = """
    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀
    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀
    ▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
    ▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀
    ▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀
    ▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
    ▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀▀
""".splitlines()

FEET_POS_LEN = len(PUSHEEN_FEET)-1
FEET_POS = 0



def main(win):
    # INIT

    # Set curse options
    curses.curs_set(0) # Invisible cursor

    # Get maximum x and y boundries
    MAX_Y, MAX_X = win.getmaxyx()

    # Bit for determing feet pos
    FEET_POS = True


    # START DRAWING FRAMES
    try:
        while True:
            # Print Pusheen from offscreen and move it
            # across the window left-to-right
            for x in range(MAX_X):
                # Clear the window before printing new frame
                win.erase()

                # Print each line of Pusheen
                for y, line in enumerate(PUSHEEN_LINES):
                    win.addstr(y, MAX_X-x-1, line[:x])

                # Print the feet and cycle feet frame
                win.addstr(len(PUSHEEN_LINES), MAX_X-x-1, PUSHEEN_FEET[FEET_POS][:x])
                FEET_POS += 1
                if (FEET_POS == FEET_POS_LEN):
                    FEET_POS = 0

                #refresh the window and sleep
                win.refresh()
                sleep(0.04)


            # Fade Pusheen offscreen past the left edge
            for l in range(PUSHEEN_MAX):
                # Clear the window before printing new frame
                win.erase()

                # Print each line of Pusheen
                for y, line in enumerate(PUSHEEN_LINES):
                    win.addstr(y, 0, line[l:])

                # Print the feet and cycle feet frame
                win.addstr(len(PUSHEEN_LINES), 0, PUSHEEN_FEET[FEET_POS][l:])
                FEET_POS += 1
                if (FEET_POS == FEET_POS_LEN):
                    FEET_POS = 0

                #refresh the window and sleep
                win.refresh()
                sleep(0.04)


    except KeyboardInterrupt:
        return 1
    except curses.error:
        return 0


if __name__ == '__main__':
    curses.wrapper(main)
