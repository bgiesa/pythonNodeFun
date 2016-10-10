import random

def randomDirection():
    return random.randint(0,3)

def correctPosition(position, direction):
    # NORTH
    if direction == 0:
        position.y = position.y - 1
    # EAST
    if direction == 1:
        position.x = position.x + 1
    # SOUTH
    if direction == 2:
        position.y = position.y + 1
    # WEST
    if direction == 3:
        position.x = position.x - 1
    return position

def shiftNode(node, oldnode):
    
    return node

def testDirection(nodes, pos):
    for item in nodes:
        if ((item.x == pos.x) and (item.y == pos.y)):
            return False
    return True

def getMaxWidth(nodes):
    x=0
    for item in nodes:
       if item.x > x:
           x = item.x
    return x

def getMinWidth(nodes):
    x=0
    for item in nodes:
        if item.x < x:
            x = item.x
    return x
    
def getMaxHeight(nodes):
    y=0
    for item in nodes:
       if item.y > y:
           y = item.y
    return y

def getMinHeight(nodes):
    y=0
    for item in nodes:
        if item.y < y:
            y = item.y
    return y

# get the node with min height
def getItemWithMinHeight(minHeight, nodes):
    result = []
    for item in nodes:
        if item.x == minHeight:
            result.append(item)
    return result

# get the node with min width
def getItemWithMinWidth(minWidth, nodes):
    result = []
    for item in nodes:
        if item.y == minWidth:
            result.append(item)
    return result