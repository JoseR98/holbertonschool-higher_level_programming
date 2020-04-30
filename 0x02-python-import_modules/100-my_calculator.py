#!/usr/bin/python3
from sys import argv
num_args = len(argv)
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+' or argv[2] == '-' or argv[2] == '*' or argv[2] == '/':
        symbol = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if symbol == '+':
            op = add(a, b)
        elif symbol == '-':
            op = sub(a, b)
        elif symbol == '*':
            op = mul(a, b)
        elif symbol == '/':
            op = div(a, b)
        print("{:d} {} {:d} = {:d}".format(a, symbol, b, op))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
