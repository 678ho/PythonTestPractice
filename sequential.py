def sequential_search(n, target, array) :
    for i in range(n) :
        if array[i] == target :
            return i + 1

inputData = input().split()
n = int(inputData[0])
target = inputData[1]

array = input().split()

print(sequential_search(n,target,array))