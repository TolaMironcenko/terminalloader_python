from termcolor import cprint
import time


class Loader:
	def __init__(self, n: int = 100, start: str = '|', end: str = '|', interval: float = 0.1, color: str = 'green', symbol: str = '█'):
		self.n = n
		self.start = start
		self.end = end
		self.interval = interval
		self.color = color
		self.symbol = symbol

	def __str__(self):
		for percent in range(self.n+1):
			s = self.start+f"{(percent // 1) * self.symbol}"
			s += f"{(self.n - (percent // 1)) * '.'}" + self.end + ' '
			s += f"{percent}"
			cprint(s, self.color, end="\r")
			time.sleep(self.interval)
		return s