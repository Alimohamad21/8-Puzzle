import time

from heapdict import heapDict
from stateFunctions import *


def breadthFirstSearch(boardState):
    startTime = time.time()
    frontier = set()
    frontier.add(boardState)
    explored = set()
    parentMap = {boardState: boardState}
    while len(frontier) > 0:
        currentState = frontier.pop()  # enqueue
        explored.add(currentState)
        if isGoal(currentState):
            break
        else:
            for child in getNextStates(currentState):
                if child not in frontier and child not in explored:
                    frontier.add(child)
                    parentMap[child] = currentState
    runTime = time.time() - startTime
    getPath(parentMap)
    print(f'\n\nBFS completed in {runTime} seconds\n\n')


def depthFirstSearch(boardState):
    startTime = time.time()
    frontier = []
    optimizedFrontier = set()
    optimizedFrontier.add(boardState)
    frontier.append(boardState)
    explored = set()
    parentMap = {boardState: boardState}
    while len(frontier) > 0:
        currentState = frontier.pop()
        explored.add(currentState)
        if isGoal(currentState):
            break
        else:
            for child in getNextStates(currentState):
                if child not in explored and child not in optimizedFrontier:
                    frontier.append(child)
                    optimizedFrontier.add(child)
                    parentMap[child] = currentState
    runTime = time.time() - startTime
    getPath(parentMap)
    print(f'\n\nDFS completed in {runTime} seconds\n\n')


def aStarSearch(initialState, heuristic):
    startTime = time.time()
    frontier = heapDict()
    frontier[initialState] = heuristic(initialState)
    explored = set()
    parentMap = {initialState: initialState}
    gScore = {initialState: int}
    fScore = {initialState: int}
    gScore[initialState] = 0
    fScore[initialState] = heuristic(initialState)
    expanded = 0
    while len(frontier):
        expanded += 1
        state = frontier.popitem()[0]
        explored.add(state)
        if isGoal(state):
            runTime = time.time() - startTime
            getPath(parentMap)
            print(f'\n\nA-Star completed in {runTime} seconds and expanded a total of {expanded} Nodes\n\n')
            return True
        else:
            for child in getNextStates(state):
                if child not in explored and child not in frontier:
                    gScore[child] = gScore[state] + 1
                    fScore[child] = heuristic(child)
                    frontier[child] = gScore[child] + fScore[child]
                    parentMap[child] = state
                elif child in frontier:
                    gScore[child] = gScore[state] + 1
                    fScore[child] = heuristic(state)
                    if fScore[child] + gScore[child] < frontier[child]:
                        frontier[child] = fScore[child] + gScore[child]
    runTime = time.time() - startTime
    print(f'\n\nA-Star completed in {runTime} seconds\n\n')
    return False


def getPath(parentMap):
    child = 12345678
    parent = parentMap[child]
    path = [child]
    while child != parent:
        child = parent
        parent = parentMap[child]
        path.append(child)
    cost = len(path)
    print('PATH:\n\n')
    for i in range(cost):
        printBoardState(path.pop())
    print(f'\n\nDEPTH=COST= {cost}')
