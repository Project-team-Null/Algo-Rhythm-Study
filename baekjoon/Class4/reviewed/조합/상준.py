from sys import stdin
from math import *

if __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    print(factorial(n)//(factorial(m)*factorial(n-m)))