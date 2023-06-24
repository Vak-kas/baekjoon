import sys;

sys.setrecursionlimit(10**6)

class TreeNode():
    def __init__(self):
        self.data = None;
        self.left = None;
        self.right = None;
        
def postOrder(current):
    if current == None:
        return;
    postOrder(current.left);
    postOrder(current.right);
    print(current.data);

n = int(sys.stdin.readline().rstrip());

node = TreeNode();
node.data = n;
root = node;
lst = []
while True:
    try:
        lst.append(int(sys.stdin.readline()));
    except:
        break;
    
    
    
for k in lst:

    node = TreeNode();
    node.data = k;
    
    current = root;
    

    while True:
        if k > current.data:
            if current.right ==None:
                current.right = node;
                break;
            else:
                current = current.right;
        else:
            if current.left ==None:
                current.left = node;
                break;
            else:
                current = current.left;

postOrder(root);
    
