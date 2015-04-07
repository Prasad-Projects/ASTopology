from math import *
import sys

year=sys.argv[1]
month=sys.argv[2]
day=sys.argv[3]
time=sys.argv[4]
filename1="/home/sourabh/routeviews/complete/data/"+year+"/"+month+"/"+day+"/"+time+"/"+"outdegree"
filename2="/home/sourabh/routeviews/complete/data/"+year+"/"+month+"/"+day+"/"+time+"/"+"radius"

fo=open(filename1)
s=fo.read()
l=s.split("\n")
l.remove("")
fo.close()

radius=[]
outdegree=[]

for i in l:
	temp1=i.split()
	outdegree.append(int(temp1[1]))

outdegree.sort()
maxoutdeg=outdegree[-1]

for i in l:
	temp1=i.split()
	outdeg=int(temp1[1])
	rad=1-log(float(outdeg+1)/(maxoutdeg+1))
	radius.append(temp1[0]+" "+str(rad))

fo=open(filename2,"w+")
for i in radius:
	fo.write(i)
	fo.write("\n")
fo.close()
