import random, time
from SystemMap import *

def test():
    start_time = time.time()
    for i in range(0,10):
        sysMap = SystemMap("Test "+str(i), 10 + (10 *i))
        print(sysMap.__str__())
        # sysMap.printMap()
    elapsed_time = time.time() - start_time
    print('EXEC TIME: {:06.4f} sec'.format(elapsed_time))
test()