#!/usr/bin/python
from flask import Flask,jsonify,send_from_directory,render_template

def get_outdegree(snapshot):
	snapshot=snapshot.split(".")
	outdegree_hash={}
	with open("../../data/"+"/".join(snapshot)+"/outdegree") as outdegree_file:
		outdegree_lines=map(str.strip,outdegree_file.readlines())
		for line in outdegree_lines:
			line=line.split(" ")
			outdegree_hash[line[0]]=int(line[1])
	return outdegree_hash

def get_country():
	#snapshot=snapshot.split(".")
	country_hash={}
	with open("../../base/gc/asn_country") as country_file:
		country_lines=map(str.strip,country_file.readlines())
		for line in country_lines:
			line=line.split(",")
			country_hash[line[0]]=str(line[1])
	return country_hash

def get_edgelist(snapshot):
	snapshot=snapshot.split(".")
	edgelist_hash={}
	with open("../../data/"+"/".join(snapshot)+"/edgelist") as edgelist_file:
		edgelist_lines=map(str.strip,edgelist_file.readlines())
		for line in edgelist_lines:
			line=line.split(" ")
			edgelist_hash[(line[0],line[3])]={"sx":float(line[1]),"sy":float(line[2]),"ex":float(line[4]),"ey":float(line[5]),"r":float(line[6]),"g":float(line[7]),"b":float(line[8]),"alpha":float(line[9])}
	return edgelist_hash
		
def get_nodelist(snapshot):
	snapshot=snapshot.split(".")
	nodelist_hash={}
	with open("../../data/"+"/".join(snapshot)+"/nodelist") as nodelist_file:
		nodelist_lines=map(str.strip,nodelist_file.readlines())
		for line in nodelist_lines:
			line=line.split(" ")
			nodelist_hash[line[0]]={"x":float(line[1]),"y":float(line[2]),"radius":float(line[3]),"r":0.0,"g":0.0,"b":0.0}
	return nodelist_hash

def get_edgetype(snapshot):
	snapshot=snapshot.split(".")
	edgetype_hash={}
	with open("../../data/"+"/".join(snapshot[:2])+"/"+snapshot[0]+snapshot[1]+".relationship") as edgetype_file:
		edgetype_lines=map(str.strip,edgetype_file.readlines())
		for line in edgetype_lines:
			line=line.split("\t")
			edgetype_hash[(line[0],line[1])]=line[2]
	return edgetype_hash

app = Flask(__name__)
app.debug=True

@app.route('/')
def home():
	return render_template("index.html")

"""
@app.route('/astopo/api/outdegree/<int:outdegree>',methods=['GET'])
def filter_by_outdegree(outdegree):
	aslist=[]
	for x in outdegree_hash:
		if outdegree_hash[x]>=outdegree:
			aslist.append(x)
	data=[]	
	for asn in aslist:
		xcoord=nodelist_hash[asn][0]
		ycoord=nodelist_hash[asn][1]
		data.append({'x':xcoord,'y':ycoord})
	print "no. of nodes: "+str(len(aslist))	
	data2=[]
	for sasn in aslist:
		for easn in aslist:
			sasn=str(sasn)
			easn=str(easn)
			if sasn+" "+easn in edgelist_hash:
				data2.append(edgelist_hash[sasn+" "+easn])
	print "no. of edges: "+str(len(data2))					
	return jsonify({'N':len(data),'E':len(data2),'data':data,'data2':data2})
"""

country_hash=get_country()
#print country_hash

@app.route('/astopo/check')
def check_route():
	return "check"

