def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    for term in terms:
        type, month = term.split()
        term_dic[type] = int(month)
        
    for i in range(len(privacies)):
        date, type = privacies[i].split()
        year, month, day = map(int, date.split("."))
        month += term_dic[type]
        year += month // 12
        if month % 12 == 0:
            year -= 1
            month = 12
        else:
            month = month % 12
        due_date = ".".join([str(year), ("0"+str(month))[-2:], ("0"+str(day))[-2:]])
        if today >= due_date: answer.append(i+1)
    return answer