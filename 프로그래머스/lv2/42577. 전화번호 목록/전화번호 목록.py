def solution(phone_book):
    phone_book.sort()
    N = len(phone_book)

    for i in range(N-1):
        for j in range(i+1, N):
            l = len(phone_book[i])
            if phone_book[j][:l] == phone_book[i]:
                return False
            else:
                break
    return True