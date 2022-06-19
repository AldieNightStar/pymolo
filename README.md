# Pymolo
### Powered by Curses

---

# Sample
```python
from pymolo import *
from dataclasses import dataclass as data # Just to not write '__init__(self)' all the time

@data
class Player:
	x: int
	y: int

# Create world
world = World()

# Add couple of elements
world.append(...)
world.append(...)
world.append(...)

# Create player
p = Player(5, 5)

# Run the game
@game
def play():
	# Draw the world
	world.draw()
	# Print player's position
	gprint(p.x, p.y, "@")

	# Controls
	k = key()
	if k == 'a': p.x -= 1
	elif k == 'd': p.x += 1
	elif k == 'w': p.y -= 1
	elif k == 's': p.y += 1
	# If user press 'q' game will end
	if k == 'q':
		end()
```

# API
```python
# Start game loop
@game
def game(): pass

# Print text at some pos
# Use it inside game loop
gprint(x, y, text, color)

# Read key string (length: 1)
key()

# Break the loop and end the Game
end()

# Check for square collision between two rectangles
isSqr(x1, y1, w1, h1, x2, y2, w2, h2)

# Colors
WHITE, RED, GREEN, BLUE
YELLOW, MAGENTA, CYAN
```

# Signals (Events)
* Before object will destroy - please disconnect it from any signals to not have _memory leaks_
```python
# New Signal
on_signal = Signal()

# Connect to signal
def some_func(evt):
	print("Event: ", evt)
on_signal.connect(some_func)

# Disconnect from signal
on_signal.disconnect(some_func)

# Connect to signal (with Decorator)
@on_signal.connect
def some_func2(evt):
	print("Event: ", evt)
```