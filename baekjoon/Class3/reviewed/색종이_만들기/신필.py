
def solution(paper, n):
    cnt = [0, 0]

    def add_cnt(target):
        if target == 1:
            cnt[1] += 1
        else:
            cnt[0] += 1

    def search_paper(x, y, m):
        if m == 1:
            add_cnt(paper[y][x])
            return

        temp = paper[y][x]
        for j in range(y, y + m):
            for i in range(x, x + m):
                if paper[j][i] != temp:
                    k = m // 2
                    search_paper(x, y, k)
                    search_paper(x + k, y, k)
                    search_paper(x, y + k, k)
                    search_paper(x + k, y + k, k)
                    return

        add_cnt(paper[y][x])

    search_paper(0, 0, n)

    return cnt


if __name__ == "__main__":
    n = int(input())
    paper = []
    for _ in range(n):
        paper.append(list(map(int, input().split())))
    white, blue = solution(paper, n)
    print(white)
    print(blue)
