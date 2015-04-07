# check prefixes and asns
# get unique edgelist_dir, prefix_origin w.r.t. a route-collector 


import sys
from itertools import islice

def isValidIP(octets):
	# ip octets greater than 255
	if octets[0]>255 or octets[1]>255 or octets[2]>255 or octets[3]>255:
		return False
	# pvt. ip : 10.*.*.*
	if octets[0]==10:
		return False
	# pvt. ip : 192.168.*.*
	if octets[0]==192 and octets[1]==168:
		return False
	# pvt. ip : 172.16.0.0 to 172.31.255.255
	if (octets[0]==172 and octets[1]>=16 and octets[2]>=0 and octets[3]>=1) and (octets[0]==172 and octets[1]<=31 and octets[2]<=255 and octets[3]<=254):
		return False
	# invalid ip : 0.0.0.0	
	if octets[0]==0 and octets[1]==0 and octets[2]==0 and octets[3]==0:
		return False
	return True
	
def isValidASN(asn):
	# pvt. or reserved ASNs. refer http://www.iana.org/assignments/as-numbers/as-numbers.xhtml
	if asn==0 or asn==65535 or (asn>=64512 and asn<=65534) or asn==23456 or (asn>=65536 and asn<=131071) or asn>=4200000000:
		return False
	return True
	
def isValidASPATH(aspath):
	# aspath of length 1
	if len(aspath)<=1:
		return False
	# aspath with as-set
	if aspath[-1][0]=='{':
		return False
	# pvt. ASNs checkd in uniq.py.
	return True
		

path="../data/"+"/".join(sys.argv[1:]) # context root for data of a route collector
prefix_aspath_unchecked_file=path+"/prefix_aspath_unchecked"
prefix_origin_file=path+"/prefix_origin"
edgelist_dir_file=path+"/edgelist_dir"
edgelist_undir_file=path+"/edgelist_undir"
asn_prefixes_file=path+"/asn_prefixes"
asn_file=path+"/asn"

chunk=1000000 # chunk size for processing prefix_aspath_unchecked
prefix_origin_hash={}
edgelist_dir_hash={}
with open(prefix_aspath_unchecked_file) as pau:
	while True:
		lines=list(islice(pau,chunk))
		lines=map(str.strip,lines)
		# lines will be empty at EOF
		if not lines:
			break
		
		for x in lines:
			tmp=x.split(":::") # format <advertised ip:::aspath>
			prefix=tmp[0]
			aspath=tmp[1]
			
			aspath=aspath.split(" ")
			if not isValidASPATH(aspath):
				continue
			
			tmp=prefix.split(".")
			octets=tmp[:3]
			# skip ipv6
			try:
				octets.append(tmp[3].split("/")[0])
				octets.append(tmp[3].split("/")[1])
			except IndexError: # ipv6 will result in IndexError 
				continue
			octets=map(int,octets)
			if not isValidIP(octets):
				continue
			
			if not prefix+" "+aspath[-1] in prefix_origin_hash:
				prefix_origin_hash[prefix+" "+aspath[-1]]=1
			
			for i in range(len(aspath)-1):
				if (aspath[i]+" "+aspath[i+1] in edgelist_dir_hash) or aspath[i]==aspath[i+1]:
					continue
				edgelist_dir_hash[aspath[i]+" "+aspath[i+1]]=1
		print "***chunk done*** "+sys.argv[5]

po=open(prefix_origin_file,"w")
print "writing prefix_origin"+sys.argv[5]
for x in prefix_origin_hash:
	po.write(x+"\n")
po.close()
				
ed=open(edgelist_dir_file,"w")
print "writing edgelist_dir"+sys.argv[5]
for x in edgelist_dir_hash:
	ed.write(x+"\n")
ed.close()
