# 첫째 줄에 N( 2 <= N <= 10000), M( 1<= M <= 10000), K( 1<= K <= 10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘쨰 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1이상 10000이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
#  (N = 배열의 크기, M = 더해지는 횟수, K = K번째 원소 선택)
# 출력 조건 : 큰 수의 법칙에 따라 더해진 답을 출력한다.
n,m,k = map(int,input().split())

data = list(map(int,input().split()))

# print(" 배열의 크기 : ",n,"\n","더해지는 횟수",m,"\n","first k번 더하고 second한번",k)
# print("주어진 데이터 ",data)

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

while True :
    for i in range(k) :
        if m == 0 :
            break
        result = result + first
        m -= 1
        print("m : ",m,"result : ", result)
    if m == 0 :
        break
    result = result + second
    m -= 1
    print("m : ",m,"result : ",result)