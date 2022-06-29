import time
from tqdm import tqdm
from progress.bar import IncrementalBar
from termcolor import cprint
from loader import Loader


def main():
    # without libraries
    for percent in range(100):
        s = f"|{(percent // 1) * '█'}"
        s += f"{(100 - (percent // 1)) * '.'}| "
        s += f"{percent}"
        cprint(s, 'green', end="\r")
        time.sleep(0.01)

    # with library tqdm
    for i in tqdm(range(10)):
        time.sleep(0.1)

    # with library progress
    mylist = range(100)

    bar = IncrementalBar('Countdown', max = len(mylist))

    for item in mylist:
        bar.next()
        time.sleep(0.01)

    bar.finish()

    #with Loader
    loader = Loader(n=100, start='{', end='}', interval=0.03, color='blue', symbol='@', step=3, defsymbol='-')
    print(loader)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        cprint('exited', 'green')
        exit()
    except Exception as e:
        cprint('Error: '+str(e), 'red')