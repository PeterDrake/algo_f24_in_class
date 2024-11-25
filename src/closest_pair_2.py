import math


def clos_pair_bruteforce(points):
    if len(points) < 2:
        raise ValueError("2 points")
    clos_pair = None
    min_distance = float('inf')
    #compare the parove sad
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            #distance
            p1, p2 = points[i], points[j]
            distance = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
            #update if better if found
            if distance < min_distance:
                min_distance = distance
                clos_pair = (p1, p2)
    return clos_pair, min_distance
