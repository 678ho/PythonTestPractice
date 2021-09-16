# 정수 n가 주어질 떄 사용할 수 있는 연산은 다음과 같이 4가지이다.
#   1. n가 5로 나누어떨어지면, 5로 나눈다.
#   2. n가 3으로 나누어떨어지면, 3으로 나눈다.
#   3. n가 2로 나누어떨어지면, 2로 나눈다.
#   4. n에서 1을 뺀다.
#

n = int(input())

d = [0] * 30001

for i in range(2,n+1):
    d[i] = d[i-1] + 1
    
    if i % 2 == 0 :
        d[i] = min(d[i], d[i // 2] + 1)
        print(d[i], end=' ')
    if i % 3 == 0 :
        d[i] = min(d[i], d[i // 3] + 1)
        print(d[i], end=' ')
    if i % 5 == 0 :
        d[i] = min(d[i], d[i // 5 + 1])
        print(d[i], end=' ')
print(d[n])