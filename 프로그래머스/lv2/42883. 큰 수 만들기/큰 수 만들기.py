from collections import deque

def solution(number, k):
    number = deque(list(number))
    # 만들어야하는 숫자 수
    n = len(number)-k
    stack = [number.popleft()]
    while number:
        # 추가할 수 있는 수가 끝수보다 크다면 앞으로 최대한 보냄, 아니면 그냥 뒤에 추가
        while k > 0 and stack and stack[-1] < number[0]:
            stack.pop()
            k -= 1
        stack.append(number.popleft())
    return "".join(stack[:n])