from searchAlgorithms import *
state = 413270568
depthFirstSearch(state)
breadthFirstSearch(state)
initialState = 103248567
breadthFirstSearch(initialState)
aStarSearch(initialState, heuristicFunctions.calculateManhattanHeuristic)
