#Task 27-01
file = open('27var1A.csv')
lst = []
for s in file:
    #print(s)
    pair = s.split(';')
    pair[0] = float(pair[0].replace(',', '.'))
    pair[1] = float(pair[1][:-1].replace(',', '.'))
    #print(pair)
    lst.append(pair)

import math

def distance(P1, P2):
    return math.sqrt((P2[0] - P1[0])**2 + (P2[1] - P1[1])**2)

N = len(lst)
labels = [0 for i in range(N)]

def update_clusters(arr, labels, C1, C2):
    N = len(arr)
    for i in range(N):
        P = arr[i]
        distance_1 = distance(P, C1)
        distance_2 = distance(P, C2)
        if distance_1 < distance_2:
            labels[i] = 0
        else:
            labels[i] = 1
        return labels

def find_centers(arr, labels):
    x0, y0, x1, y1 = 0, 0, 0, 0
    count0 = 0
    count1 = 0
    for i in range(N):
        if labels[i] == 0:
            count0 += 1
            x0 += arr[i][0]
            y0 += arr[i][1]
        else:
            count1 += 1
            x1 += arr[i][0]
            y1 += arr[i][1]
    C0 = [x0 / count0, y0 / count0]
    C1 = [x1 / count1, y1 / count1]
    return C1, C0

def clusterization(arr, labels, max_iter):
    C0 = [10, 10]
    C1 = [0, 0]
    for i in range(max_iter):
        labels = update_clusters(arr, labels, C0, C1)
        C0, C1 = find_centers(arr, labels)
    return labels

print(clusterization(lst, labels, 50))
