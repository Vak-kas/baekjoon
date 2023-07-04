import sys;
from collections import deque;
queue = deque();


def push(x):
    queue.append(x);
    
def pop():
    if len(queue) == 0:
        return -1
    tmp = queue.popleft();
    return tmp;

def front():
    if len(queue) == 0:
        return -1
    return queue[0];
    
def back():
    if len(queue) == 0:
        return -1
    return queue[-1];

def empty():
    if len(queue) == 0:
        return 1;
    else:
        return 0;
    
def size():
    return len(queue);

n = int(sys.stdin.readline().rstrip());
for i in range(n):
    order = list(map(str, sys.stdin.readline().split()));
    
    if order[0] == "push":
        push(order[1]);
    elif order[0] == "pop":
        print(pop());
    elif order[0] == "size":
        print(size());
    elif order[0] == "empty":
        print(empty());
    elif order[0] == "front":
        print(front());
    elif order[0] == "back":
        print(back());
    
