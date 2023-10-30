import sys;

def preOrder(node):
    if node == None:
        return;
    
    print(node, end="");
    preOrder(edgeList[node][0]);
    preOrder(edgeList[node][1]);
    
def inOrder(node):
    if node == None:
        return;
    
    inOrder(edgeList[node][0]);
    print(node, end= "");
    inOrder(edgeList[node][1]);
    
def postOrder(node):
    if node == None:
        return;
    
    postOrder(edgeList[node][0]);
    postOrder(edgeList[node][1]);
    print(node, end="");
    
    
n = int(sys.stdin.readline().rstrip());
edgeList = {};
for i in range(n):
    parent, left, right = sys.stdin.readline().split();
    edgeList[parent] = [None, None];
    
    if left == ".":
        pass;
    else:
        edgeList[parent][0] = left;
    
    if right == ".":
        pass;
    else:
        edgeList[parent][1] = right;
        
# print(edgeList);

preOrder("A");
print();
inOrder("A");
print();
postOrder("A");
print();



    