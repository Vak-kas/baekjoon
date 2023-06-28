import sys;
dic = {};

input_data, find_data = map(int, sys.stdin.readline().split());

for i in range(input_data):
    link, pw = map(str, sys.stdin.readline().split());
    
    dic[link] = pw;
    
    
    
for i in range(find_data):
    data = sys.stdin.readline().rstrip();
    
    print(dic[data]);