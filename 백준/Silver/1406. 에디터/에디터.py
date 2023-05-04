import sys

#양방향 연결리스트 생성
class linklist:
    def __init__(self):
        self.data = None;
        self.pre = None;
        self.next = None;
        
#현재 current위치 출력        
def printCurrent(current):
    print(current.data);
        
#전체 연결리스트 출력
def printlist(root):
    current = root.next;
    print(current.data, end= "");
    while current.next!=None:
        current = current.next;
        print(current.data, end = "")
        
#노드 추가하기        
def addNode(current, alp):
    node = linklist();
    node.data = alp;
    
    #노드 끝 부분일때
    if current.next == None:
        # print("current.next == None");
        current.next = node;
        node.pre = current;
    #노드 처음~중간 부분일 때
    else:
        nxt = current.next;

        current.next = node;
        node.pre = current;

        nxt.pre = node;
        node.next = nxt;

    current = node;
    return current;

#current 를 한 칸 왼쪽으로 옮기기
def leftMove(current):
    if current.pre == None:
        return current;
    current = current.pre;
    return current;

#current 를 한 칸 오른쪽으로 옮기기
def rightMove(current):
    if current.next == None:
        return current;
    current = current.next;
    return current;

#노드 삭제
def deleteNode(current):
    global root;
    if current == root:
        return current;
    elif current.next ==None:
        pre = current.pre;
        pre.next = None;
        current.pre = None;
        return pre;
    else:
        pre = current.pre;
        next = current.next;
        
        pre.next = current.next;
        next.pre = current.pre;
        current.pre = None;
        current.next = None;
        return pre;
        
    
    




current = None;
pre = None;

string = sys.stdin.readline().rstrip();
start = linklist();
root = start;


node = linklist();
node.data = string[0];
node.pre = start;
start.next = node;
current = node;




for i in string[1:]:
    node = linklist();
    node.data = i;
    
    pre = current;
    current = node;
    
    pre.next = current;
    current.pre = pre;


repeat = int(sys.stdin.readline().rstrip())
# printCurrent(current)

for i in range(repeat):
    order = list(map(str,sys.stdin.readline().split()))
    
    if order[0] == "L":
        current = leftMove(current);
        # printCurrent(current);
    elif order[0] == "P":
        current = addNode(current, order[1]);
        # printlist(root);
        # printCurrent(current);
    elif order[0] == "B":
        current = deleteNode(current);
        # printCurrent(current);
    elif order[0] == "D":
        current = rightMove(current);
        # printCurrent(current);


    
printlist(root);

