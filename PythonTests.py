ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

data = ONE_TEN

createdList = []

for i in range(0, len(data), 1):
    if data[i] % 2 == 0:
        createdList.append(data[i])

for i in range(0, len(data), 1):
    if data[i] % 2 != 0:
        createdList.append(data[i])

print(createdList)