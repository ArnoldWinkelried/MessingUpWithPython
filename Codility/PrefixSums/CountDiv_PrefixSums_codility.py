#TS:50% C:100% P:0% O(B-A)
def solution(A, B, K):
    divisible = 0

    for number in range(A,B+1):
        if number % K == 0:
            divisible += 1

    return divisible

#TS:50% C:100% P:0%
def solution(A, B, K):
    divisible = 0

    for number in range(B+1, A, -1):
        if number % K == 0:
            divisible = number / K - int(A / K)
            break

    return divisible

#TS:100% C:100% P:100%  O(1) !!!
def solutionG(A, B, K):
    divisible = 0

    if len(range(B, A, -1)) < 1:
        if A % K == 0 or B % K == 0:
            divisible += 1

    for number in range(B, A, -1):
        if number % K == 0:
            divisible = int(number / K) - int(A / K)
            if A % K == 0:
                divisible += 1
            break
    return divisible

solutionG(1, 10, 2)
