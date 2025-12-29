import math

def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
points = [
    (1, 2),
    (2, 2),
    (8, 8),
    (9, 8)
]
clusters = [[p] for p in points]
def cluster_distance(c1, c2):
    min_dist = float("inf")
    for p1 in c1:
        for p2 in c2:
            d = euclidean(p1, p2)
            if d < min_dist:
                min_dist = d
    return min_dist
def find_closest_clusters(clusters):
    min_dist = float("inf")
    pair = (0, 1)

    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            d = cluster_distance(clusters[i], clusters[j])
            if d < min_dist:
                min_dist = d
                pair = (i, j)

    return pair


while len(clusters) > 1:
    i, j = find_closest_clusters(clusters)

    print(f"Merging {clusters[i]} and {clusters[j]}")

    new_cluster = clusters[i] + clusters[j]

    clusters.pop(j)
    clusters.pop(i)

    clusters.append(new_cluster)
