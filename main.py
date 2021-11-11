from searchAlgorithms import *

start=0
end=2
for x in range(start,end):
    filename=f"optimal/manhattan/puzzle3x3-{x:02d}.txt"
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            aStarSearch(int(line), heuristicFunctions.calculateManhattanHeuristic)

