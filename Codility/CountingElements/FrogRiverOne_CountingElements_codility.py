#TS:36% C:50% P:20%
def solution(X, A):
    road = list(range(1,X+1))
    print("road: " + str(road))
    counter = range(0, len(A)-1)
    print("counter: " + str(counter))
    for i in counter:
        if A[i] in road:
            print("A[i]: " + str(A[i]))
            road.remove(A[i])
        if len(road) == 0:
            print("len(road): " + str(len(road)))
            return i


#TS:36% C:50% P:20%
def solution(X, A):
    road = list(range(1,X+1))
    counter = range(0, len(A))
    for i in counter:
        if A[i] in road:
            road.remove(A[i])
        if len(road) == 0:
            return i


#TS: 63% C:100% P:20%
def solution(X, A):
    road = list(range(1, X+1))
    counter = range(0, len(A))
    for i in counter:
        if A[i] in road:
            road.remove(A[i])
        if len(road) == 0:
            return i
    return -1


#TS: 63% C:100% P:20%
def solution(X, A):
    road = list(range(1, X+1))
    counter = range(0, len(A))
    for i in counter:
        element = A[i]
        if element in road:
            road.remove(element)
        if len(road) == 0:
            return i
    return -1


#TS: 54% C:100% P:0%
def solution(X, A):
    road = list(range(1, X+1))
    last = 0
    for i in road:
        try:
            element = A.index(i)
        except:
            return -1
        if last < element:
            last = element
    return last


#TS: 54% C:100% P:0%
def solution(X, A):
    road = list(range(1, X+1))
    last = 0
    for i in road:
        try:
            element = next(i for i, val in enumerate(A) if val == i)
        except:
            return -1
        if last < element:
            last = element
    return last

#TS: 27% C:50% P:0%
def solution(X, A):
    road = dict.fromkeys(range(1, X+1), 0)
    counter = range(0, len(A))
    for step in road:
        if step not in A:
            return -1
        road[step] = A.index(step)
    print(road)
    print(road[max(road)])


#TS: 54% C:100% P:0%
def solution(X, A):
    road = list(range(1, X+1))
    leaves = {}
    last = 0
    for item in A:
        leaves[item] = A.index[item]
    for step in road:
        try:
            if last < leaves[step]:
                last = leaves[step]
        except:
            return -1
    return last


#TS: 100% C:100% P:100%
def solution(X, A):
    road = set(range(1, X+1))
    counter = range(0, len(A))
    for i in counter:
        element = A[i]
        if element in road:
            road.remove(element)
        if len(road) == 0:
            return i
    return -1


solution(2, [1, 4, 3, 6, 2, 4])
