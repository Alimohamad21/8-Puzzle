import time

from heapdict import heapDict
from heuristicFunctions import *
from stateFunctions import *


def breadthFirstSearch(boardState):
    startTime = time.time()
    frontier = []  # list used as queue
    optimizedFrontier = set()  # used a set to keep track of the frontier to make searching for expanded nodes in frontier in O(1)
    optimizedFrontier.add(boardState)
    frontier.append(boardState)
    explored = set()
    parentMap = {
        boardState: boardState}  # parent map to keep track of each of the child's parents, to get the goal path at the end
    while len(frontier) > 0:
        currentState = frontier.pop(0)  # dequeue
        explored.add(currentState)
        if isGoal(currentState):
            break
        else:
            children = getNextStates(currentState)
            for child in children:
                if child not in optimizedFrontier and child not in explored:
                    frontier.append(child)  # enqueue
                    optimizedFrontier.add(child)  # optimized frontier is updated with main frontier
                    parentMap[child] = currentState
    runTime = time.time() - startTime
    print('BFS PATH:\n\n')
    getPath(parentMap)
    print(f'\n\nNumber of nodes expanded in BFS: {len(explored)}')
    print(f'\n\nBFS completed in {runTime} seconds\n\n')


def depthFirstSearch(boardState):
    startTime = time.time()
    frontier = []  # list used as stack
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
            children = getNextStates(currentState)
            for child in children:
                if child not in explored and child not in optimizedFrontier:
                    frontier.append(child)  # push
                    optimizedFrontier.add(child)
                    parentMap[child] = currentState
    runTime = time.time() - startTime
    print('DFS PATH:\n\n')
    getPath(parentMap)
    print(f'\n\nNumber of nodes expanded in DFS: {len(explored)}')
    print(f'\n\nDFS completed in {runTime} seconds\n\n')


def aStarSearch(initialState, heuristic=calculateManhattanHeuristic):
    startTime = time.time()
    frontier = heapDict()
    frontier[initialState] = heuristic(initialState)
    explored = set()
    parentMap = {initialState: initialState}
    gScore = {initialState: int}
    hscore = {initialState: int}
    gScore[initialState] = 0
    hscore[initialState] = heuristic(initialState)
    expanded = 0
    while len(frontier):
        expanded += 1
        state = frontier.popitem()[0]
        explored.add(state)
        if isGoal(state):
            break
        else:
            children = getNextStates(state)
            for child in children:
                if child not in explored and child not in frontier:
                    gScore[child] = gScore[state] + 1
                    hscore[child] = heuristic(child)
                    frontier[child] = gScore[child] + hscore[child]
                    parentMap[child] = state
                elif child in frontier:
                    t_gScore = gScore[state] + 1
                    if hscore[child] + t_gScore < frontier[child]:
                        gScore[child] = t_gScore
                        frontier[child] = hscore[child] + gScore[child]
                        parentMap[child] = state
    runTime = time.time() - startTime
    print('A* PATH:\n\n')
    getPath(parentMap)
    print(f'\n\nNumber of nodes expanded A*: {expanded}')
    print(f'\n\nA* completed in {runTime} seconds\n\n')


def getPath(parentMap):
    child = 12345678
    parent = parentMap[child]
    path = [child]
    while child != parent:
        child = parent
        parent = parentMap[child]
        path.append(child)
    n = len(path)
    cost = n - 1
    for i in range(n):
        printBoardState(path.pop())
    print(f'\n\nDEPTH=COST= {cost}')
