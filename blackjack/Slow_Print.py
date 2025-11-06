import builtins
import time

def slow_print(*args, sep=" ", end="\n", delay=0.035, flush=True):
    text = sep.join(map(str, args)) + end
    for char in text:
        builtins.print(char, end="", flush=flush)
        time.sleep(delay)

if __name__ == "__main__":
    slow_print("")
