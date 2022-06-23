def gcd(A,B):
    return B if A%B == 0 else gcd(B,A%B)
    
def solution(w,h):
    return w*h - (w+h-gcd(w,h))

# w,h의 서로소 w0 = w/gcd(w,h), h0 = h/gcd(w,h)
# w0*h0 종이에서 대각선을 그을 때 1+(w0-1)+(ho-1)개의 정사각형을 지나게 됨
# 즉, 사용 불가능한 정사각형은 gcd(w,h)*(1+(w0-1)+(ho-1))개
