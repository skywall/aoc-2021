def scan(fn, state, seq):
    for x in seq:
        state = fn(state, x)
    return state


def move(position, operation):
    """
    Change submarine position based on passed operation

    :param position: current submarine position; 2-tuple (x, depth)
    :param operation: str <operation_name value> where operation_name is one of forward, up, down
    :return: updated position
    """
    direction, value = operation.split(" ")
    value = int(value)

    return {
        "forward": lambda (x, depth): (x + value, depth),
        "up": lambda (x, depth): (x, depth - value),
        "down": lambda (x, depth): (x, depth + value)
    }[direction](position)


with open("day2.txt", "r") as f:
    pos = scan(move, (0, 0), f)

    print(pos[0] * pos[1])
