from pymolo import *

on_sig = Signal()
dat = [""]

@game
def start(time):
	rect(5, 5, 50, 20, "#~.-@", time)
	gprint(0, 0, dat[0])
	k = key()
	dat[0] = f"{k} : {type(k)} : {len(k)} : {ord(k)}"
	if k == "q": end()