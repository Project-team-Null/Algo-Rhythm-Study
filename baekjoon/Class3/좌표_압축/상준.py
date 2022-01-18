from queue import PriorityQueue

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    n = 100000
    arr = [i for i in range(n)]
    numset = set(arr)
    pq = PriorityQueue()
    count = dict()
    for num in numset:
        pq.put(num)
    for i in range(pq.qsize()):
        count[pq.get()] = i
    for num in arr:
        print(count[num], end =" ")