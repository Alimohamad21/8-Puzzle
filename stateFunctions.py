import random


def isGoal(boardState):
    if boardState == 12345678:
        return True
    else:
        return False


def isSolvable(boardState):
    return True


def getRandomState():
    arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    random.shuffle(arr)
    randomState = int(''.join(arr))
    return randomState


def getElementAtIndex(boardState, i, j):
    temp = boardState
    return temp // 10 ** (8 - (3 * i + j)) % 10


def findIndexOf(boardState, toBeFound):
    temp = boardState
    for i in range(9):
        if temp % 10 == toBeFound:
            return (8 - i) // 3, (8 - i) % 3
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


def swap(boardState, position1, position2):
    tempBoardState = str(boardState)
    if boardState < 100000000:
        tempBoardState = '0' + tempBoardState
    tempBoardState = list(tempBoardState)
    tempBoardState[position1], tempBoardState[position2] = tempBoardState[position2], tempBoardState[position1]
    return int(''.join(tempBoardState))


def getNextStates(boardState):
    states = []
    i, j = findIndexOf(boardState, 0)
    position1 = 3 * i + j
    if i < 2:
        position2 = 3 * (i + 1) + j
        states.append(swap(boardState, position1, position2))
        # swap with lower
    if j < 2:
        position2 = 3 * i + (j + 1)
        states.append(swap(boardState, position1, position2))
        # swap with right
    if i > 0:
        position2 = 3 * (i - 1) + j
        states.append(swap(boardState, position1, position2))
        # swap with upper
    if j > 0:
        position2 = 3 * i + (j - 1)
        states.append(swap(boardState, position1, position2))
        # swap with left
    return states
