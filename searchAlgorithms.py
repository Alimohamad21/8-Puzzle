import time

from stateFunctions import *


def breadthFirstSearch(boardState):
    startTime = time.time()
    frontier = set()
    frontier.add(boardState)
    explored = set()
    parentMap = {boardState: boardState}
    while len(frontier) > 0:
        currentState = frontier.pop()   # enqueue
        explored.add(currentState)
        if isGoal(currentState):
            break
        else:
            for child in getNextStates(currentState):
                if child not in frontier and child not in explored:
                    frontier.add(child)
                    parentMap[child] = currentState
    runTime = time.time() - startTime
    print('BFS PATH:\n\n')
    getPath(parentMap)
    print(f'\n\nNumber of nodes expanded in BFS: {len(explored)}')
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
    print('DFS PATH:\n\n')
    getPath(parentMap)
    print(f'\n\nNumber of nodes expanded DFS: {len(explored)}')
    print(f'\n\nDFS completed in {runTime} seconds\n\n')


def getPath(parentMap):
    child = 12345678
    parent = parentMap[child]
    path = [child]
    while child != parent:
        child = parent
        parent = parentMap[child]
        path.append(child)
    cost = len(path)
    for i in range(cost):
        printBoardState(path.pop())
    print(f'\n\nDEPTH=COST= {cost}')
