def solution(brown, yellow):
    answer = []
    a = 1
    b = -2 -brown//2
    c = brown + yellow
    
    X = (-b+(b*b-4*a*c)**0.5)//(2*a)
    Y = (-b-(b*b-4*a*c)**0.5)//(2*a)
    
    answer.append(max(X,Y))
    answer.append(min(X,Y))
    return answer