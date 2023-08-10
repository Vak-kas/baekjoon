import sys
class sets():
    def __init__(self):
        self.s = set([]);
        
        
    def add(self,x):
        self.s.add(x);
    
    def remove(self,x):
        if x not in self.s:
            return 
        self.s.remove(x);
        
    def check(self, x):
        if x in self.s:
            return 1;
        return 0;
    
    def toggle(self,x):
        if x in self.s:
            self.s.remove(x);
        else:
            self.s.add(x);
            
    def all(self):
        self.s = set(["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"])
        
    def empty(self):
        self.s = set([]);
        
a = sets();
n = int(sys.stdin.readline().rstrip());

for i in range(n):
    order = (sys.stdin.readline().split());
    # print(order[0])
    # print(order[1]);
    # print(order)
    
    if order[0] == "add":
        a.add(order[1]);
    elif order[0] == "check":
        print(a.check(order[1]));
    elif order[0] == "remove":
        (a.remove(order[1]));
    elif order[0] == "toggle":
        (a.toggle(order[1]));
    elif order[0] == "all":
        a.all();
    elif order[0] =="empty":
        a.empty();
    elif order[0] == "print":
        print(a.s)