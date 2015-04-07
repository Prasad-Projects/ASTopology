import sys

path="../data/"+"/".join(sys.argv[1:])

angle_gc_file="../base/gc/angle_gc"
angle_gl_file="../base/gl/angle_gl"

gc_hash={}
with open(angle_gc_file) as gc_file:
	gc_list=map(str.strip,gc_file.readlines())
	for x in gc_list:
		tmp=x.split(" ")
		gc_hash[tmp[0]]=tmp[1]

gl_hash={}
with open(angle_gl_file) as gl_file:
	gl_list=map(str.strip,gl_file.readlines())
	for x in gl_list:
		tmp=x.split(" ")
		gl_hash[tmp[0]]=tmp[1]

angle_hash={}
with open(path+"/asn") as asn_file:
	asn_list=map(str.strip,asn_file.readlines())	 
	for x in asn_list:
		if x in gc_hash:
			angle_hash[x]=gc_hash[x]
		else:
			angle_hash[x]=gl_hash[x]

angle_file=open(path+"/angle","w")
for x in angle_hash:
	angle_file.write(x+" "+angle_hash[x]+"\n")
angle_file.close()

