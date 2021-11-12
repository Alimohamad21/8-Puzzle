from math import sqrt

from stateFunctions import getElementAtIndex


def calculateManhattanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            number = getElementAtIndex(boardState, i, j)
            if number != 0:
                h += abs(number // 3 - i) + abs(number % 3 - j)     # equation to get the position of a number at goal state
    return h


def calculateEuclideanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            number = getElementAtIndex(boardState, i, j)
            if number != 0:
                h += sqrt(abs(number // 3 - i) ** 2 + abs(number % 3 - j) ** 2)
    return h
