def findmax(finder):
    return finder.count(max(finder))


nine, ten, eleven = [], [], []
f = open('input.txt', 'r', encoding='utf-8')
for i in f:
    line = list(i.split())
    if line[2] == '9':
        nine.append(int(line[3]))
    elif line[2] == '10':
        ten.append(int(line[3]))
    elif line[2] == '11':
        eleven.append(int(line[3]))
print(findmax(nine), findmax(ten), findmax(eleven))
f.close()
