import curses

screen = None

WHITE = 1
RED = 2
GREEN = 3
BLUE = 4
YELLOW = 5
MAGENTA = 6
CYAN = 7

def init():
	global screen
	screen = curses.initscr()
	curses.noecho()
	curses.start_color()

	curses.init_pair(WHITE, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(YELLOW, curses.COLOR_YELLOW, curses.COLOR_BLACK)
	curses.init_pair(MAGENTA, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(CYAN, curses.COLOR_CYAN, curses.COLOR_BLACK)

def gprint(x, y, text, color=WHITE):
	try: screen.addstr(y,x, text, curses.color_pair(color))
	except: pass

def key(): return screen.getkey()

class GameEndExc(Exception): pass

def end(): raise GameEndExc()

def game(f):
	if screen == None: init()
	while True:
		screen.clear()
		try:
			f()
		except GameEndExc:
			break
		screen.refresh()