def solution(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
    if stack: return False
    return True