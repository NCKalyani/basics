import time
import random

def wait_game():
    target = random.randint(2, 4)
    print(f'we have to wait '
          f'{target} seconds')
    input("press enter to begin")
    start = time.perf_counter()
    input(f"press again after {target} seconds")
    elapsed = time.perf_counter() - start
    print(f'\n Elapsed time:{elapsed}')
    if elapsed == target:
        return 'Wow! You Won....'
    elif elapsed < target:
        return f'you are {target-elapsed:.3f} seconds fast'
    else:
        return f'you are {elapsed-target:.3f} seconds slow'


print(wait_game())
