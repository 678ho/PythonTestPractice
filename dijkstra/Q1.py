# 입력조건 
#    첫째 줄에 전체 회사의 개수 N과 경로 M이 공백으로 구분되어 차례대로 주어진다.
#    둘째 줄부터 M+1번째 줄에는 연결된 두 회사의 번호가 공백으로 구분되어 주어진다.
#    M+2번째 줄에는 X와 K가 공백으로 구분되어 차례대로 주어진다.
# 출력조건
#    첫째 줄에 방문 판매원 A가 K번 회사를 거쳐 X번 회사로 가는 최소 이동 시간을 출력한다.
#    만약 X번 회사에 도달할 수 없다면 -1을 출력한다.

INF = int(1e9)

n, m = map(int, input().split())

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1) :
    for b in range(1,n+1) :
        if a==b :
            graph[a][b] = 0

for _ in range(m) :
    a,b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1) :
    for a in range(1, n+1) :
        for b in range(1, n+1) :
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF :
    print("-1")
else:
    print(distance)
