from sys import stdin, setrecursionlimit
setrecursionlimit(1000000)

def solve(inorder, postorder, i_frm, i_to, p_frm, p_to, idx_dict):
    if p_frm > p_to: return
    pivot = idx_dict[postorder[p_to]]
    print(postorder[p_to], end = " ")
    solve(inorder, postorder, i_frm, pivot-1, p_frm, p_to - (i_to - pivot + 1), idx_dict)
    solve(inorder, postorder, pivot+1, i_to, p_frm + pivot - i_frm, p_to-1, idx_dict)


if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    inorder = list(map(int, read().rstrip().split()))
    postorder = list(map(int, read().rstrip().split()))
    idx_dict = {}
    for i, num in enumerate(inorder):
        idx_dict[num] = i
    solve(inorder, postorder, 0, n-1, 0, n-1, idx_dict)

# 15
# 8 4 9 2 10 5 11 1 12 6 13 3 14 7 15
# 8 9 4 10 11 5 2 12 13 6 14 15 7 3 1