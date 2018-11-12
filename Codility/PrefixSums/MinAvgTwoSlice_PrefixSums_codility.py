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


    Example test:   [4, 2, 2, 5, 1, 5, 8]
Output (stderr):
Invalid result type, int expected, <class 'NoneType'> found.
Output:
[(0, 2.0), (1, 1.0), (1, 1.0), (1, 5.5), (4, 0.5), (1, 5.5), (6, 4.0)]
RUNTIME ERROR (tested program terminated with exit code 1)
"""
Dokumentacja upadku, tu leży jakiś pomysł, 
ale autor już nie pamięta jaki.. dobranoc.

def solution(A):

    listed = []

    for item in A:
        startIndex = A.index(item)
        leftIndex = startIndex
        rightIndex = startIndex
        testSumLeft = item
        testSumRight = item

        decreasing = True
        i = 1
        while decreasing and (startIndex + i) < (len(A) - 1):
            if (leftIndex - 1) > 0 and (testSumLeft + A[leftIndex-1])/(i+1) < testSumLeft:
                testSumLeft += A[leftIndex-1]
                leftIndex -= 1
            elif (rightIndex + 1) < (len(A) - 1) and (testSumRight + A[rightIndex+1])/(i+1) < testSumRight:
                testSumRight += A[rightIndex+1]
                rightIndex += 1
            else:
                decreasing = False
                if i != 1:
                    if testSumLeft <= testSumRight:
                        listed.append([leftIndex, testSumLeft/(i), i, startIndex])
                    elif testSumLeft > testSumRight:
                        listed.append([rightIndex, testSumRight/(i), i, startIndex])
            i += 1
        print(listed)
"""
