#TS: 20% C: 20% P: 20%
def solution(A):
    for item in range(min(A), max(A)):
        if item not in A:
            return item


#TS: 50% C: 80% P: 20%
def solution(A):
    if len(A) == 0 or start != 1:
        return 1

    start = min(A)
    end = max(A)

    for item in range(start, end):
        if item not in A:
            return item
    return max(A)+1


#TS: 60% C: 100% P: 20%
def solution(A):
    if len(A) == 0:
        return 1
    start = min(A)
    end = max(A)
    if start != 1:
        return 1
    for item in range(start, end):
        if item not in A:
            return item
        else:
            return max(A)+1


#TS: 60% C: 100% P: 20%
def solution(A):
    if len(A) == 0:
        return 1
    start = min(A)
    end = max(A)
    if start != 1:
        return 1


#TS: 100% C: 100% P: 100%
def solution(A):
    if len(A) == 0:
        return 1
    start = min(A)
    end = max(A)
    if start != 1:
        return 1

    full_list = list(range(1,end+1))
    difference = sum(full_list) - sum(A)

    if difference == 0:
        return max(A) + 1
    else:
        return difference
