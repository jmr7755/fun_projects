import time
import random
import colorama

colors = list(vars(colorama.Fore).values())

timeout = 10
timeout_start = time.time()
while time.time() < timeout_start + timeout:
    time.sleep(.5)
    print(
        " " * random.randint(0, 150)
        + f"{colorama.Style.NORMAL}"
          f"{random.choice(colors)}Happy "
          f"{random.choice(colors)}Birthday "
          f"{random.choice(colors)}MLworld ",
        end="",
    )

    print(" " * random.randint(0,150) + f"{random.choice(colors)} *", end=" ")
    print(" " * random.randint(0,150) + f"{random.choice(colors)} *")
