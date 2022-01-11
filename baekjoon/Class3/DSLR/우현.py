from collections import deque

def move(C, num):
    if C == 'D': return (num*2) % 10000
    elif C == 'S': return (10000 + num - 1) % 10000
    elif C == 'L': return (num*10 + int(num/1000)) % 10000
    else: return int(num/10) + 1000*(num%10)
    
def solution():
    n, m = map(int, input().split())
    moved = ["" for _ in range(10000)]
    moved[n] = "_"
    bfs = deque([n])
    move_arr = ['D', 'S', 'L', 'R']
    while bfs:
        num = bfs.popleft()
        if num == m:
            print(moved[num][1:])
            break
        
        for char in move_arr:
            moved_num = move(char, num)
            if moved[moved_num] == "" and num != moved_num:
                bfs += [moved_num]
                moved[moved_num] = moved[num] + char

if __name__ == '__main__':
    case = int(input())
    
    for i in range(case):
        solution()
