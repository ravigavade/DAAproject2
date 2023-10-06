import random

def pareto_optimal_staircase(P):
    if len(P) <= 2:
        return P

    P.sort(key=lambda point: (-point[1], point[0]))
    pareto_optimal = [P[0]]
    max_x = P[0][0]

    for i in range(1, len(P)):
        if P[i][0] > max_x:
            pareto_optimal.append(P[i])
            max_x = P[i][0]
            
    return pareto_optimal

def generate_random_points(n):
    max_coordinate = 100
    points = [(random.randint(1, max_coordinate), random.randint(1, max_coordinate)) for _ in range(n)]
    return points

n_values = [10,100,1000,10000,100000]

for n in n_values:
    points = generate_random_points(n)
    sorted_staircase = pareto_optimal_staircase(points)
    print(f"For n = {n}, top-right staircase of Pareto-optimal points:")
    for point in sorted_staircase:
        print(point)
    print()
