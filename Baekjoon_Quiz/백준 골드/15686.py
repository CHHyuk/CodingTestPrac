from itertools import combinations

n, m = map(int, input().split())
city_map = []
chickens = []
houses = []

for r in range(n):
    row = list(map(int,input().split()))
    city_map.append(row)
    for c, cell in enumerate(row):
        if cell == 1:
            houses.append((r,c))
        elif cell == 2:
            chickens.append((r,c))

def distance(city_map, chickens, selected_chickens):
    chicken_distance_sum = 0
    for house_r, house_c in city_map:
        min_distance = float('inf')
        for chicken_r, chicken_c in selected_chickens:
            distance = abs(house_r - chicken_r) + abs(house_c - chicken_c)
            min_distance = min(min_distance, distance)
        chicken_distance_sum += min_distance
    return chicken_distance_sum

min_chickens_distance = float('inf')
for selected_chickens in combinations(chickens, m):
    min_chickens_distance = min(min_chickens_distance, distance(city_map, chickens, selected_chickens))

print(min_chickens_distance)