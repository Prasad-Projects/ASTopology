import sys

path="../data/"+"/".join(sys.argv[1:])

all_rir_hash={}
with open("rir") as rir:
	rirlist=map(str.strip,rir.readlines())
	for x in rirlist:
		tmp=x.split(",")
		for i in range(int(tmp[0]),int(tmp[1])+1):
			all_rir_hash[str(i)]=tmp[2]

asn_rir_hash={}
with open(path+"/asn") as asn:
	asnlist=map(str.strip,asn.readlines())
	for x in asnlist:
		asn_rir_hash[x]=all_rir_hash[x]

asn_whois=open(path+"/asn_whois","w")
for x in asn_rir_hash:
	asn_whois.write(x+" "+asn_rir_hash[x]+"\n")
asn_whois.close()

asn_rir=open(path+"/asn_rir","w")
for x in asn_rir_hash:
	asn_rir.write(x+" "+asn_rir_hash[x].split(".")[1]+"\n")
asn_rir.close()

		
		
		
	


