n,k = map(int,input().split())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))

array1 = sorted(array1)
array2 = sorted(array2,reverse=True)
result = 0
for i in range(k) :
    if array1[i] < array2[i] :
        array1[i], array2[i] = array2[i], array1[i]

for j in range(n) :
    result += array1[j]

print(result)