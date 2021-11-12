from searchAlgorithms import *
from solvable import isSolvable

state = getRandomState()
print('CURRENTLY SOLVING:')
printBoardState(state)
if not isSolvable(state):
    print('8 PUZZLE NOT SOLVABLE DUE TO ODD NUMBER OF INVERSIONS')
    exit(0)
depthFirstSearch(state)
breadthFirstSearch(state)
print('\n\nA* USING MANHATTAN HEURISTIC:\n\n')
aStarSearch(state, calculateManhattanHeuristic)
print('\n\nA* USING EUCLIDEAN HEURISTIC:\n\n')
aStarSearch(state, calculateEuclideanHeuristic)
