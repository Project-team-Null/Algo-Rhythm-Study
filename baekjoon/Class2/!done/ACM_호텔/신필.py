
def solution(h, w, n):
    width, height = divmod(n, h)
    if height == 0:
        height = h
        width -= 1
    return height*100 + width+1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        h, w, n = map(int, input().split())
        print(solution(h, w, n))
