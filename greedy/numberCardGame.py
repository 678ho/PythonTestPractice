# 숫자가 쓰인 카드들이 N * M 형태로 놓여있다.( N = 행(가로), M = 열(세로))
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽀아야 한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽀을것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야한다.
#
# 3     1     2    
# 4     1     4
# 2     2     2
#
# (1 <= N,M <= 100)
# 둘째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
from random import randint
n,m = map(int,input().split())

result = 0

for i in range(n) :
    data = list(map(int,input().split()))
    minValue = randint(1,100)
    for a in data :
        minValue = min(minValue,a)
    result = max(result, minValue)

print(result)
