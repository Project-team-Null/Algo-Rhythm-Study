if __name__ == '__main__':
    # Test case 갯수 받기
    case = int(input())
    
    # Test case 별 함수, 숫자 갯수, 숫자 리스트 초기화
    str_input = ["" for _ in range(case)]
    num_input = [0 for _ in range(case)]
    arr_input = [[] for _ in range(case)]
    
    # 함수, 숫자 갯수, 숫자 리스트 받기 및 파싱
    for i in range(case):
        str_input[i] = str(input())
        num_input[i] = int(input())
        command = str(input())
        command = command[1:len(command) - 1].split(',')
        temp = []
        for n in command:
            temp.append(n)
        arr_input[i] = temp

    # 알고리즘
    for k in range(case):
        front = 0
        back = 0
        is_front = True
        for i in str_input[k]:
            if i == 'D':
                if is_front: front += 1
                else: back += 1
            elif i == 'R':
                is_front = not is_front

        # D의 총합이 숫자 갯수보다 클 경우 error
        if front + back > num_input[k]:
            print("error")
            continue

        # 숫자 리스트의 앞, 뒤로 pop 실행
        for i in range(front):
            arr_input[k].pop(0)
        for i in range(back):
            arr_input[k].pop()

        # R이 홀수개 일 경우, 뒤집음
        if not is_front: arr_input[k].reverse()

        print('[' + ','.join(arr_input[k]) + ']')