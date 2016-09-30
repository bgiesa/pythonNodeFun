import random, time
from SystemMap import *

def getConnection(sysMap):
    for i in sysMap.nodes:
        print(i.__str__())
        for j in i.connected:
            print("\t"+j.__str__())

def test():
    start_time = time.time()
    for i in range(0,1):
        sysMap = SystemMap("Test "+str(i), 2, 1)

        print(sysMap.__str__())
        # sysMap.printMap()

    elapsed_time = time.time() - start_time
    print('EXEC TIME: {:06.4f} sec'.format(elapsed_time))
test()