import sys;

sentence = list(sys.stdin.readline().rstrip().split("-"));

for i in range(len(sentence)):
    tmp = list(sentence[i].split("+"))
    # print(tmp)
    for j in range(len(tmp)):
        tmp[j] = int(tmp[j]);
        
    s = sum(tmp);
    sentence[i] = s;
    
        
    
start = sentence[0];
if len(sentence) == 1:
    print(start);
else:
    for i in sentence[1:]:
        start -=int(i);
    print(start);
        
    
    