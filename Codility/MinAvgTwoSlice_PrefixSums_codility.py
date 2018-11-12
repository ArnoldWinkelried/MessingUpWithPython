import random
import time

def timer(func):
    def inner(*args, **kwargs):
        t1 = time.time()
        f = func(*args, **kwargs)
        t2 = time.time()
        a = t2-t1
        print("%.16f" % a)
        return f
    return inner
"""
#TS:50% C:40% P:60% O(N*M)
#[-3, -5, -8, -4, -10]
def solution(A):
    smallest = max(A)
    startIndex = 0

    for i in range(0, len(A) - 1):
        slice = (A[i] + A[i + 1]) / 2
        if slice < smallest:
            smallest = slice
            startIndex = i

    return startIndex

#O(N**3) lol
def solution(A):
    def solution(A):

    smallest = ()
    N = len(A)
    minimum = max(A)

    for i in range(N-1):
        for j in range(N-1):

            slice = A[j:j+i+2]
            avg = sum(slice)/len(slice)

            if minimum > avg:
                minimum = avg
                smallest = (j , avg)

    return smallest[0]

#TS:60% C:100% P:20% O(N**2)
def solution(A):
    minimal = max(A)
    smallestIndex = 0

    for index in range(0, len(A)):
        sumIn = A[index]
        for step in range(index+1, len(A)):
            sumIn += A[step]
            if sumIn/(step + 1 - index) < minimal:
                minimal = sumIn/(step + 1 - index)
                smallestIndex = index

    return smallestIndex
"""

#TS:50% C:100% P:0% O(N**3)
@timer
def solutionT(A):
    minimal = max(A)
    smallestIndex = 0

    for index in range(0, len(A) - 1):
        tempList = A[index:]
        while len(tempList) > 1:
            sumIn = sum(tempList)
            if sumIn/len(tempList) < minimal:
                minimal = sumIn/len(tempList)
                smallestIndex = index
            tempList.pop()

    print("index i minimal: ", smallestIndex, minimal)
    return smallestIndex

#TS:60% C:100% P:20% O(N**2)
@timer
def solutionM(A):
    minimal = 10001
    minAvgRight, minAvgLeft = minimal, minimal
    endOfList = len(A)

    for startIndex in range(0, endOfList):
        minAvgLeft, minAvgRight = minimal, minimal

        sumRight = A[startIndex]
        for step in range(startIndex + 1, endOfList):
            sumRight += A[step]
            if sumRight/((step - startIndex) + 1) < minAvgRight:
                minAvgRight = sumRight/((step - startIndex) + 1)
                rightIndex = startIndex

        sumLeft = A[startIndex]
        for step in range(startIndex - 1, 0, -1):
            sumLeft += A[step]
            if sumLeft/((startIndex - step) + 1) < minAvgLeft:
                minAvgLeft = sumLeft /((startIndex - step))
                leftIndex = step

        if minAvgRight < minAvgLeft and minAvgRight < minimal:
            minimal = minAvgRight
            smallestIndex = rightIndex
        elif minAvgLeft < minimal:
            minimal = minAvgLeft
            smallestIndex = leftIndex

    print(smallestIndex)
    return smallestIndex

#TS:60% C:100% P:20% O(N**2)
@timer
def solutionG(A):
    print(A)
    minimal = 10001
    minDict = {}
    sum = A[0]
    startingIndex = 0
    divider = 1

    for index in range(1, len(A) - 1):
        divider += 1
        if (sum + A[index]) / divider < minimal:
            sum += A[index]
            minimal = sum / divider
            minDict[minimal] = startingIndex
        elif (sum + A[index]) / divider > minimal:
            sum = A[index]
            startingIndex = index
            divider = 1

    print(minDict)
    print(minDict[minimal])

#testingInput = [-11, 2, -10, 1, 4, -10]
testingInput = [-3, -5, -8, -4, -10]
#testingInput = [random.randrange(-10, 10) for _ in range(0, 10)]
print("========")

#solutionT(testingInput)
print("+++++++")
solutionM(testingInput)
print("========")
solutionG(testingInput)
