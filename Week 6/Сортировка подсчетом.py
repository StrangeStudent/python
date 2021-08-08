def CountSort(A):
    MyLine = []
    NewList = [0] * (max(A) + 1)
    for i in A:
        NewList[i] += 1
    for now in range(len(NewList)):
        if NewList[now] != 0:
            for i in range(NewList[now]):
                MyLine.append(now)
    return MyLine


MyList = list(map(int, input().split()))

Onemorelist = CountSort(MyList)
print(*Onemorelist)
