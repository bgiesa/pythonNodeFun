import random, time
import SystemMap
from SystemMap.Map import Map
from SystemMap.NetNode import NetNode, Position

def test():
    start_time = time.time()
    for i in range(0,10):
        sysMap = Map("Test "+str(i), 10 + (10 *i))
        print(sysMap.__str__())
        # sysMap.printMap()
    elapsed_time = time.time() - start_time
    print('EXEC TIME: {:06.4f} sec'.format(elapsed_time))

class NODE(NetNode):
    def __init__(self):
        super().__init__("NODE")
        self.maxConnections = 4
        self.char = 'N'
        self.allowedConnections = {CPU, STORAGE, IONODE, NODE}

class CPU(NetNode):
    def __init__(self):
        super().__init__("CPU")
        self.maxConnections = 4
        self.char = 'C'
        self.allowedConnections = {NODE}

class STORAGE(NetNode):
    def __init__(self):
        super().__init__("STOAGE")
        self.maxConnections = 2
        self.char = 'S'
        self.allowedConnections = {STORAGE, IONODE, NODE}

class IONODE(NetNode):
    def __init__(self):
        super().__init__("IONODE")
        self.maxConnections = 1
        self.char = 'I'
        self.allowedConnections = {STORAGE, NODE}


# dificult 0 to unlimited
def getNodesDict(dificult):
    nodeDict =  { 'cpu':1, 'storage':2, 'io': 3, 'node':5}
    for i in range(0, dificult):
        if (i % 5) == 0:
            nodeDict['cpu'] += 1            
        if(i % 2) == 0:
            nodeDict['storage'] += 1
        nodeDict['node'] += 1

    return nodeDict

def getNodeCount(nodeDict):
    res = 0
    for key in iter(nodeDict):
        res += nodeDict[key]
    return res

test()