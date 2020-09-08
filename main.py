from datetime import datetime
from time import sleep


def print_current_time():
    now = datetime.now()
    print(f"It is {now.strftime('%H:%M:%S')} now.")


if __name__ == "__main__":
    while True:
        print_current_time()
        sleep(1)

