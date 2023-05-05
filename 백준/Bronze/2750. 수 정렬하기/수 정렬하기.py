import sys;

# def quickSort(ary):
    #퀵정렬 1
    # n = len(ary);
    # if n<=1:
    #     return ary;
    
    # pivot = ary[n//2];
    # leftAry , rightAry = [], [];
    # midAry = [];
    
    # for i in ary:
    #     if i < pivot:
    #         leftAry.append(i);
    #     elif i>pivot:
    #         rightAry.append(i);
    #     else:
    #         midAry.append(i);
            
    # return quickSort(leftAry) + midAry + quickSort(rightAry);
    
def quickSort(ary, start, end):
    if end<=start:
        return

    low = start;
    high = end;
    #퀵정렬 2
    n = len(ary);

    pivot = ary[(low+high)//2]

    while low<=high:
        while ary[low]<pivot:
            low+=1;
        while ary[high]>pivot:
            high-=1;

        if low<=high:
            ary[low], ary[high] = ary[high], ary[low];
            low+=1;
            high-=1;

    mid =low;

    quickSort(ary, start, mid-1);
    quickSort(ary, mid, end);
        
        
def QS(ary):
    quickSort(ary, 0, len(ary)-1);
        
        


n = int(sys.stdin.readline().rstrip());
lst = [];

for i in range(n):
    tmp = int(sys.stdin.readline().rstrip());
    lst.append(tmp);
    
QS(lst);
# print(lst);

#버블 정렬 1
# for i in range(n-1):
#     for j in range(n-1-i):
#         if lst[j]>lst[j+1] :
#             lst[j], lst[j+1] = lst[j+1], lst[j];

# #버블 정렬 2
# for end in range(n-1, 0, -1):
#     is_change = False;
#     for j in range(0, end):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j];
#             is_change =True;
            
#     if not is_change:
#         break;

#퀵정렬 1
# lst = (quickSort(lst));



        
            
for i in lst:
    print(i);