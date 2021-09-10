# def binary_search(array, target, start, end) :
#     while start <= end :
#         mid = (start+end)//2

#         if array[mid] == target :
#             return mid
#         elif array[mid] > target :
#             end = mid -1
#         else :
#             start = mid + 1
#     return None


# inputNum = int(input())
# k = list(map(int,input().split()))
# k.sort()

# inputNum1 = int(input())

# l = list(map(int,input().split()))
# l.sort()

# for i in l :
#     result = binary_search(k,i,0,inputNum - 1)
#     if result != None :
#         print('yes', end=' ')
#     else :
#         print('no',end=' ')

n = int(input())
array = [0] * 1000001

for i in input().split() :
    array[int(i)] = 1

m = int(input())
x = list(map(int,input().split()))

for i in x :
    if array[i] == 1 :
        print('yes', end=' ')
    else :
        print('no', end='')