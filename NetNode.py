class NetNode:
    def __init__(self, type):
        self.x = 0
        self.y = 0
        self.type = type
        self.char = ' '
        self.connected = []

    def setPos(self, x, y):
        self.x = x
        self.y = y
    def addConnector(self, node):
        self.connected.append(node)

    def setChar(self, char):
        self.char = char

    def __str__(self):
        return '| x: {:4} | y: {:4} | type: {} |'.format(self.x, self.y, self.type)

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y