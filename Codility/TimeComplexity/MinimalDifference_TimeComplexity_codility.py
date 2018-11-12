#Alpha
def solution1(A):
    temp = abs(max(A))
    solution = 0

    for i in range(1, len(A)):
        difference = abs( sum(A[:i]) - sum(A[i:]) )
        if difference < temp:
            temp = difference
            solution = i


#TS: 33% C: 66% P: 0%
def solution2(A):
    solution = abs(sum(A))

    for i in range(1, len(A)):
        difference = abs( sum(A[:i]) - sum(A[i:]) )
        if difference < solution:
            solution = difference

    return solution


#TS: 50% C: 100% P: 0%
def solution3(A):
    solution = abs(max(A) - min(A))
#chnging len(A) to initialized  variable size desn't change the score
    for i in range(1, len(A)):
        difference = abs( sum(A[:i]) - sum(A[i:]) )
        if difference < solution:
            solution = difference

    return solution


#TS: 100% C: 100% P: 100%
#import timeit


def solution(A):
    solution = abs(max(A) - min(A))
    left = sum(A[:1])
    right = sum(A[1:])
    for i in range(1, len(A)):
        difference = abs(left - right)
        if difference < solution:
            solution = difference
        left += A[i]
        right -= A[i]

    return solution

#values = range(100000)
#print(timeit.timeit('f(lst)', 'from __main__ import solution as f, values as lst', number=100))
