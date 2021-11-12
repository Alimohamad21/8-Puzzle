def isSolvable(boardState):
    array = [int(x) for x in str(boardState)]
    sortedList, inversions = Inversions(array)
    if inversions % 2 == 0:
        return True
    else:
        return False


def counter(left, right):
    mergedList = list()
    inversions, l, r = 0, 0, 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            mergedList.append(left[l])
            l += 1
        else:
            mergedList.append(right[r])
            if right[r] != 0:
                inversions += (len(left) - l)
            r += 1
    mergedList += left[l:]
    mergedList += right[r:]
    return mergedList, inversions


def Inversions(list):
    if len(list) <= 1:
        return list, 0
    midIndex = len(list) // 2
    leftList, leftInversions = Inversions(list[:midIndex])
    rightList, rightInversions = Inversions(list[midIndex:])
    mergedList, mergedInversions = counter(leftList, rightList)
    mergedInversions += (leftInversions + rightInversions)
    return mergedList, mergedInversions