@app.route('/astopo/api/normal/<string:query>')
def query_normal(query):
	print "Normal Graph"
	parts=map(str,query.split("&"))
	query_hash={}
	for x in parts:
		tmp=x.split("=")
		query_hash[tmp[0]]=tmp[1]
	outdegree_hash=get_outdegree(query_hash["snapshot"])
	nodelist_hash=get_nodelist(query_hash["snapshot"])
	edgelist_hash=get_edgelist(query_hash["snapshot"])
	edgetype_hash=get_edgetype(query_hash["snapshot"])
	#print edgetype_hash
	#country_hash=get_country(query_hash["snapshot"])
	print query_hash
	
	aslist={}
	for asn in outdegree_hash:
		try:
			if (outdegree_hash[asn]>=int(query_hash["outdegree"]) or query_hash["outdegree"]=="") and (country_hash[asn]==str(query_hash["country"]) or str(query_hash["country"])==""):
				aslist[asn]=None
		except KeyError:
			continue
				
	data=[]
	for asn in aslist:
		data.append(nodelist_hash[asn])
	
	data2=[]
	for asn1,asn2 in edgelist_hash:
		if (asn1 in aslist) and (asn2 in aslist):
			if query_hash["edgetype"]=="all":
				data2.append(edgelist_hash[(asn1,asn2)]) 
			elif query_hash["edgetype"]=="p2p":
				if ((asn1,asn2) in edgetype_hash) and (edgetype_hash[(asn1,asn2)]=="p2p"):
					data2.append(edgelist_hash[(asn1,asn2)]) 
				elif ((asn2,asn1) in edgetype_hash) and (edgetype_hash[(asn2,asn1)]=="p2p"):
					data2.append(edgelist_hash[(asn1,asn2)])
			elif query_hash["edgetype"]=="p2c":
				if ((asn1,asn2) in edgetype_hash) and ((edgetype_hash[(asn1,asn2)]=="p2c") or (edgetype_hash[(asn1,asn2)]=="c2p")):
					data2.append(edgelist_hash[(asn1,asn2)]) 
				elif ((asn2,asn1) in edgetype_hash) and ((edgetype_hash[(asn2,asn1)]=="p2c") or (edgetype_hash[(asn2,asn1)]=="c2p")):
					data2.append(edgelist_hash[(asn1,asn2)])
			
	print "Nodes:"+str(len(data))
	print "Edges:"+str(len(data2))		
	return jsonify({'N':len(data),'E':len(data2),'data':data,'data2':data2}) 
	
"""
@app.route('/astopo/api/bipartite/<string:query>')
def query_bipartite(query):
	parts=map(str,query.split("&"))
	query_hash={}
	for x in parts:
		tmp=x.split("=")
		query_hash[tmp[0]]=tmp[1]
	print query_hash
	return query
"""	

@app.route('/astopo/api/bipartite/<string:query>')
def query_bipartite(query):
	print "Bipartite Graph"
	parts=map(str,query.split("&"))
	query_hash={}
	for x in parts:
		tmp=x.split("=")
		query_hash[tmp[0]]=tmp[1]
	#country_hash=get_country(query_hash["snapshot"])
	nodelist_hash=get_nodelist(query_hash["snapshot"])
	edgelist_hash=get_edgelist(query_hash["snapshot"])

	aslist1={}
	for asn in nodelist_hash:
		try:
			if country_hash[asn]==str(query_hash["set1"]):
				aslist1[asn]=None
		except KeyError:
			continue
	
	aslist2={}
	for asn in nodelist_hash:
		try:
			if country_hash[asn]==str(query_hash["set2"]):
				aslist2[asn]=None
		except KeyError:
			continue
		
	set1=[]
	for asn in aslist1:
		tmp=nodelist_hash[asn]
		tmp["r"]=1.0
		set1.append(tmp)
	
	set2=[]
	for asn in aslist2:
		set2.append(nodelist_hash[asn])
	
	data2=[]
	for asn1,asn2 in edgelist_hash:
		if ((asn1 in aslist1) and (asn2 in aslist2)) or ((asn1 in aslist2) and (asn2 in aslist1)):
			data2.append(edgelist_hash[(asn1,asn2)]) 
	
	print "Nodes:"+str(len(set1)+len(set2))
	print "Edges:"+str(len(data2))		
	return jsonify({'N_set1':len(set1),'N_set2':len(set2),'E':len(data2),'set1':set1,'set2':set2,'data2':data2})


@app.route('/astopo/api/ascentric/<string:query>')
def query_ascentric(query):
	print "AS-Centric"
	parts=map(str,query.split("&"))
	query_hash={}
	for x in parts:
		tmp=x.split("=")
		query_hash[tmp[0]]=tmp[1]
	nodelist_hash=get_nodelist(query_hash["snapshot"])
	edgelist_hash=get_edgelist(query_hash["snapshot"])

	aslist={}
	data=[]
	data.append(nodelist_hash[str(query_hash["asnumber"])])
	data2=[]
	for asn1,asn2 in edgelist_hash:
		if asn1==str(query_hash["asnumber"]):
			data2.append(edgelist_hash[(asn1,asn2)])
			#data2.append(edgelist_hash[(asn2,asn)])
			data.append(nodelist_hash[asn2])
		elif asn2==str(query_hash["asnumber"]):
			data2.append(edgelist_hash[(asn1,asn2)])
			#data2.append(edgelist_hash[(asn2,asn)])
			data.append(nodelist_hash[asn1])		

	print "Nodes:"+str(len(data))
	print "Edges:"+str(len(data2))		
	return jsonify({'N':len(data),'E':len(data2),'data':data,'data2':data2})

	
if __name__ == '__main__':
    app.run()
