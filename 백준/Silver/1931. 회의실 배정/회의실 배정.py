time_table = []

for _ in range(int(input())):
    time_table.append(list(map(int, input().split())))

time_table.sort(key=lambda x: (x[1], x[0]))

answer, temp = 0, 0
for start, end in time_table:
    if temp <= start:
        answer += 1
        temp = end

print(answer)