import time

for percent in range(100):
    s = f"[{(percent // 1) * '|'}"
    s += f"{(100 - (percent // 1)) * '.'}] "
    s += f"{percent}"
    print(s, end="\r")
    time.sleep(0.1)