#Task 27-01
import turtle as t

#t.tracer(0)
#t.done()
#t.lt(90)
#k = 10

from math import *

file = [i[:-1].split(';') for i in open('27var1A.csv')]
data = []
for j in file:
    data1 = []
    for i in range(len(j)-1):
        #эти числа надо как-то интовать
        num1 = float(j[i].replace(',', '.'))
        num2 = float(j[i + 1].replace(',', '.'))
        print(num1, num2)
        data.append([num1, num2])
#print(data)

#t.up()
#for p in file:
 #   t.setpos(p[0] * k, p[1] * k)
  #  t.dot(2)

def clusterization(data):
    eps = 1.5
    clusters = []
    while data:
        el = data.pop()
        clusters.append([el])
        for p in clusters[-1]:
            neighbours = [pt for pt in data if dist(p, pt) < eps]
            clusters[-1] += neighbours
            for pt in neighbours:
                data.remove(pt)
    return clusters

def centers(clusters):
    cent = []
    for cl in clusters:
        d_min = 1000000
        c = [0, 0]
        for p in cl:
            d = sum([dist(p, pt) for pt in cl])
            if d < d_min:
                d_min = d
                c = p
        cent.append(c)
    return cent

#print(centers(clusterization(data)))
clusters = clusterization(data)
cent = centers(clusters)
Px = int(abs(sum(p[0] for p in cent) / len(cent)) * 10000)
Py = int(abs(sum(p[1] for p in cent) / len(cent)) * 10000)
print(Px, Py)
