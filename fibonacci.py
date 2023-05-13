#!/usr/bin/env python3
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number"""
    if n <=0:
        raise ValueError("n must be positive")

    if n ==1:
        return 0

    if n == 2:
        return 1

    prev, curr = 0, 1
    for _ in range(2,n):
        prev, curr = curr, prev + curr

    return curr
