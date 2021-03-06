import curses
# 初期化
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)

# 終了処理せずに終了するとターミナルの表示が壊れる！
raise Exception()
stdscr.clear()
stdscr.addstr(0, 0, 'Hello curses !!')
stdscr.refresh()
stdscr.getkey()

# 終了処理
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
