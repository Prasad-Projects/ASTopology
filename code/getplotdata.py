# gets the edgelist with edge rgb and alpha values
# gets the nodelist with node-size and rgb values 
# requires outdegree,radius,angle,edgelist_dir files
# usage : python getplotdata.py <year> <month> <day> <time>

import sys
import math

path="../data/"+"/".join(sys.argv[1:])
outdegree_path=path+"/outdegree"
radius_path=path+"/radius"
angle_path=path+"/angle"
nodelist_path=path+"/nodelist"
edgelist_dir_path=path+"/edgelist_dir"
edgelist_path=path+"/edgelist"

outdegree_hash={}
maxoutdegree=-1
with open(outdegree_path) as outdegree_file:
	for x in map(str.strip,outdegree_file.readlines()):
		asn,outdegree=x.split(" ")
		asn=int(asn)
		outdegree=int(outdegree)
		outdegree_hash[asn]=outdegree
		if outdegree>maxoutdegree:
			maxoutdegree=outdegree

print maxoutdegree
print float(1)/(1+maxoutdegree)

width_2=1024/2
maxradius=1-math.log(float(1)/(1+maxoutdegree))

radius_hash={}
with open(radius_path) as radius_file:
	for x in map(str.strip,radius_file.readlines()):
		asn,radius=x.split(" ")
		asn=int(asn)
		radius=float(radius)
		radius_hash[asn]=radius

angle_hash={}
with open(angle_path) as angle_file:
	for x in map(str.strip,angle_file.readlines()):
		asn,angle=x.split(" ")
		asn=int(asn)
		angle=float(angle)
		angle_hash[asn]=math.radians(angle)
		
x_hash={}
y_hash={}
ns_hash={}
for asn in radius_hash:
	radius=radius_hash[asn]
	angle=angle_hash[asn]
	outdegree=outdegree_hash[asn]
	x_hash[asn]=(width_2*(radius/maxradius)*math.cos(angle))+width_2
	y_hash[asn]=-(width_2*(radius/maxradius)*math.sin(angle))+width_2
	ns_hash[asn]=(0.0019*outdegree)+2
	#TO-DO: red_hash, green_hash, blue_hash

nodelist_file=open(nodelist_path,"w")
for asn in radius_hash:
	data=map(str,[asn,x_hash[asn],y_hash[asn],ns_hash[asn],0.0,0.0,0.0])
	nodelist_file.write(" ".join(data)+"\n")
nodelist_file.close()



# Edgelist

def edge_rgba(asn1,asn2):
	if outdegree_hash[asn1]<=15 or outdegree_hash[asn2]<=15:
		return "0.5372 0.8118 0.902 0.1"
	if (outdegree_hash[asn1]<=300 and outdegree_hash[asn1]>15) or (outdegree_hash[asn2]<=300 and outdegree_hash[asn2]>15):
		return "0.0 0.0 1.0 0.25"
	if outdegree_hash[asn1]>300 or outdegree_hash[asn2]>300:
		return "1.0 0.0 0.0 0.9"

edgelist_dir=[]
with open(edgelist_dir_path) as edgelist_dir_file:
	for x in map(str.strip,edgelist_dir_file.readlines()):
		asn1,asn2=map(int,x.split(" "))
		edgelist_dir.append((asn1,asn2))

edgelist_file=open(edgelist_path,"w")
for edge in edgelist_dir:
	asn1=edge[0]
	asn2=edge[1]
	data=map(str,[asn1,x_hash[asn1],y_hash[asn1],asn2,x_hash[asn2],y_hash[asn2],edge_rgba(asn1,asn2)])
	edgelist_file.write(" ".join(data)+"\n")
edgelist_file.close()
