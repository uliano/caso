from sympy import *
# compute n+1 digits and drops the last to avoid rounding.


if __name__ == '__main__':
    n = 1000000

    digits = str(N(pi, n + 1)).replace('.', '')[:-2]
    with open('pi_1M.txt', 'w') as textfile:
        textfile.write(digits)

    digits = str(N(E, n + 1)).replace('.', '')[:-2]
    with open('e_1M.txt', 'w') as textfile:
        textfile.write(digits)