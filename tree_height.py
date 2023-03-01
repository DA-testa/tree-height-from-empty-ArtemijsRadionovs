# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    heights = [0]*n
    
    max_height = 0
    # Your code here
    for i in range(n):
        node_height = 0
        parent = parents[i]
        while parent != - 1:
            node_height += 1
            parent = parents[parent]
    max_height = max(heights)
    
    return max_height


def main():
    # implement input form keyboard and from files
    check_for_I = input().upper() 
    
    if check_for_I == "I":
        n = int(input().strip())
        parents = list(map(int, input().split()))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision    
        
    elif check_for_I == "F":
        file_name = input().strip()
        if 'a' in file_name:
            print("File name cannot contain letter 'a'!")
        try:
            with open('test/' + file_name, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found!")
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
