# 리프 한 층이 추가되면 이진수 사이사이에 추가
# 서브 트리의 루트가 0이라면 자손들은 다 0
# 완전 이진 트리의 노드 개수 : 2**k - 1
def checkTree(tree, left, right):
    
    # 체크를 완료한 트리
    if left >= right: return 1

    root = (left+right) // 2
    
    # 루트가 0 이라면 자손은 다 0
    if tree[root] == 0:
        for i in range(left, right+1):
            if tree[i] != 0: return 0
    return min(checkTree(tree, left, root-1), checkTree(tree, root+1, right))
        

def solution(numbers):
    answer = []
    for number in numbers:
        binary = list(map(int, bin(number)[2:]))
        
        # 완전 이진 트리로 만들기
        temp = len(binary)
        k = 1
        while temp > 2**k-1: k += 1
        complete_binary = [0]*(2**k-1-temp) + binary
        
        # 유효한 트리인지 체크
        answer.append(checkTree(complete_binary, 0, len(complete_binary)-1))
    return answer