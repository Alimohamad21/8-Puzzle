import heuristicFunctions
import searchAlgorithms

initialState = 103248567
searchAlgorithms.breadthFirstSearch(initialState)
searchAlgorithms.aStarSearch(initialState, heuristicFunctions.calculateManhattanHeuristic)
