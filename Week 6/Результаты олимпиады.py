n = int(input())
participants = []
for i in range(n):
    ktemp = input().split()
    k = ((ktemp[0]), int(ktemp[1]))
    participants.append(k)
sorted_list = sorted(participants, key=lambda x: x[1])
for i in reversed(sorted_list):
    print(i[0])
