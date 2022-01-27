def solve():
    commands = input()
    n = int(input())
    data = input()[1:-1]
    arr = list(data.split(','))
    
    is_reversed = False
    low, high = 0, n-1
    for command in commands:
        if command == 'R':
            is_reversed = not is_reversed
        else:
            if is_reversed: high -= 1
            else: low += 1
        if low > high + 1:
            print("error")
            return
    
    if is_reversed:
        arr = arr[low:high+1]
        arr.reverse()
        print('[' + ','.join(arr) + ']')
    else:
        print('[' + ','.join(arr[low:high+1]) + ']')
    return

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()