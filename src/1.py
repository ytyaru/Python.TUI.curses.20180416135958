import curses
def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, 'Hello curses !!')
    stdscr.addstr(1, 0, 'Next Line.')
    stdscr.addstr(2, 4, 'Indent.')
    stdscr.refresh()
    stdscr.getkey()
curses.wrapper(main)
