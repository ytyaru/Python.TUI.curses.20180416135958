import os, curses
def main(stdscr):
    if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
    stdscr.clear()
    curses.start_color()
    curses.use_default_colors()
    for i in range(0, curses.COLORS):
        curses.init_pair(i + 1, i, -1)
    try:
        for i in range(0, 255):
            stdscr.addstr(str(i), curses.color_pair(i))
    except curses.ERR: pass
    stdscr.refresh()
    stdscr.getkey()

os.environ['TERM'] = 'xterm-256color'
curses.wrapper(main)
