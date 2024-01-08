from itertools import permutations

def solution(n, weak, dist):
    N, W = n, len(weak)
    answer = []
    weaks = weak[:]
    # 선형으로 만들기
    for w in weak:
        weaks.append(w + N)

    for i, start in enumerate(weak):
        for friends in permutations(dist):
            count = 1
            position = start

            for friend in friends:
                position += friend
                if position < weaks[i+W-1]:
                    count += 1
                    for w in weak[i+1:i+W]:
                        if w > position:
                            position = w
                            break
                else:
                    answer.append(count)
                    break
                    
    return min(answer) if answer else -1