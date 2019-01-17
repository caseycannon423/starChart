T = [[9, 3], [4, 4], [12, 2], [8, 3], [1, 2], [2, 1], [13, 3], [7, 5], [6, 2], [3, 2]]

def findStart(Array):
    iMax = 0
    cell = Array[0]
    for x in Array:
        if x[1] > iMax:
            iMax = x[1]
            cell = x
    return cell

def findMaxChartDay(Array):
    iLargestIndex = 0
    for x in Array:
        if x[0] > iLargestIndex:
            iLargestIndex = x[0]
    return iLargestIndex

def printLine(starList, days):
    for x in range(days+1):
        bMatch = False
        for star in starList:
            if x == star:
                bMatch = True
        if bMatch == True:
            print('*', end='')
        else:
            print(' ', end='')
    print()

def main():
    start = findStart(T)
    days = findMaxChartDay(T)
    starList = [start[0]]
    for x in range(start[1]-1, -1, -1):
        printLine(starList, days)
        for cell in T:
            if cell[1] == x:
                starList.append(cell[0])
    for x in range(days):
        print(x+1, end='')

main()

