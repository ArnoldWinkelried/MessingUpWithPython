#TS:50% C:100% P:0%
from itertools import combinations


def solution(A):
    tupleA = tuple(enumerate(A))

    b = [x for x in list(combinations(tupleA, 2)) if (x[0][1] != x[1][1])
         and (x[0][1] == 0 and x[0][0] < x[1][0]) or (x[1][0] == 0 and x[0][0] > x[1][0])]


    pairs = len(b)

    if pairs > 1000000000:
        return -1
    else:
        return pairs


#TS:50% C:100% P:0%
from itertools import combinations


def solution(A):

    passings = [x for x in list(combinations(A, 2)) if x[0] != x[1] and x[0] != 1]

    pairs = len(passings)

    if pairs > 1000000000:
        return -1
    else:
        return pairs


#TS:50% C:100% P:0% for larger lists time is worse than before, but for <10k is 4x faster
def solution(A):
    pairs = 0
    zeros = A.count(0)
    sublist = A

    for zero in range(zeros):
        sublistStart = sublist.index(0) + 1
        sublist = sublist[sublistStart:]
        pairs += sublist.count(1)

        if pairs > 1000000000:
            return -1

    return pairs


#TS:50% C:100% P:0% similar to above, but for <10k is 2x faster
def solution(A):
    pairs = 0
    sublist = A
    indexedA = list(enumerate(A))
    zerosIndex = [x for x in indexedA if x[1] == 0]
    zerosIndexR = zerosIndex[::-1]
    temp = len(A)
    subSum = []

    for item in zerosIndexR:
        value = item[0]
        subSum.append(temp - value - 1)
        temp = value
    print(subSum)
    suma = 0
    i = 0
    while subSum != []:
        suma += sum(subSum)
        subSum.pop()
        i += 1
        if i > 1000000000:
            return -1
    print(suma)


#TS:50% C:100% P:0% same as before with combinations
from itertools import combinations
import collections


def solutionX(A):

    passings = list(combinations(A, 2))

    pairs = collections.Counter(passings)
    print(pairs[(0, 1)])

    if pairs[(0, 1)] > 1000000000:
        return -1
    else:
        return pairs


#TS:jebac to
def solution(A):
    pairs = 0
    i = 0
    for item in A:
        if item == 0:
            sublist = A[i:]
            pairs += sum(sublist)
            i += 1
            if pairs > 1000000000:
                return -1
    return pairs


'''
Example test:   [0, 1, 0, 1, 1]
Returned value: 5

Your test case: [0, 1, 0, 1, 1, 1, 0, 1, 0]
Returned value: 10

Your test case: [0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0]
Returned value: 35

Your test case: [0, 1, 0, 1]
Returned value: 3
'''

solutionM([0, 1, 0, 1, 1, 1, 0, 1, 0])
