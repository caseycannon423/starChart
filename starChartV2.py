T = [[9, 3], [4, 4], [12, 2], [8, 3], [1, 2], [2, 1], [13, 3], [7, 5], [6, 2], [3, 2]]

def main():
    lastDay = 0
    maxStar = 0
    sMap = {}
    for x in T:
        if x[0] > lastDay:
            lastDay = x[0]
        if x[1] > maxStar:
            maxStar = x[1]
        sMap[x[0]] = x[1]
    while maxStar > 0:
        for x in range(1, lastDay+1):
            if x in sMap:
                if sMap[x] != maxStar:
                    print(' ', end='')
                else:
                    print('*', end='')
                    sMap[x] = sMap[x]-1
            else:
                print(' ', end='')
        maxStar = maxStar - 1
        print()
"""
def printNumbers(i):
    if i < 10:
        print(i, end='')
        #print()
    else:
        printNumbers(i//10)
        print(i%10, end='')
"""
main()
