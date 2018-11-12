#TS:66% C:100% P:40%
def solution(N, A):
    counters = []
    for i in range(N):
        counters.append(0)
    for item in A:
        if item >= 1 and item <= N:
            counters[item - 1] += 1
        if item > N:
            maxi = max(counters)
            for i in range(N):
                counters[i] = maxi
    return counters


#TS:66% C:100% P:40%
def solution(N, A):
    counters = [0] * N

    for item in A:
        if item >= 1 and item <= N:
            counters[item - 1] += 1
        if item > N:
            maxi = max(counters)
            for i in range(N):
                counters[i] = maxi
    return counters


#TS:66% C:100% P:40%
def solution(N, A):
    counters = [0] * N

    for item in A:
        if item >= 1 and item <= N:
            counters[item - 1] += 1
        if item > N:
            maxi = max(counters)
            counters = [maxi] * N
    return counters


#TS:88% C:100% P:80%
def solution(N, A):
    counters = [0] * N
    maxi = 0
    for item in A:
        if item >= 1 and item <= N:
            counters[item - 1] += 1
            if counters[item - 1] > maxi:
                maxi = counters[item - 1]
        if item > N:
            counters = [maxi] * N
    return counters


#TS:88% C:100% P:80%
def solution(N, A):
    counters = [0] * N
    maxi = 0
    for item in A:
        if item >= 1 and item <= N:
            counters[item - 1] += 1
            if counters[item - 1] > maxi:
                maxi = counters[item - 1]
        if item > N:
            counters = [maxi] * N
    return counters
