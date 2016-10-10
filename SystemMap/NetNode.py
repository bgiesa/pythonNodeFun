class NetNode:
    def __init__(self, nodeType):
        self.x = 0
        self.y = 0
        self.nodeType = nodeType
        self.char = ' '
        self.connected = []
        self.position = Position(self.x, self.y)
        self.maxConnections = 0
        self.allowedConnections = []

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.position.setPosition(x, y)

    def addConnector(self, node):
        self.connected.append(node)

    def getConnectorN(self):
        for con in self.connected:
            if (con.x == self.x) and (con.y == self.y -1):
                return con
        return None

    def getConnectorE(self):
        for con in self.connected:
            if (con.x == self.x + 1) and (con.y == self.y):
                return con
        return None

    def getConnectorS(self):
        for con in self.connected:
            if (con.x == self.x) and (con.y == self.y + 1):
                return con
        return None

    def getConnectorW(self):
        for con in self.connected:
            if (con.x == self.x - 1) and (con.y == self.y):
                return con
        return None

    def getConnectorPos(self, pos):
        pos = self.position
        if pos == 0:            
            pos.y = pos.y - 1
            return pos
        elif pos == 1:
            pos.x = pos.x + 1
            return pos
        elif pos == 2:
            pos.y = pos.y + 1
            return pos
        elif pos == 3:
            pos.x = pos.x - 1
            return pos
                
    def setChar(self, char):
        self.char = char

    def setMaxConnections(self, maxConnections):
        self.maxConnections = maxConnections

    def getMaxConnections(self):
        return self.maxConnections

    def __str__(self):
        return '| x: {:4} | y: {:4} | Nodetype: {} |'.format(self.x, self.y, self.nodeType)

class NetNodeType:
    def __self__(self):
        self.connections = 0
        self.name = ""
        self.allowedNodes = []

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setPosition(self, x, y):
        self.x = x
        self.y = y