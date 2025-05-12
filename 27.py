file = open('A.txt')
cluster_1, cluster_2 = [], []
for line in file:
    x, y = map(float, line.replace(',', '.').split())
    if 2 <= x <= 6 and 5 <= y <= 10:
        cluster_1.append((x, y))
    if 4 <= x <= 8 and 20 <= y <= 30:
        cluster_2.append((x, y))

def centroids(cluster):
    x_centr, y_centr, minimum = 0, 0, 10*100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
        if res < minimum:
            minimum = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

x1, y1 = centroids(cluster_1)
x2, y2 = centroids(cluster_2)
result_A = ( (x1 + x2) / 2 * 10000, (y1 + y2) / 2 * 10000 )
print(result_A)


file = open('B.txt')
cluster_1, cluster_2, cluster_3 = [], [], []
for line in file:
    x, y = map(float, line.replace(',', '.').split())
    if -10 <= x <= -4 and 0 <= y <= 4:
        cluster_1.append((x, y))
    if 4 <= x <= 8 and 2 <= y <= 4:
        cluster_2.append((x, y))
    if 2 <= x <= 6 and 8 <= y <= 12:
        cluster_3.append((x, y))

def centroids(cluster):
    x_centr, y_centr, minimum = 0, 0, 10*100
    for i in range(len(cluster)):
        res = 0
        for j in range(len(cluster)):
            x1, y1 = cluster[i]
            x2, y2 = cluster[j]
            res += ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
        if res < minimum:
            minimum = res
            x_centr, y_centr = x1, y1
    return x_centr, y_centr

x1, y1 = centroids(cluster_1)
x2, y2 = centroids(cluster_2)
x3, y3 = centroids(cluster_3)
result_B = ( (x1 + x2 + x3) / 3 * 10000, (y1 + y2 + y3) / 3 * 10000 )
print(result_B)


#47817 162912
#10895 45618
