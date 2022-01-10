import math
if __name__ == '__main__':
    INIT_CHANNEL = 100
    dest = int(input())
    broken_num = int(input())
    arr = []
    if broken_num != 0:
        arr = list(map(int, input().split()))
    
    button = [str(i) for i in range(10) if i not in arr]

    cost_init = abs(INIT_CHANNEL - dest)
    mini = float('inf')
    
    val = 0
    for i in range(0, 1000000):
        is_possible = True
        number = str(i)
        for t in number:
            if t not in button:
                is_possible = False
                break
        if is_possible and abs(i - dest) < mini:
            mini = abs(i - dest)
            val = i

    cost_button = 1 + mini
    if val: cost_button += int(math.log10(val))

    print(cost_button if cost_button <= cost_init else cost_init)