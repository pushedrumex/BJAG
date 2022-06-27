def solution(files):
    answer = []
    d = {}
    for i in range(len(files)):
        for j in range(len(files[i])):
            if files[i][j].isnumeric():
                for k in range(j,j+6): # 5개가 모두 숫자인 경우 고려
                    if k == len(files[i]) or not files[i][k].isnumeric():break
                break
        d[files[i]] = [files[i][:j].lower(),int(files[i][j:k]),i]
    d_sorted= sorted(d.items(),key=lambda x:x[1])
    for ds in d_sorted:answer.append(ds[0])
    return answer
