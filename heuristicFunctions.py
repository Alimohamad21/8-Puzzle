from stateFunctions import *
from math import sqrt


def calculateManhattanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            number = getElementAtIndex(boardState, i, j)
            if number != 0:
                h += abs(goalState[number][0] - i) + abs(goalState[number][1] - j)
    return h


def calculateEuclideanHeuristic(boardState):
    h = 0
    for i in range(3):
        for j in range(3):
            number = getElementAtIndex(boardState, i, j)
            if number != 0:
                h += sqrt(abs(goalState[number][0] - i) ** 2 + abs(goalState[number][1] - j) ** 2)
    return h
