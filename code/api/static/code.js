$(document).ready(function() {
	$(".button-collapse").sideNav({
		menuWidth: 300, // Default is 240
		edge: 'left', // Choose the horizontal origin
		closeOnClick: false // Closes side-nav on <a> clicks, useful for Angular/Meteor);
	});
	
	$('select').material_select();
	
	var paper = Raphael($("#container")[0],1600,1200);
	paper.circle(512+100,512+40,512+20);
	//paper.cirlce(512+40,512+40,200);
	
	function NodeManager( paper, node_radius, node_style, label_style )
	{
		this.paper = paper;
		this.nodes = {};
		this.node_radius = node_radius || 2;
		this.node_style = node_style || { fill: 'white', stroke: 'black', 'stroke-width': 1.5 };
		this.label_style = label_style || { fill: 'black', stroke: 'none', 'font-family': 'Arial,Helvetica,sans-serif', 'font-size': 32, 'font-weight': 600 };
	}

	NodeManager.prototype.addNode = function addNode(code, x, y, node_radius, node_style)
	{
			var node = this.paper.circle( x, y, node_radius || this.node_radius ).attr( node_style || this.node_style );
			this.nodes[code] = 
				{
					x: x,
					y: y,
					r: node_radius || this.node_radius,
					node: node
				};
	}
		
	NodeManager.prototype.connectNodes = function connectNodes(startX, startY, endX, endY, alpha, r, g, b)
	{   
			var line = paper.path( ["M", startX, startY, "L", endX, endY ] );
			line.attr("stroke-width", "0.25");
			line.attr("opacity", 1.5*alpha);
			line.attr("stroke", Raphael.rgb(r*255,g*255,b*255));
			line.translate(0.1, 0.1);
	}
	
		
	function randomIntFromInterval(min,max)
	{
		return Math.floor(Math.random()*(max-min+1)+min);
	}
	
	query_prefix="http://localhost:5000/astopo/api";
	
	function getNormalQuery() {
		snapshot="2013.03.01.0200";
		outdegree=$("#outdegree")[0].value;
		country=$("#country")[0].value;
		edgetype=$("#edgetype")[0].value;
		return query_prefix+"/normal/snapshot="+snapshot+"&outdegree="+outdegree+"&country="+country+"&edgetype="+edgetype;
	}
	
	function getBipartiteQuery() {
		snapshot="2013.03.01.0200";
		set1=$("#set1")[0].value;
		set2=$("#set2")[0].value;
		return query_prefix+"/normal/snapshot="+snapshot+"&set1="+set1+"&set2="+set2;
	}
	
	function getASCentricQuery() {
		snapshot="2013.03.01.0200";
		asnumber=$("#asnumber")[0].value;
		return query_prefix+"/normal/snapshot="+snapshot+"&asnumber="+asnumber;
	}
		
	$("#normalRedraw").bind('click', function () { 
		$.get(getNormalQuery(), function(json) {
			paper.clear();
			paper.circle(512+100,512+40,512+20);
			drawEdges(json.data2,json.E);
			drawNodes(json.data,json.N);
			paper.cirlce(512+40,512+40,20);
		});
	});
	
	$("#bipartiteRedraw").bind('click', function () { 
		alert(getBipartiteQuery());
	});
	
	$("#ascentricRedraw").bind('click', function () {
		alert(getASCentricQuery());
	});
	
	var nodeMgr = new NodeManager(paper);

	var XOFFSET = 40;
	var YOFFSET = 40;
		
	var LY = 5;
	var LY1 = 10;
	var RY = 1.428169;
	
	var LX = 5;
	var LX1 = 10;
	var RX = 0.6584415;
	
	//drawEdges(JSON.parse(data2));
	//drawNodes(JSON.parse(data));
	
	function drawEdges(jsondata,E) {
		var mydata = jsondata
		for(i = 0; i < E; i++) {
			var givenStartX = mydata[i].sx;
			var givenStartY = mydata[i].sy;
			
			//var startX = (givenStartX - LX)/RX + LX1;
			//var startY = (givenStartY - LY)/RY + LY1;
			
			//var startX = givenStartX / 2 + 300;
			//var startY = givenStartY / 2 + 100;
			
			var startX = givenStartX + XOFFSET;
			var startY = givenStartY + YOFFSET;
			
			var givenEndX = mydata[i].ex;
			var givenEndY = mydata[i].ey;
			
			//var endX = (givenEndX - LX)/RX + LX1;
			//var endY = (givenEndY - LY)/RY + LY1;
			
			//var endX = givenEndX / 2 + 300;
			//var endY = givenEndY / 2 + 100;
			
			var endX = givenEndX + XOFFSET;
			var endY = givenEndY + YOFFSET;
			
			var alpha = mydata[i].alpha;
			var r = mydata[i].r;
			var g = mydata[i].g;
			var b = mydata[i].b;
			
			nodeMgr.connectNodes(startX, startY, endX, endY, alpha, r, g, b);
		}	
	}
	
	function drawNodes(jsondata,N) {
		var mydata = jsondata;
		for(i = 0; i < N; i++) {
			var givenx = mydata[i].x;
			var giveny = mydata[i].y;
			
			//var x = (givenx - LX)/RX + LX1;
			//var y = (giveny - LY)/RY + LY1;
			
			//var x = givenx / 2 + 300;
			//var y = giveny / 2 + 100;
			
			var x = givenx + XOFFSET;
			var y = giveny + YOFFSET;
			
			var radius = mydata[i].radius*0.3;
			var node_style = { fill: Raphael.rgb(mydata[i].r, mydata[i].g, mydata[i].b), stroke: 'black', 'stroke-width': 1 };
						
			nodeMgr.addNode("o", x, y, radius, node_style);
		}	
	}
});
