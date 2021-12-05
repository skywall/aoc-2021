import sys


def scan(fn, state, seq):
    for x in seq:
        state = fn(state, x)
    return state


with open("day1.txt", "r") as f:
    func = lambda (last, increases), current: (int(current), increases + (int(current) > last))
    res = scan(func, (sys.maxint, 0), f)

print(res[1])
