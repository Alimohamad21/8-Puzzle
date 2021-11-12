import random


def isGoal(boardState):
    if boardState == 12345678:
        return True
    else:
        return False


def getRandomState():
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    random.shuffle(arr)
    randomState = int(''.join(arr))
    return randomState


def getElementAtIndex(boardState, i, j):
    temp = boardState
    return temp // 10 ** (8 - (3 * i + j)) % 10  # equation to get element at position i,j in the board


def findIndexOf(boardState, toBeFound):
    temp = boardState
    for i in range(9):
        if temp % 10 == toBeFound:
            return (8 - i) // 3, (8 - i) % 3  # equation to get i,j of a certain element in the board
        temp = temp // 10


def printBoardState(boardState):
    for i in range(3):
        for j in range(3):
            element = getElementAtIndex(boardState, i, j)
            if element != 0:
                print(element, end="\t")
            else:
                print('_', end="\t"),
        print('\n')
    print('---------')


def swap(boardState, position1, position2):  # function for swapping the blocked tile with an adjacent number
    tempBoardState = str(boardState)
    if boardState < 100000000:
        tempBoardState = '0' + tempBoardState
    tempBoardState = list(tempBoardState)
    tempBoardState[position1], tempBoardState[position2] = tempBoardState[position2], tempBoardState[position1]
    return int(''.join(tempBoardState))


def getNextStates(boardState):  # generates all possible next states by swapping blocked tile with an adjacent number
    states = []
    i, j = findIndexOf(boardState, 0)
    position1 = 3 * i + j
    if i < 2:
        # swap blocked tile with lower
        position2 = 3 * (i + 1) + j
        states.append(swap(boardState, position1, position2))
    if j < 2:
        # swap blocked tile with right
        position2 = 3 * i + (j + 1)
        states.append(swap(boardState, position1, position2))
    if i > 0:
        # swap blocked tile with upper
        position2 = 3 * (i - 1) + j
        states.append(swap(boardState, position1, position2))
    if j > 0:
        # swap blocked tile with left
        position2 = 3 * i + (j - 1)
        states.append(swap(boardState, position1, position2))
    return states
