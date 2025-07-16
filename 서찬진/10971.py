import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

min_cost = float('inf')

cities = [i for i in range(1, n)]  # 0번 도시 고정

for route in permutations(cities):
    cost = 0
    current = 0  # 출발 도시는 항상 0번

    valid = True

    for next_city in route:
        if w[current][next_city] == 0:
            valid = False
            break
        cost += w[current][next_city]
        current = next_city

    # 마지막 도시에서 다시 출발 도시(0번)으로 돌아오기
    if valid and w[current][0] != 0:
        cost += w[current][0]
        min_cost = min(min_cost, cost)

print(min_cost)