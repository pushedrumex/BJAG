s = list(input().split('-'))
add = list(map(int, s[0].split('+')))
sub = []
result = 0

for i in add: result += i
for i in range(1,len(s)): sub += list(map(int,s[i].split('+')))
for i in sub: result -= i  # '-'뒤의 숫자들은 다 빼줌
print(result)
