#TS:83% C:83% P:83%
def solution(A):
    N = max(A)
    if len(A) == N:
        return 1
    else:
        return 0


#TS: 58% C:66% P:50%
def solution(A):
    N = max(A)
    if len(set(A)) == N:
        return 1
    else:
        return 0


#TS: 100% C:100% P:100%
def solution(A):
    N = max(A)
    elements = len(set(A))
    if elements == len(A) and elements == N:
        return 1
    else:
        return 0
