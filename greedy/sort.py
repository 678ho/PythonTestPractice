stdNum = int(input())

array = []

for i in range(stdNum) :
    inputData = input().split()
    array.append((inputData[0],inputData[1]))


array = sorted(array)

for i in range(stdNum) :
    print(array[i][0],end=' ')

