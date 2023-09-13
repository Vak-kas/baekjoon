n = int(input()); #전체 개수 입력받기
lst = list(map(int, input().split()));

print(min(lst), end=" ");
print(max(lst));