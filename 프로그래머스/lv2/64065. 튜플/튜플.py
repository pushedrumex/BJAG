def solution(s):
    arr = s[2:len(s)-2].split("},{")
    for i in range(len(arr)):
        arr[i] = list(map(int, arr[i].split(",")))
    arr.sort(key = lambda x: len(x))

    answer = []
    for i in arr:
        answer += set(i).difference(answer)
    return answer