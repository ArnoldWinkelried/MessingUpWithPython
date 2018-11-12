#TS: 44% C: 100% P: 0%
def solution(X, Y, D):
    counter = 0
    while X < Y:
        X += D
        counter += 1
    return counter
#For example, for the input (3, 999111321, 7)
#the solution exceeded the time limit.

#TS: 100% C: 100% P: 100%
from decimal import Decimal


def solution(X, Y, D):
    road_ahead = Y - X
    solution = road_ahead / D
    if solution % 1 > 0:
        solution += 1
    return int(solution)
