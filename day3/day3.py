import numpy as np


def scan(fn, state, seq):
    for x in seq:
        state = fn(state, x)
    return state


def bin_array2int(binary_array):
    """
    Convert binary array (big endian) into single integer; e.g. [1, 0, 0, 1] => 9

    :param binary_array: binary representation if the final int
    :return: integer representation of input binary array
    """
    return int("".join(map(str, binary_array)), 2)


def apply_signal(state, signal):
    items_counts, bit_counts = state

    if bit_counts is None:
        bit_counts = np.zeros(len(signal) - 1, dtype=np.int32)

    return items_counts + 1, np.add(bit_counts, [int(x) for x in signal.strip()])


with open("day3.txt", "r") as f:
    (counts, signal_bits) = scan(apply_signal, (0, None), f)

gamma = bin_array2int((signal_bits > counts / 2) + 0)
epsilon = bin_array2int((signal_bits < counts / 2) + 0)

print(gamma * epsilon)
