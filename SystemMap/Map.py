import time
from .NetNode import NetNode, Position
from .NodeUtil import *

class Map:
    def __init__(self,systemName, nodeCount):
        self.name = systemName
        self.nodeCount = nodeCount
        self.nodes = []
        self.MAP_WIDTH = 0
        self.MAP_HEIGHT = 0
        self.elapsed_time = 0
        self.factory()        

    def factory(self):
        start_time = time.time()
        nodeCount = self.nodeCount
        nodes = []
        lastNode = None
        for i in range(0, nodeCount):
            if(i == 0):
                nodeN = NetNode("CPU")
                nodeN.setChar('C')
                nodeN.setPos(0, 0)
                nodes.append(nodeN)
                lastNode = nodeN

            else:
                if(i == (nodeCount - 1)):
                    nodeN = NetNode("CONNECT")
                    nodeN.setChar('I')
                    nodeN.addConnector(lastNode)
                
                else:
                    nodeN = NetNode("NODE")
                    nodeN.setChar('N')
                    nodeN.addConnector(lastNode)

                tmpPos = Position(lastNode.x, lastNode.y)
                tmpPos = correctPosition(tmpPos, randomDirection())
                
                if(testDirection(nodes, tmpPos)):
                    nodeN.setPos(tmpPos.x, tmpPos.y)
                else:
                    tmpPos = correctPosition(tmpPos, randomDirection())
                    while(not testDirection(nodes, tmpPos)):
                        tmpPos = correctPosition(tmpPos, randomDirection())
                    nodeN.setPos(tmpPos.x, tmpPos.y)
                
                nodeN = shiftNode(nodeN, lastNode)

                nodes.append(nodeN)
                lastNode = nodeN

            minHeight = getMinHeight(nodes)
            minWidth = getMinWidth(nodes)

            for item in nodes:
                item.x = item.x + abs(minWidth)
                item.y = item.y + abs(minHeight)

        MAP_WIDTH=0 + int(getMaxWidth(nodes) + 1)
        MAP_HEIGHT=0 + int(getMaxHeight(nodes) + 1)
        self.MAP_HEIGHT = MAP_HEIGHT
        self.MAP_WIDTH = MAP_WIDTH

        self.nodes = nodes
        self.elapsed_time = time.time() - start_time                        

    def getMapString(self):
        nodes = self.nodes
        MAP_WIDTH=0 + int(getMaxWidth(nodes) + 1)
        MAP_HEIGHT=0 + int(getMaxHeight(nodes) + 1)
        self.MAP_HEIGHT = MAP_HEIGHT
        self.MAP_WIDTH = MAP_WIDTH

        map = [[ '.'
                for y in range(MAP_HEIGHT) ]
                    for x in range(MAP_WIDTH)]

        for item in nodes:
            if item.type == 'CPU':
                map[int(item.x)][int(item.y)] = item.char
            if item.type == 'NODE':
                map[int(item.x)][int(item.y)] = item.char
            if item.type == 'CONNECT':
                map[int(item.x)][int(item.y)] = item.char

        out = ""
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                out += map[x][y]
            out += "\n"
        return out

    def printMap(self):
        print(self.getMapString())

    def __str__(self):
        return str('Name: {} | Nodes: {} | width: {:5} | height: {:5} | exec time: {:06.4f} sec'.format(self.name, self.nodeCount, self.MAP_WIDTH, self.MAP_HEIGHT, self.elapsed_time))