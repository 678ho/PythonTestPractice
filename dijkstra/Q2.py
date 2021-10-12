# 입력 조건 : 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다
#            둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다.
#               (특정도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 뜻.)
#
# 출력 조건 : 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline

n, m, c = map(int, input().split())

graph = [[]*(n+1) for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m) :
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(c) :
    q = []
    heapq.heappush(q,(0,c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
        if cost < distance[i[0]] :
            distance[i[0]] = cost
            heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count = 0

max_distance = 0
for d in distance :
    if d != INF :
        count += 1
        max_distance = max(max_distance, d)
print(count -1, max_distance)