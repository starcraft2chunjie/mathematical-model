from collections import defaultdict
from random import uniform
from math import sqrt

def distence(a, b):
    dimensions = len(a)
    _sum = 0
    for dimension in range(dimensions):
        dif = (a[dimension] - b[dimension]) ** 2
        _sum += dif
    return sqrt(_sum) 


def point_avg(points):
    """
        Returns a new point which is the center of all the points.
    """
    dimensions = len(points[0])

    new_center = []

    for dimension in range(dimensions):
        dim_sum = 0 # dimension sum
        for p in points:
            dim_sum += p[dimension]
        
        # average of each dimension
        new_center.append(dim_sum / float(len(points)))

    return new_center

def generate_k(data_set, k):
    """
    
    """
    centers = []
    dimensions = len(data_set[0])
    min_max = defaultdict(int)

    for point in data_set:
        for i in range(dimensions):
            val = point[i]
            min_key = 'min_%d' % i
            max_key = 'max_%d' % i
            if min_key not in min_max or val < min_max[min_key]:
                min_max[min_key] = val
            if min_key not in min_max or val > min_max[max_key]:
                min_max[max_key] = val

    for _k in range(k):
        rand_point = []
        for i in range(dimensions):
            min_val = min_max['min_%d' % i]
            max_val = min_max['max_%d' % i]

            rand_point.append(uniform(min_val, max_val))
        
        centers.append(rand_point)
    
    return centers



def assign_points(data_set, centers):
    assignments = []
    for point in data_set:
        shortest = 100000 # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distence(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments



def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers where `k` is the number of unique assignments.
    """

    new_means = defaultdict(list)
    centers = []
    for assignment, point in zip(assignments, data_set):
        new_means[assignment].append(point)
    for key, points in new_means.items():
        centers.append(point_avg(points))
    
    return centers


def k_means(data_set, k):
    centers = generate_k(data_set, k)
    assignments = assign_points(data_set, centers)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(data_set, assignments)
        old_assignments = assignments
        assignments = assign_points(data_set, new_centers)
    
    return assignments, data_set

# points = [
#     [1, 2],
#     [2, 1],
#     [3, 1],
#     [5, 4],
#     [5, 5],
#     [6, 5],
#     [10, 8],
#     [7, 9],
#     [11, 5],
#     [14, 9],
#     [14, 14],
#     ]
# assignments, data_sets = k_means(points, 3)
# print(assignments)


