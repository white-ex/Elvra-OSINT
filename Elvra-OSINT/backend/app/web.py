from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/dashboard", response_class=HTMLResponse)
def dashboard():

    return """
<html>
<head>
<title>Elvra OSINT</title>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>

<style>

body{
margin:0;
background:radial-gradient(circle at top,#0b1220,#05070f);
color:#e5e7eb;
font-family:Arial;
}

.header{text-align:center;padding:20px;}

.title{
font-size:26px;
font-weight:bold;
}

.sub{
opacity:0.6;
font-size:13px;
}

.panel{
display:flex;
justify-content:center;
gap:8px;
flex-wrap:wrap;
margin-top:15px;
}

.tag{
padding:8px 12px;
background:#111827;
border:1px solid #1f2937;
border-radius:8px;
cursor:pointer;
transition:0.2s;
font-size:13px;
}

.tag.active{
background:#6366f1;
border-color:#6366f1;
}

.input-box{text-align:center;margin-top:15px;}

input{
padding:12px;
width:320px;
background:#0f172a;
color:white;
border:1px solid #1f2937;
border-radius:10px;
margin:5px;
}

button{
margin-top:10px;
padding:12px 20px;
background:#6366f1;
border:none;
border-radius:10px;
color:white;
cursor:pointer;
}

.container{
display:flex;
gap:15px;
padding:20px;
}

.card{
flex:1;
background:rgba(17,24,39,0.7);
border:1px solid #1f2937;
border-radius:12px;
padding:15px;
}

.small{
font-size:13px;
line-height:1.5;
}

#graph{height:280px;}

</style>

</head>

<body>

<div class="header">

<div class="title">Elvra OSINT</div>
<div class="sub">Identity Intelligence Dashboard</div>

<div class="panel">

<span class="tag active" onclick="toggle('email')" id="tag_email">Email</span>
<span class="tag active" onclick="toggle('username')" id="tag_username">Name</span>
<span class="tag" onclick="toggle('phone')" id="tag_phone">Phone</span>
<span class="tag" onclick="toggle('ip')" id="tag_ip">IP</span>
<span class="tag" onclick="toggle('domain')" id="tag_domain">Domain</span>
<span class="tag" onclick="toggle('hash')" id="tag_hash">Hash</span>

</div>

<div class="input-box">
<div id="inputs"></div>
<button onclick="run()" id="btn">Analyze</button>
</div>

</div>

<div class="container">

<div class="card">
<h3>Profile</h3>
<div id="profile" class="small"></div>
</div>

<div class="card">
<h3>Analysis</h3>
<div id="analysis" class="small"></div>
</div>

<div class="card">
<h3>Graph</h3>
<div id="graph"></div>
</div>

</div>

<div class="container">

<div class="card">
<h3>Radar</h3>
<canvas id="radar"></canvas>
</div>

<div class="card">
<h3>Results</h3>
<div id="results" class="small"></div>
</div>

</div>

<script>

let chart=null;
let network=null;

let selected={
email:true,
username:true,
phone:false,
ip:false,
domain:false,
hash:false
};

function toggle(t){
selected[t]=!selected[t];
document.getElementById("tag_"+t).classList.toggle("active");
renderInputs();
}

function renderInputs(){

let html="";

if(selected.email) html+="<input id='email' placeholder='email'>";
if(selected.username) html+="<input id='username' placeholder='name'>";
if(selected.phone) html+="<input id='phone' placeholder='phone'>";
if(selected.ip) html+="<input id='ip' placeholder='ip'>";
if(selected.domain) html+="<input id='domain' placeholder='domain'>";
if(selected.hash) html+="<input id='hash' placeholder='hash'>";

document.getElementById("inputs").innerHTML=html;
}

renderInputs();

async function run(){

const btn=document.getElementById("btn");
btn.innerText="Analyzing...";
btn.disabled=true;

let email=document.getElementById("email")?.value || "";
let username=document.getElementById("username")?.value || "";
let phone=document.getElementById("phone")?.value || "";
let ip=document.getElementById("ip")?.value || "";
let domain=document.getElementById("domain")?.value || "";
let hash=document.getElementById("hash")?.value || "";

const res=await fetch(
"/enrich?email="+encodeURIComponent(email)+
"&username="+encodeURIComponent(username)+
"&phone="+encodeURIComponent(phone)+
"&ip="+encodeURIComponent(ip)+
"&domain="+encodeURIComponent(domain)+
"&hash="+encodeURIComponent(hash)
);

const data=await res.json();

btn.innerText="Analyze";
btn.disabled=false;

const fusion=data.identity_fusion?.identity || {};
const radar=data.radar || {labels:[],values:[]};
const graph=data.graph || {nodes:[],edges:[]};
const links=data.username_results || [];
const ai=data.ai || {};

document.getElementById("profile").innerHTML=
"<b>Name:</b> "+(fusion.main_username||"N/A")+"<br>"+
"<b>Email:</b> "+(fusion.email||"N/A")+"<br>"+
"<b>Phone:</b> "+(fusion.phone||"N/A")+"<br><br>"+
"<b>Confidence:</b> "+(fusion.confidence||0)+"%";

document.getElementById("analysis").innerHTML=
"<b>Analysis:</b><br>"+
(ai.analysis||ai.summary||"N/A")+"<br><br>"+
"<b>Level:</b> "+(ai.level||"N/A")+"<br><br>"+
"<b>Note:</b><br>"+(ai.technical_note||"N/A");

let html="";
for(let i=0;i<links.length;i++){
html+="<a href='"+links[i].url+"' target='_blank'>"+links[i].platform+"</a><br>";
}
document.getElementById("results").innerHTML=html||"No results";

if(chart) chart.destroy();

chart=new Chart(document.getElementById("radar"),{
type:"radar",
data:{
labels:radar.labels||[],
datasets:[{data:radar.values||[],label:"OSINT"}]
}
});

const container=document.getElementById("graph");

if(network) network.destroy();

network=new vis.Network(container,{
nodes:new vis.DataSet(graph.nodes||[]),
edges:new vis.DataSet(graph.edges||[])
},{physics:{enabled:true}});

}

</script>

</body>
</html>
"""