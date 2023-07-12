import sys;
def printArray(array):
    for i in range(1, len(array)):
        print(f"{i} --> {array[i]}")
n = int(sys.stdin.readline().rstrip());
m = [0] * (n+2);
t = [0] * (n+2);
p = [0] * (n+2);

for i in range(1, n+1):
    t[i], p[i] = map(int, sys.stdin.readline().split());

for i in range(1, n+1):
    time = t[i];
    try:
        m[i+time] =max(p[i] + m[i], m[i+time]);
        for j in range(i+time+1, n+2):
            if m[j] <m[i+time]:
                m[j] = m[i+time]
        # print(m[i+time])
    except:
        pass;
# printArray(m)
print(m[-1])