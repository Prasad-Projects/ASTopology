# check for invalid ASNs in edgelist_dir
# get global unique edgelist_dir, edgelist_undir, prefix_origin

import sys

path="../data/"+"/".join(sys.argv[1:]) # context root
rclist=["route-views","route-views2","route-views3","route-views4","route-views6","route-views.saopaulo","route-views.linx","route-views.sydney","route-views.wide","route-views.kixp","route-views.eqix","route-views.isc","route-views.telxatl","route-views.jinx"]

def isValidASN(asn):
	# check if ASN is pvt or reserved
	asn=int(asn)
	if asn==0 or asn==65535 or (asn>=64198 and asn<=65534) or asn==23456 or (asn>=65536 and asn<=131071) or (asn>=135581 and asn<=196607) or (asn>=202240 and asn<=262143) or (asn>=328704 and asn<=393215) or (asn>=394240 and asn<=4199999999) or asn>=4200000000:
		return False
	return True

# write edgelist_dir without duplicates
edgelist_dir_hash={}
for rc in rclist:
	edgelist_dir_file=path+"/"+rc+"/edgelist_dir"
	try:
		with open(edgelist_dir_file) as ed:
			edgelist=map(str.strip,ed.readlines())
			for x in edgelist:
				tmp=x.split(" ")
				# check for validity of ASNs
				if not (isValidASN(tmp[0]) and isValidASN(tmp[1])):
					continue
				if not x in edgelist_dir_hash:
					edgelist_dir_hash[x]=1
	except IOError: # file not found
		print "file not found "+rc
ed=open(path+"/edgelist_dir","w")
print "writing edgelist_dir main"
for x in edgelist_dir_hash:
	ed.write(x+"\n")
ed.close()

# write prefix_origin without duplicates
prefix_origin_hash={}
for rc in rclist:
	prefix_origin_file=path+"/"+rc+"/prefix_origin"
	try:
		with open(prefix_origin_file) as po:
			polist=map(str.strip,po.readlines())
			for x in polist:
				if not x in prefix_origin_hash:
					prefix_origin_hash[x]=1
	except IOError:
		print "file not found "+rc
po=open(path+"/prefix_origin","w")
print "writing prefix_origin main"
for x in prefix_origin_hash:
	po.write(x+"\n")
po.close()
del prefix_origin_hash

# write edgelist_undir
edgelist_undir_hash={}
for x in edgelist_dir_hash:
	tmp=x.split(" ")
	if tmp[1]+" "+tmp[0] in edgelist_undir_hash:
		continue
	edgelist_undir_hash[x]=1
eu=open(path+"/edgelist_undir","w")
print "writing edgelist_undir"
for x in edgelist_undir_hash:
	eu.write(x+"\n")
eu.close()
del edgelist_undir_hash

# write asn
asn_hash={}
for x in edgelist_dir_hash:
	tmp=x.split(" ")
	if not tmp[0] in asn_hash:
		asn_hash[tmp[0]]=1
	if not tmp[1] in asn_hash:
		asn_hash[tmp[1]]=1
asn=open(path+"/asn","w")
print "writing asn"
for x in asn_hash:
	asn.write(x+"\n")
asn.close()
