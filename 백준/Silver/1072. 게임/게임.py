total, win = map(int, input().split())

def binary_search(total, win, start, end):
    result = -1
    rate = win * 100 // total
    while start <= end:
        mid = (start + end) // 2
        _rate = (win + mid) * 100 // (total + mid)
        if rate >= _rate:
            start = mid + 1
        else:
            end = mid - 1
            result = mid
    return result

print(binary_search(total, win, 0, total))