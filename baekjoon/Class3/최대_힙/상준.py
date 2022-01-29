from sys import stdin

def downheap(heap, idx, size):
    next, left, right = idx, 2*idx, 2*idx+1
    if left <= size and heap[left] > heap[idx]: next = left
    if right <= size and heap[right] > heap[next]: next = right
    if next != idx:
        heap[idx], heap[next] = heap[next], heap[idx]
        downheap(heap, next, size)

def upheap(heap, idx):
    if idx == 1: return
    if heap[idx//2] <= heap[idx]:
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        upheap(heap, idx//2)

def heapify(heap, size, x):
    heap[size] = x
    upheap(heap, size)

if __name__ == '__main__':
    read = stdin.readline
    n = int(read().rstrip())
    heap = [0 for _ in range(100001)]
    size = 0
    for _ in range(n):
        x = read().rstrip()
        if x == '0':
            if size == 0:
                print(0)
            else:
                print(heap[1])
                heap[1], heap[size] = heap[size], heap[1]
                size -= 1
                downheap(heap, 1, size)
        else:
            size += 1
            heapify(heap, size, int(x))
        