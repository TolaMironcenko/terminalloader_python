# TERMINAL_LOADER_ON_PYTHON

from loader import Loader

### code:
```python
loader = Loader()
print(loader)
```

### result:
	|████████████████████████████████████████████████████████████████████████████████████████████████████| 100%

### code:
```python
loader = Loader(n=10, start='(', end=')', interval=0.1, color='white', symbol='*')
print(loader)
```

### result:
	(**********) 10%

### code:
```python
loader = Loader(n=50, start='[', end=']', interval=0.2, color='black', symbol='#')
print(loader)
```

### result:
	[##################################################] 50%

### code:
```python
loader = Loader(n=50, start='[', end=']', interval=0.2, color='black', symbol='#', display='of')
print(loader)
```

### result:
	[##################################################] 50/50

### code:
```python
loader = Loader(n=100, start='{', end='}', interval=0.03, color='blue', symbol='@', step=3, defsymbol='-')
print(loader)
```

### result:
	{@@@@@@@@@@@@@@@@@@@@@@@@@@-------} 78%

### colors:
	- grey
	- red
	- green
	- yellow
	- blue
	- magenta
	- cyan
	- white