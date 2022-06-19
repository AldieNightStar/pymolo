# Pymolo
### Powered by Curses

---

# Sample
```python
from pymolo import *

# Avoid constructor writing
from dataclasses import dataclass as data

@data
class Player:
	x: int
	y: int

p = Player(5, 5)

@game
def play():
	gprint(p.x, p.y, "@")
	k = key()
	if k == 'a': p.x -= 1
	elif k == 'd': p.x += 1
	elif k == 'w': p.y -= 1
	elif k == 's': p.y += 1
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

# Colors
WHITE, RED, GREEN, BLUE
YELLOW, MAGENTA, CYAN
```