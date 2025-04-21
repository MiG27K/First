#Task-27-02
file_a = [file.split('\t') for file in open('27var2A.txt')]
file = file_a
data = []
for i in file:
    for j in range(len(i) - 1):
        num_x = float(i[j].replace(',', '.'))
        num_y = float(i[j+1].replace(',', '.'))
        data.append([num_x, num_y])

from math import *

def clusterization(data):
    eps = 1.5
    clusters = []
    while data:
        el = data.pop()
        clusters.append([el])
        for p in clusters[-1]:
            neigh = [pt for pt in data if dist(p, pt) < eps]
            clusters[-1] += neigh
            for pt in neigh:
                data.remove(pt)
    return clusters

def centers(clusters):
    centrs = []
    for cluster in clusters:
        distance_min = 10000
        c = [0, 0]
        for p in cluster:
            d = sum([dist(p, pt) for pt in cluster])
            if d < distance_min:
                distance_min = d
                c = p
        centrs.append(c)
        return centrs

clusters = clusterization(data)
centrs = centers(clusters)
Px = int(abs(sum(p[0] for p in centrs) / len(centrs))*10000)
Py = int(abs(sum(p[1] for p in centrs) / len(centrs))*10000)
print(Px, Py)
    
