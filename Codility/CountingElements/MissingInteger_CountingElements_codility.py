#TS:55% C:60% P:50%
def solution(A):
    setA = set(A)
    maxi = max(setA)

    if maxi < 1 or min(setA) != 1:
        return 1
    elif maxi == len(setA):
        return maxi + 1
    else:
        for i in range(1, maxi):
            if i not in setA:
                return i


#TS:77% C:80% P:75%
def solution(A):
    setA = set(A)
    maxi = max(setA)

    if (maxi < 1 or min(setA) != 1) and 1 not in setA:
        return 1
    elif maxi == len(setA):
        return maxi + 1
    else:
        for i in range(1, maxi):
            if i not in setA:
                return i


#TS:100% C:100% P:100% <30min            
def solution(A):
    setA = set(A)
    maxi = max(setA)

    if (maxi < 1 or min(setA) != 1) and 1 not in setA:
        return 1
    else:
        for i in range(1, maxi + 1):
            if i not in setA:
                return i
