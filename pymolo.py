import curses
import inspect

screen = None

WHITE = 1
RED = 2
GREEN = 3
BLUE = 4
YELLOW = 5
MAGENTA = 6
CYAN = 7

world = None

def init():
	global screen
	global world
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
	world = World()

def gprint(x, y, text, color=WHITE):
	try: screen.addstr(y,x, text, curses.color_pair(color))
	except: pass

def key(): return screen.getkey()

class GameEndExc(Exception): pass

def end(): raise GameEndExc()

def isSqr(x1, y1, w1, h1, x2, y2, w2, h2):
	if x1+w1 < x2: return False
	if y1+h1 < y2: return False
	if x1 > x2+w2: return False
	if y1 > y2+h2: return False
	return True

class Signal:
	def __init__(self):
		self.funcs = []
	def connect(self, func):
		self.funcs.append(func)
		return func
	def emit(self, *data):
		for f in self.funcs:
			f(*data)
	def disconnect(self, func):
		self.funcs.remove(func)

def game(f):
	if screen == None: init()
	while True:
		screen.clear()
		try:
			f()
		except GameEndExc:
			break
		screen.refresh()