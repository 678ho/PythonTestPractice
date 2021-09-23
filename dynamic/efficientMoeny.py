# N종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고한다.
# 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
#
# 입력조건 : 첫째줄에 N, M이 주어진다 ( 1<= N <= 100, 1 <= M <= 10000)
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다.
#
# 출력조건 : 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다
# (불가능한 경우에는 -1을 출력한다.)
#

n,m = map(int,input().split())

nMoney = []

for i in range(n):
    nMoney.append(int(input()))

d = [10001] * (m+1)
d[0] = 0

for i in range(n) :
    for j in range(nMoney[i], m + 1) :
        if d[j - nMoney[i]] != 10001 :
            d[j] = min(d[j], d[j - nMoney[i]] + 1)

if d[m] == 10001 :
    print(-1)

else:
    print(d[m])

