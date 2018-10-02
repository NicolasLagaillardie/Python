import os
from  random  import randrange
m=input("m=")
m=int(m)
t=[]
for k in range(0,m+1):
     t.extend([randrange(2)])
for k in range(0,m):
	i=0
	while t[i]==1:
		t[i]=0
		i=i+1
	t[i]=1
	print (t)
os.system("pause")
