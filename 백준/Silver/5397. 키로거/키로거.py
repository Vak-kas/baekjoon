import sys;

#연결리스트 클래스 생성
class LinkList:
    def __init__ (self):
        self.data = None;
        self.prev = None;
        self.next = None;

class testPassword:
    def __init__(self, password):
        self.password = password;
        self.start = LinkList();
        self.root = self.start;
        self.current = None;

        
    
    
    def makeLink(self):
        node = LinkList();
        idx = 0;
        while idx<len(self.password):
            if (self.password[idx] =="<") or (self.password[idx]==">") or (self.password[idx] == "-"):
                idx+=1;
            else:
                node.data = self.password[idx];
                # print(node.data);
                break;
        self.current = node;
        self.root.next = node;
        node.prev = self.start;

                
                
        for i in self.password[idx+1:]:
            if i =="<":
                self.leftMove();
            elif i==">":
                self.rightMove();
            elif i=="-":
                self.deleteNode();
            else:
                self.addNode(i);
    
    def leftMove(self):
        # self.printCurrent();
        if self.current.prev ==None:
            return;
        self.current = self.current.prev;
    
    def rightMove(self):
        # self.printCurrent();
        if self.current.next == None:
            return;
        self.current = self.current.next;
    
    def deleteNode(self):
        # self.printCurrent();
        #현재 커서 위치가 제일 앞인 경우
        if self.current.data == None:
            return
        
        # 현재 다음에 연결된 노드가 없는 경우
        elif self.current.next ==None:
            prev = self.current.prev;
            prev.next = None;
            self.current.prev = None;
            self.current = prev;
        #나머지 일반적인 경우
        else:
            prev = self.current.prev;
            next = self.current.next;
            prev.next = self.current.next;
            next.prev = self.current.prev;
            self.current.prev = None;
            self.current.next = None;
            self.current = prev;
    
    def addNode(self, data):
        # self.printCurrent();
        if self.current.next ==None:
            node = LinkList();
            node.data = data;
            self.current.next = node;
            node.prev = self.current; 
            self.current = node;
        else:
            node = LinkList();
            node.data = data;
            next = self.current.next;
            node.next = next;
            node.prev = self.current;
            self.current.next = node;
            next.prev = node;
            self.current = node;
            
    #루트+1부터 전체 노드 데이터 출력
    def printList(self):
        if self.root.next==None:
            return;
        current = self.root.next;
        print(current.data, end= "");
        while current.next!=None:
            current = current.next;
            print(current.data, end= "");
    #현재 노드 출력            
    def printCurrent(self):
        print(self.current.data);
    
    
        

        
        
# 메인
if __name__ == "__main__":
    n = int(sys.stdin.readline().rstrip());
    
    for i in range(n):
        string = sys.stdin.readline().rstrip();
        a = testPassword(string);
        a.makeLink()
        a.printList();
        print();
        
    
    
    
    

        
        