from sys import stdin

def init_seg(arr, seg_tree, idx, frm, to):
    if frm == to: 
        seg_tree[idx] = arr[frm]
        return seg_tree[idx]
    mid = (frm + to) // 2
    seg_tree[idx] = init_seg(arr, seg_tree, 2*idx, frm, mid) + init_seg(arr, seg_tree, 2*idx+1, mid+1, to)
    return seg_tree[idx]


def get_sum(seg_tree, idx, frm, to, left, right):
    if frm > right or to < left: return 0
    if frm <= left and right <= to: return seg_tree[idx]
    mid = (left + right) // 2
    return get_sum(seg_tree, 2*idx, frm, to, left, mid) + get_sum(seg_tree, 2*idx+1, frm, to, mid+1, right)


if  __name__ == '__main__':
    read = stdin.readline
    n, m = map(int, read().rstrip().split())
    arr = list(map(int, read().rstrip().split()))
    c_sum = [0] * (n+1)
    for i in range(n):
        c_sum[i+1] = c_sum[i] +arr[i]
    for _ in range(m):
        i, j = map(int, read().rstrip().split())
        print(c_sum[j] - c_sum[i-1])
    
    # seg_tree = [0] * (4*n)
    # init_seg(arr, seg_tree, 1, 1, n)
    
    # for _ in range(m):
    #     i, j = map(int, read().rstrip().split())
    #     print(get_sum(seg_tree, 1, i, j, 1, n))