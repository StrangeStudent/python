n = int(input())
PressCount = list(map(int, input().split()))
CommonPress = int(input())
RangePress = list(map(int, input().split()))
NewList = [0] * (max(RangePress) + 1)
for i in RangePress:
    NewList[i] += 1
for i in range(n):
    if PressCount[i] < NewList[i+1]:
        print('YES')
    else:
        print('NO')
