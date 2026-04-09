import time

from poll import poll


def main():
    interval = 30

    while True:
        poll()
        time.sleep(interval)


main()
