from sys import stdin

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    arr = list(map(int, read().rstrip().split()))
    dp = [(1, -1, arr[i]) for i in range(n)]
    visited = set([0])

    for i in range(n):
        for j in range(i):
            if j not in visited and arr[i] > arr[j]:
                visited.add(j)
                dp[i] = (max(dp[i][0], dp[j][0] + 1), j, arr[i])

    ans_len, ans_idx, last_num = max(dp)
    lst = [last_num]
    while ans_idx != -1:
        lst.append(arr[ans_idx])
        ans_idx = dp[ans_idx][1]
    lst.append(arr[ans_idx])

    for i in lst[::-1]:
        print(i, end=" ")
