# -*- coding: utf-8 -*-
from time import time

def f(input, output, indice) :
    if  input[indice][0] in output :
        return []
    else :
        l = [input[indice][0]]
        for i in input[indice][1] :
                l = l + f(input,output + [input[indice][0]],i)
        for i in l :
            if i not in output :
                output = output + [i]
        return output

t = time()

file = open('day12.txt','r')
docint = file.readlines()
doc = []
for i in docint :
    sl = i[:-1].split(' <-> ')
    ssl = sl[1].split(',')
    doc = doc + [[int(sl[0]),[int(j) for j in ssl]]]

print doc
print len(f(doc,[],0))

vus = [i for i in range(0,len(doc))]
group = 0

while vus != [] :
    inte = f(doc,[],vus[0])
    for i in inte :
        vus.remove(i)
    group += 1

print group

print time() - t