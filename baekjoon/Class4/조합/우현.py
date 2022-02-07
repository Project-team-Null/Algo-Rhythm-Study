from math import factorial

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(factorial(n) // factorial(n - m) // factorial(m))
