if __name__ == '__main__':
    cnt = int(input())
    
    arr = [0 for _ in range(cnt)] 
    
    for i in range(cnt):
        arr[i] = int(input())
        
    zeros = [0 for _ in range(max(arr) + 1)]
    ones = [0 for _ in range(max(arr) + 1)]
    
    for i in range(max(arr) + 1):
        if i == 0: zeros[i] += 1
        elif i == 1: ones[i] += 1
        else:
            zeros[i] = zeros[i - 2] + zeros[i - 1]
            ones[i] = ones[i - 2] + ones[i - 1]
        
        
    for i in arr:
        print(zeros[i], ones[i])