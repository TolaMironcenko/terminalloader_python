# TERMINAL_LOADER_ON_PYTHON

from loader import Loader

### code:
loader = Loader(n=10, start='(', end=')', interval=0.1, color='white', symbol='*')\n
print(loader)

### result:
	(**********) 10

### code:
loader = Loader(n=50, start='[', end=']', interval=0.2, color='black', symbol='#')\n
print(loader)

### result:
	[##################################################] 50