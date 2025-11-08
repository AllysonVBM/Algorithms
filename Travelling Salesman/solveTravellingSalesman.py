import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def generate_permutations(cities):
    if len(cities) == 1:
        return [cities]
    
    permutations = []
    for i in range(len(cities)):
        current_city = cities[i]
        remaining_cities = cities[:i] + cities[i+1:]
        for perm in generate_permutations(remaining_cities):
            permutations.append([current_city] + perm)
    
    return permutations

def calculate_total_distance(route):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += calculate_distance(route[i], route[i+1])
    total_distance += calculate_distance(route[-1], route[0])
    return total_distance

def traveling_salesman(cities):
    routes = generate_permutations(cities)
    min_distance = float('inf')
    best_route = None
    for route in routes:
        route_distance = calculate_total_distance(route)
        if route_distance < min_distance:
            min_distance = route_distance
            best_route = route
    return best_route, min_distance

if __name__ == "__main__":
    cities = [(0, 0), (1, 1), (2, 2), (3, 3)]
    best_route, min_distance = traveling_salesman(cities)
    print("Best route:", best_route)
    print("Minimum distance:", min_distance)
