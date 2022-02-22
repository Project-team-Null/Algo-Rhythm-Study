
import re
from collections import deque


def solution(words):
    p = re.compile('-|\+|\d*')
    deq = deque(p.findall(words)[:-1])
    result = 0
    while deq:
        word = deq.popleft()
        if word.isdigit():
            result += int(word)
        elif word == '-':
            while deq and deq[0] != '-':
                word = deq.popleft()
                if word.isdigit():
                    result -= int(word)
    return result


if __name__ == "__main__":
    words = input()
    print(solution(words))
