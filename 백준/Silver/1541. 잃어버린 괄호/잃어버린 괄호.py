s = list(input().split('-'))
add = list(map(int, s[0].split('+')))
sub = []
result = 0
for i in add: result += i
for i in range(1,len(s)): sub += list(map(int,s[i].split('+')))
for i in sub: result -= i
print(result)