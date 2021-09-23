# 가로 N , 세로 2인 직사각형 형태의 얇은 바닥이 있다.
# 이 얇은 바닥을 1*2, 2*1, 2*2 덮개를 이용해 채우고자한다.
# 이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.
# ex) 2 * 3 크기의 바닥을 채우는 경우의 수는 5가지
#
# 입력조건 : 첫째 줄에 N이 주어진다.
# 출력조건 : 2 * N 크기의 바닥을 채우는 방법의 수를 796,796으로 나눈 나머지를 출력한다.


n = int(input())

d = [0] * 1001


d[1] = 1

d[2] = 3

for i in range(3,n+1) :
    d[i] = (d[i-1] + 2*d[i-2])%796796
print(d[n])