# Number Frames
# n = 5
#
# 555555555
# 4   4   4  
# 3   3   3  
# 2   2   2
# 1111*1111
# 2   2   2
# 3   3   3
# 4   4   4
# 555555555

import math

def getWidth(target):
    max_width = (target * 2) - 1
    mid = math.ceil((max_width / 2))
    return { 'mid': mid, 'max_width': max_width }


def createTopBottomBounds(target, max_width):
    _str = ""
    for i in range(max_width):
        _str += str(target)

    return _str

def createMid(n, mid, max_width):
    for i in range(max_width):
        if i == (mid - 1):
            print("*", end="")
        else:
            print(n, end="")

    print("")

def createFrame(n, mid, max_width):
    _str = "";

    for i in range(max_width):
        if i == 0 or i == (mid - 1) or i == (max_width - 1):
            _str += str(n)
        else:
            _str += str(" ")

    
    return _str


def createBody(target, mid, max_width):
    _tb = createTopBottomBounds(target, max_width)
    
    #upper
    for i in reversed(range(target)):
        cursor = (i + 1)
        if cursor == target:
            print(_tb)
        elif cursor == 1:
            print("", end="")
        else:
            print(createFrame(cursor, mid, max_width))


    createMid(1, mid, max_width)

    for i in range(target):
        cursor = (i + 1)
        if cursor == target:
            print(_tb)
        elif cursor == 1:
            print("", end="")
        else:
            print(createFrame(cursor, mid, max_width))


def main():
    target_number = int(input("Input: "))
    gw = getWidth(target_number)
    mid = gw["mid"]
    max_width = gw["max_width"]
    createBody(target_number, mid, max_width)

main()
