import argparse
import os
import numpy as np
import matplotlib.pyplot as plt


def compute_digit_stats(digits):
    ntot = len(digits)
    counts = np.zeros(10)
    deviations = np.zeros((ntot, 10))
    frequencies = np.zeros((ntot, 10))
    for i, digit in enumerate(digits):
        n = i + 1
        counts[int(digit)] += 1
        for d in range(10):
            frequencies[i, d] = counts[d] / n
            deviations[i, d] = counts[d] - n/10.0

    return frequencies, deviations


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='text file with digits to analyze')
    args = parser.parse_args()

    base, _ = os.path.splitext(args.input)

    with open(args.input, 'r') as inputfile:
        the_digits = inputfile.read()

    freq, dev = compute_digit_stats(the_digits)

    ndigits = len(the_digits)
    npoints = 1000
    step = ndigits // npoints
    slicer = range(0, ndigits, step)
    x = [i + 1 for i in slicer]
    freq = freq[slicer, :]
    dev = dev[slicer, :]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.plot(x, freq)
    ax1.set_ylim([0.095, 0.105])
    ax2.plot(x, dev)
    plt.show()




