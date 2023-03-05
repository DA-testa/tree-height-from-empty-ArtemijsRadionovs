# python3

import sys
import threading
import numpy as np


def parseTree(parents, currElem, deepness = 0):
    return_deep = deepness;
    childList = np.where(parents == currElem)[0]
    
    if len(childList) > 0 :
        childDeepness = []
        for i in childList:
            childDeepness.append(parseTree(parents, str(i), deepness+1))
        return_deep = np.max(childDeepness)
    return return_deep

def main():
    # implement input form keyboard and from files
    check_for_I = input().replace('\r','')
    if check_for_I == "I":
        n = int(input())
        parents = np.array(input().split())
        if n < parents.size:
            print("The number of child offspring is higher than it should be!")
            return
        print(parseTree(parents, "-1"))
        
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision    
        
    elif check_for_I == "F":
        file_name = input().replace('\r','')
        if 'a' in file_name:
            print("File name cannot contain letter 'a'!")
            return
        try:
            with open('./test/' + file_name, 'r') as f:
                n = int(f.readline())
                parents = np.array(f.readline().split())
                print(parseTree(parents, "-1"))
        except FileNotFoundError:
            print("File not found!")
            return

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
