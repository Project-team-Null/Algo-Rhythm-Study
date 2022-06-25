from collections import defaultdict, deque
from sys import stdin
input = stdin.readline

n, q = map(int, input().split())
d = [0] * (n + 1)


def func_1(tree, lst):
    visited = set()
    x, v = lst[1], lst[2]
    queue = deque([x])
    while queue:
        node = queue.popleft()
        d[node] += v
        d[node] %= 2**32
        for i in tree[node]:
            if i not in visited:
                visited.add(i)
                queue += [i]


def func_2(tree, lst):
    x, y, v = lst[1], lst[2], lst[3]
    visited = set()
    queue = [(x, [x])]
    tot_way = []
    while queue:
        node, way = queue.pop()
        if node == y:
            tot_way = way
            break
        for next_node in tree[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, way + [next_node]))
    for i in tot_way:
        d[i] += v
        d[i] %= 2**32


def func_3(tree, lst):
    x, v = lst[1], lst[2]
    visited = set()
    queue = deque([x])
    while queue:
        node = queue.popleft()
        d[node] *= v
        d[node] %= 2**32
        for i in tree[node]:
            if i not in visited:
                visited.add(i)
                queue += [i]


def func_4(tree, lst):
    x, y, v = lst[1], lst[2], lst[3]
    visited = set()
    queue = [(x, [x])]
    tot_way = []
    while queue:
        node, way = queue.pop()
        if node == y:
            tot_way = way
            break
        for next_node in tree[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, way + [next_node]))
    for i in tot_way:
        d[i] *= v
        d[i] %= 2**32


def func_5(tree, lst):
    x = lst[1]
    visited = set()
    queue = deque([x])
    sum_money = 0
    while queue:
        node = queue.popleft()
        sum_money += d[node]
        for i in tree[node]:
            if i not in visited:
                visited.add(i)
                queue += [i]
    print(sum_money)


def func_6(tree, lst):
    x, y = lst[1], lst[2]
    visited = set()
    queue = [(x, d[x])]
    sum_money = 0
    while queue:
        node, money = queue.pop()
        if node == y:
            sum_money = money
            break
        for next_node in tree[node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append((next_node, money + d[next_node]))
    print(sum_money)


tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue = deque([1])
while queue:
    parent = queue.pop()
    for child in tree[parent]:
        if parent in tree[child]:
            tree[child].remove(parent)
            queue += [child]

for _ in range(q):
    lst = list(map(int, input().split()))
    if lst[0] == 1:
        func_1(tree, lst)
    elif lst[0] == 2:
        func_2(tree, lst)
    elif lst[0] == 3:
        func_3(tree, lst)
    elif lst[0] == 4:
        func_4(tree, lst)
    elif lst[0] == 5:
        func_5(tree, lst)
    elif lst[0] == 6:
        func_6(tree, lst)
