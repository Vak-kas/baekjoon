import sys;
sys.setrecursionlimit(100000);

def find(a):
    global parent;
    if parent[a] == a:
        return a;
    else:
        parent[a] = find(parent[a]);
        return parent[a]
    
def union(a, b):
    a = find(a);
    b = find(b);
    
    if a>b:
        a, b = b, a;
        
    parent[b] = a;

if __name__ == "__main__":
    people, party = map(int, sys.stdin.readline().split());
    know = list(map(int, sys.stdin.readline().split()));
    parent = [i for i in range(people+1)]
    know_list = [];
    party_list = [];
     
    if len(know) == 1:
        pass;
    else:
        for i in know[1:]:
            know_list.append(i);
    
    for i in range(party):
        lst = list(map(int, sys.stdin.readline().split()))
        if lst[0] == 1:
            party_list.append([lst[1]])
        else:
            index = 1;
            for j in range(2, len(lst)):
                union(lst[index], lst[j])
            
            party_list.append(lst[1:])
                
#     print(know_list)
#     print(parent);
#     print(party_list);
    
    for i in range(len(know_list)):
        know_list[i] = find(know_list[i])
        
    
    count = 0;
    
    for i in range(len(party_list)):
        flag = True;
        for j in party_list[i]:
            if find(j) in know_list:
                # print(f"레벨업 실패 {j}, {find(j)}")
                flag = False
                break;
        if flag:
            count+=1;
            
    print(count);
            
                
                
            
                
                
        
    