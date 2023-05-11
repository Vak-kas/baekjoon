import sys;
from itertools import combinations


n, m = map(int, sys.stdin.readline().split());

array = list(map(int, sys.stdin.readline().split()));
max_value = -1;
for card in combinations(array, 3):
    tmp = sum(card);
    if tmp <=m and tmp>max_value:
        max_value = tmp;
        
print(max_value);
    
    
            
    
