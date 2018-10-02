# -*- coding: utf-8 -*-
from multiprocessing import Pool

pool = Pool(processes=8)

f = open('day131.txt', 'r')
docint = f.readlines()
f.close()

Nlayers = 0

for i in docint:
    Nlayers = max(Nlayers, int(i[:-1].split(': ')[0]))

doc = [0] * (Nlayers + 1)

for i in range(len(docint)):
    inte = docint[i][:-1].split(': ')
    doc[int(inte[0])] = int(inte[1])

r = []


def f(positionS, doc, sens):
    for j in range(len(positionS)):
        if doc[j] != 0:
            if sens[j] == 1 and positionS[j] + 1 > doc[j] - 1:
                positionS[j] -= 1
                sens[j] = -1
            elif sens[j] == -1 and positionS[j] - 1 < 0:
                positionS[j] += 1
                sens[j] = 1
            else:
                positionS[j] += sens[j]
    return positionS, sens


def g(positionS, doc, sens, stop, r):
    for i in range(stop):
        positionS, sens = f(positionS, doc, sens)
    for i in range(Nlayers + 1):
        if positionS[i] == 0:
            r += (doc[i] * i)
        positionS, sens = f(positionS, doc, sens)
    return r


stop = [0, 1, 2, 3, 4, 5, 6, 7]
while 0 not in r:
    positionS = [0] * (Nlayers + 1)
    sens = [1] * (Nlayers + 1)

    result1 = pool.apply_async(g, (positionS, doc, sens, stop[0], 0,))
    r = r + [result1.get(timeout=1)]
    stop[0] += 1
    result2 = pool.apply_async(g, (positionS, doc, sens, stop[1], 0,))
    r = r + [result2.get(timeout=1)]
    stop[1] += 1
    result3 = pool.apply_async(g, (positionS, doc, sens, stop[2], 0,))
    r = r + [result3.get(timeout=1)]
    stop[2] += 1
    result4 = pool.apply_async(g, (positionS, doc, sens, stop[3], 0,))
    r = r + [result4.get(timeout=1)]
    stop[3] += 1
    result5 = pool.apply_async(g, (positionS, doc, sens, stop[4], 0,))
    r = r + [result5.get(timeout=1)]
    stop[4] += 1
    result6 = pool.apply_async(g, (positionS, doc, sens, stop[5], 0,))
    r = r + [result6.get(timeout=1)]
    stop[5] += 1
    result7 = pool.apply_async(g, (positionS, doc, sens, stop[6], 0,))
    r = r + [result7.get(timeout=1)]
    stop[6] += 1
    result8 = pool.apply_async(g, (positionS, doc, sens, stop[7], 0,))
    r = r + [result8.get(timeout=1)]
    stop[7] += 1

print (stop,r[-8:])
