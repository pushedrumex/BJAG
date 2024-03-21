from collections import defaultdict

N, score, P = map(int, input().split())
if N == 0:
    print(1)
    exit()

scores = list(map(int, input().split()))
scores.append(score)
scores.sort()

dic = defaultdict(int)
for x in scores:
    dic[x] += 1

rank = 1
count = 0
for x in sorted(dic.keys(), reverse=True):
    count += dic[x]
    if x == score:
        answer = rank
        break
    rank += dic[x] # 다음 등수


if count <= P:
    print(answer)
else:
    print(-1)
