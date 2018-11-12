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

#TS:62% C:100% P:0% O(N*M)

def solution(S, P, Q):
    output = []

    nucleotideDict = {"A" : 1,
                      "C" : 2,
                      "G" : 3,
                      "T" : 4}

    for i in range(0, len(P)):
        nucleotide = min(S[P[i]:Q[i]+1])
        output.append(nucleotideDict[nucleotide])

    return output


#TS:62% C:100% P:0% O(N*M)
#for medium size arrays, with mid scenario, this method is roughly 3 times faster then bellow
#for worse cases bellow wins
@timer
def solutionM(S, P, Q):
    output = []

    for i in range(0, len(P)):

        tempSet = set(S[P[i]:Q[i]+1])

        if   "A" in tempSet:
            output.append(1)
        elif "C" in tempSet:
            output.append(2)
        elif "G" in tempSet:
            output.append(3)
        elif "T" in tempSet:
            output.append(4)

    return output

#TS:100% C:100% P:100% O(N+M) zrob takie tylko swoje
@timer
def solutionO(S, P, Q):
    cost_dict = {'A':1, 'C':2, 'G':3, 'T':4}

    curr_counts = [0,0,0,0]
    counts = [curr_counts[:]]
    for s in S:
        curr_counts[cost_dict[s]-1] += 1
        counts.append(curr_counts[:])

    results = []
    for i in range(len(Q)):
        counts_q = counts[Q[i] + 1]
        counts_p = counts[P[i]]

        if Q[i] == P[i]:
            results.append(cost_dict[S[Q[i]]])
        elif counts_q[0] > counts_p[0]:
            results.append(1)
        elif counts_q[1] > counts_p[1]:
            results.append(2)
        elif counts_q[2] > counts_p[2]:
            results.append(3)
        elif counts_q[3] > counts_p[3]:
            results.append(4)

    return results

geny = list("AGGTGACCGATTAAGGTGACCGATTAGAACCTGAATTAAGGTGACCTGACCGATTAAGGTGACCGATTAGAACCTGTGACCGATTAGAACCT")
peki = [1, 2, 4, 4, 5, 3, 2, 10, 5, 6, 4, 16, 11, 17, 1, 2, 4, 4, 5, 3, 2, 10, 5, 6, 4, 16, 11, 17]
quki = [len(geny)-1] * len(peki)


solutionM(geny, peki, quki)


solutionO(geny, peki, quki)
