import sys

n = int(sys.stdin.readline().rstrip());

for i in range(1, n+1):
    score = list(map(int, sys.stdin.readline().split()));
    del score[0];
    
    score.sort(reverse=True);
    gap = [];
    for j in  range(len(score)-1):
        gap.append(abs(score[j] - score[j+1]))
    
    print(f"Class {i}")
        
    print(f"Max {score[0]}, Min {score[-1]}, Largest gap {max(gap)}")