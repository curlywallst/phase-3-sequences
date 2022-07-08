#!/usr/bin/env python3

def print_fibonacci(length):
    fib = [0,1]
    while len(fib) < length and length > 2:
        fib.append(fib[-1] + fib[-2])

    for x in range(0,length):
        print(fib[x])