#!/usr/bin/env python3

import sys

def factorize(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
        if n == 1:
            break
    return factors

def main(filename):
    try:
        with open(filename, 'r') as file:
            numbers = file.read().splitlines()
            for number in numbers:
                n = int(number)
                factors = factorize(n)
                if len(factors) > 1:
                    p = factors[0]
                    q = n // p
                    print(f"{n}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        filename = sys.argv[1]
        main(filename)

