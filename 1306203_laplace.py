import uuid

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="1306203/Laplace Transform Fundamentals",
    layout="wide",
)

# Remove Streamlit's default padding/header so the app fills the page
st.markdown(
    """
    <style>
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    header[data-testid="stHeader"] {height: 0;}
    </style>
    """,
    unsafe_allow_html=True,
)

uid = "laplace_" + uuid.uuid4().hex[:8]

html = r"""
<div id="ROOT_ID" class="animation-app">

<style>
#ROOT_ID {
    width:100%;
    max-width:1500px;
    margin:auto;
    padding:clamp(8px, 2vw, 24px);
    box-sizing:border-box;
    font-family:Arial,sans-serif;
    position:relative;
    color:#1f2a44;
    background:linear-gradient(160deg,#f7f9ff 0%,#eaf0fc 100%);
    border-radius:18px;
    box-shadow:0 10px 30px rgba(31,42,68,0.10);
}

#ROOT_ID * { box-sizing:border-box; }

#ROOT_ID h2 {
    text-align:center;
    font-size:clamp(20px, 2.6vw, 30px);
    margin:12px 0 4px;
    padding:0 140px;
    letter-spacing:0.5px;
    background:linear-gradient(90deg,#2f6fed,#12a36a);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
    color:transparent;
}

#ROOT_ID .subtitle {
    text-align:center;
    font-size:clamp(13px,1.7vw,18px);
    margin:0 0 18px;
    opacity:0.85;
}

#ROOT_ID button.theme {
    color:white;
    border:0;
    border-radius:10px;
    cursor:pointer;
    font-weight:bold;
    white-space:nowrap;
    touch-action:manipulation;
    box-shadow:0 4px 10px rgba(0,0,0,0.22);
    transition:transform .12s, filter .12s;
    background:linear-gradient(135deg,#8b6cff,#5a3fd4);
    position:absolute;
    top:clamp(24px,3vw,36px);
    right:clamp(8px,1.5vw,16px);
    padding:8px 14px;
    font-size:clamp(12px,1.3vw,14px);
    z-index:2;
}
#ROOT_ID button.theme:hover { transform:translateY(-1px); filter:brightness(1.08); }
#ROOT_ID button.theme:active { transform:scale(0.97); }

/* ---------- two-column layout ---------- */
#ROOT_ID .layout {
    display:grid;
    grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);
    gap:18px;
    align-items:start;
}

#ROOT_ID .colhead {
    margin:0 0 10px;
    padding:8px 14px;
    border-radius:10px;
    font-size:16px;
    font-weight:bold;
    color:#fff;
    background:linear-gradient(135deg,#2f6fed,#1a56c4);
}
#ROOT_ID .colhead.s { background:linear-gradient(135deg,#12a36a,#0d7a50); }

#ROOT_ID .panel {
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:14px;
    box-shadow:0 6px 18px rgba(31,42,68,0.12);
    padding:14px;
}

#ROOT_ID .col { display:flex; flex-direction:column; gap:14px; min-width:0; }

#ROOT_ID .panel h3 { margin:0 0 10px; font-size:17px; }
#ROOT_ID .sigcard { --c:#2f6fed; }
#ROOT_ID .sigcard h3 { color:var(--c); }

#ROOT_ID .tiles { display:grid; grid-template-columns:1fr; gap:8px; }
#ROOT_ID .tsub { display:grid; grid-template-columns:minmax(170px,210px) minmax(0,1fr); gap:14px; align-items:start; }

#ROOT_ID .tile {
    cursor:pointer;
    border:2px solid #d3dcf0;
    border-radius:10px;
    padding:6px 4px 5px;
    text-align:center;
    font-size:12px;
    font-weight:bold;
    line-height:1.25;
    background:#ffffff;
    user-select:none;
    transition:border-color .12s, box-shadow .12s;
}
#ROOT_ID .tile:hover { border-color:var(--c); }
#ROOT_ID .tile.active {
    border-color:var(--c);
    box-shadow:0 0 0 3px color-mix(in srgb, var(--c) 25%, transparent);
}
#ROOT_ID .tile svg { display:block; width:100%; height:34px; stroke:var(--c); fill:none; }

#ROOT_ID .formula {
    margin:12px 0 0;
    padding:9px 10px;
    border-radius:8px;
    background:rgba(47,111,237,0.08);
    font-size:15px;
    font-weight:bold;
    text-align:center;
    overflow-wrap:anywhere;
}

#ROOT_ID .param { display:block; margin-top:10px; font-size:13px; font-weight:bold; }
#ROOT_ID .param.hide { display:none; }

#ROOT_ID input[type=number] {
    display:block;
    width:100%;
    margin-top:5px;
    padding:7px;
    font-size:15px;
    border:1px solid #b9c5e0;
    border-radius:8px;
    background:#ffffff;
    color:#1f2a44;
    text-align:center;
}
#ROOT_ID input[type=number]:focus {
    outline:none;
    border-color:#2f6fed;
    box-shadow:0 0 0 3px rgba(47,111,237,0.25);
}

#ROOT_ID .grid2 { display:grid; grid-template-columns:1fr 1fr; gap:10px; }
#ROOT_ID .grid2 label { font-size:13px; font-weight:bold; }

#ROOT_ID .hint { margin-top:8px; font-size:12px; opacity:0.75; line-height:1.45; }

#ROOT_ID canvas {
    display:block;
    max-width:100%;
    background:linear-gradient(180deg,#ffffff,#f0f4fc);
    border:1px solid #cdd7ec;
    border-radius:12px;
}

/* ---------- X(s) display ---------- */
#ROOT_ID .xs {
    text-align:center;
    font-size:clamp(20px,2.6vw,30px);
    font-weight:bold;
    padding:6px 4px 10px;
    overflow-wrap:anywhere;
}
#ROOT_ID .frac { display:inline-flex; flex-direction:column; vertical-align:middle; text-align:center; }
#ROOT_ID .frac > span:first-child { border-bottom:2px solid currentColor; padding:0 8px 3px; }
#ROOT_ID .frac > span:last-child { padding:3px 8px 0; }

#ROOT_ID .pills { display:flex; flex-wrap:wrap; gap:10px; justify-content:center; }
#ROOT_ID .pill {
    padding:8px 16px;
    border-radius:999px;
    background:#ffffff;
    border:1px solid #d3dcf0;
    box-shadow:0 3px 10px rgba(31,42,68,0.08);
    font-size:clamp(12px,1.4vw,15px);
    font-weight:bold;
}

/* ---------- pole / zero summary ---------- */
#ROOT_ID .pzsum { display:grid; grid-template-columns:1fr 1fr; gap:14px; }
#ROOT_ID .pzbox h4 { margin:0 0 8px; font-size:15px; display:flex; align-items:center; gap:8px; }
#ROOT_ID .pzbox ul { margin:0; padding-left:20px; font-size:14px; line-height:1.8; }
#ROOT_ID .pzbox .none { font-size:14px; opacity:0.75; }
#ROOT_ID .pzbox.z h4 { color:#12a36a; }
#ROOT_ID .pzbox.p h4 { color:#e5484d; }
#ROOT_ID .counts { margin-top:10px; font-size:13px; opacity:0.85; }

/* ---------- dark mode ---------- */
#ROOT_ID.dark {
    background:linear-gradient(160deg,#0d1117 0%,#161d2e 100%);
    color:#e6edf7;
    box-shadow:0 10px 30px rgba(0,0,0,0.45);
}
#ROOT_ID.dark h2 {
    background:linear-gradient(90deg,#6aa9ff,#3ddc97);
    -webkit-background-clip:text;
    background-clip:text;
    -webkit-text-fill-color:transparent;
}
#ROOT_ID.dark .panel {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
    box-shadow:0 6px 18px rgba(0,0,0,0.5);
}
#ROOT_ID.dark canvas {
    background:linear-gradient(180deg,#1b2336,#111724);
    border-color:#2f3b57;
}
#ROOT_ID.dark .sigcard { --c:#58a6ff; }
#ROOT_ID.dark .tile { background:#0f1522; border-color:#33415f; }
#ROOT_ID.dark .tile:hover,
#ROOT_ID.dark .tile.active { border-color:var(--c); }
#ROOT_ID.dark .formula { background:rgba(88,166,255,0.12); }
#ROOT_ID.dark input[type=number] { background:#0f1522; color:#e6edf7; border-color:#3b4866; }
#ROOT_ID.dark input[type=number]:focus { border-color:#58a6ff; box-shadow:0 0 0 3px rgba(88,166,255,0.30); }
#ROOT_ID.dark .pill { background:#1a2233; border-color:#33415f; color:#e6edf7; box-shadow:0 3px 12px rgba(0,0,0,0.4); }
#ROOT_ID.dark .pzbox.z h4 { color:#3ddc97; }
#ROOT_ID.dark .pzbox.p h4 { color:#ff6b6b; }

/* ---------- responsive ---------- */
@media (max-width:1100px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
}
@media (max-width:900px) {
    #ROOT_ID .layout { grid-template-columns:1fr; }
}
@media (max-width:650px) {
    #ROOT_ID .tsub { grid-template-columns:1fr; }
    #ROOT_ID .tiles { grid-template-columns:1fr 1fr; }
}
@media (max-width:550px) {
    #ROOT_ID { padding:6px; }
    #ROOT_ID h2 { margin-top:64px; padding:0; }
    #ROOT_ID button.theme { padding:7px 11px; }
    #ROOT_ID .pzsum { grid-template-columns:1fr; }
}
</style>

<button class="theme" id="theme">🌙 DARK MODE</button>

<h2>1306203 Signals & Systems: Laplace Transform Fundamentals</h2>
<div class="subtitle">X(s) = ∫<sub>0</sub><sup>∞</sup> x(t) e<sup>−st</sup> dt &nbsp;&nbsp;(unilateral transform, s = σ + jω)</div>

<div class="layout">

    <!-- LEFT COLUMN: TIME DOMAIN -->
    <div class="col">

        <div class="colhead">Time domain</div>

        <div class="tsub" id="time_area">

        <div class="panel sigcard" id="card_sig"></div>

        <div class="col">
        <div class="panel sigcard">
            <h3>Signal information</h3>
            <div id="info_top"></div>
        </div>

        <div class="panel">
            <h3 style="color:#2f6fed">Signal x(t)</h3>
            <canvas id="cTime"></canvas>
            <div class="grid2" style="margin-top:10px">
                <label>t<sub>min</sub> (s)
                    <input id="tmin" type="number" value="-2" step="1" min="-100" max="99">
                </label>
                <label>t<sub>max</sub> (s)
                    <input id="tmax" type="number" value="10" step="1" min="-99" max="100">
                </label>
            </div>
            <div class="hint">The amplitude axis fits the signal automatically.</div>
        </div>
        </div>

        </div>

    </div>

    <!-- RIGHT COLUMN: S DOMAIN -->
    <div class="col">

        <div class="colhead s">s-domain</div>

        <div class="panel">
            <h3 style="color:#12a36a">Laplace transform X(s)</h3>
            <div class="xs" id="xs"></div>
            <div class="pills">
                <div class="pill" id="pill_roc"></div>
                <div class="pill" id="pill_jw"></div>
            </div>
        </div>

        <div class="panel">
            <h3 style="color:#12a36a">Pole-zero plot</h3>
            <canvas id="cPZ"></canvas>
            <div class="pzsum" style="margin-top:14px">
                <div class="pzbox z">
                    <h4><svg width="18" height="18" viewBox="0 0 18 18"><circle cx="9" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2.4"/></svg>Zeros</h4>
                    <div id="zlist"></div>
                </div>
                <div class="pzbox p">
                    <h4><svg width="18" height="18" viewBox="0 0 18 18"><path d="M3 3 L15 15 M15 3 L3 15" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/></svg>Poles</h4>
                    <div id="plist"></div>
                </div>
            </div>
            <div class="counts" id="counts"></div>
        </div>

    </div>

</div>

<script>
(function(){

const root=document.getElementById("ROOT_ID");
const $=s=>root.querySelector(s);

// ======================================
// SIGNAL TABLE
// ======================================

const TYPES={
    imp:  {label:"Unit impulse<br>δ(t)",            path:"M2 24 H38 M20 24 V6 M15.5 11 L20 5 L24.5 11"},
    step: {label:"Unit step<br>u(t)",               path:"M2 24 H19 V6 H38"},
    ramp: {label:"Ramp<br>t·u(t)",                  path:"M2 24 H12 L34 4"},
    tn:   {label:"Power × exponential<br>tⁿ e<sup>−at</sup> u(t)", path:"M2 24 H10 C16 24 18 4 24 4 C30 4 32 20 38 23"},
    exp:  {label:"Real exponential<br>e<sup>−at</sup> u(t)",       path:"M2 24 H11 V6 C16 17 26 22 38 23"},
    cos:  {label:"Cosine<br>cos(ω₀t) u(t)",         path:"M2 24 H10 M10 6 C16 6 19 22 25 22 S34 6 38 6"},
    sin:  {label:"Sine<br>sin(ω₀t) u(t)",           path:"M2 14 H10 C14 0 18 0 22 14 S30 28 38 14"},
    dcos: {label:"Damped cosine<br>e<sup>−at</sup>cos(ω₀t) u(t)",  path:"M2 24 H10 M10 5 C14 5 15 22 20 22 S24 8 28 8 S31 18 34 18 S36 14 38 14"},
    dsin: {label:"Damped sine<br>e<sup>−at</sup>sin(ω₀t) u(t)",    path:"M2 14 H10 C12 2 15 2 18 14 S23 24 26 14 S30 8 32 14 S35 18 38 14"}
};

const ORDER=["imp","step","ramp","exp","cos","sin","dcos","tn"];

const PARAMS=[
    {p:"A",label:"Amplitude A",                              types:["imp","step","ramp","tn","exp","cos","sin","dcos","dsin"], min:-20, max:20, step:0.1},
    {p:"a",label:"Decay rate a  (e<sup>−at</sup>, any real number)", types:["tn","exp","dcos","dsin"], min:-5, max:5, step:0.1},
    {p:"n",label:"Power n  (integer)",                       types:["tn"], min:0, max:6, step:1, int:true},
    {p:"w",label:"Frequency ω<sub>0</sub> (rad/s)",          types:["cos","sin","dcos","dsin"], min:0.1, max:30, step:0.1}
];

const sig={type:"dcos", A:1, a:0.5, n:2, w:3};
const view={tmin:-2, tmax:10};

// ======================================
// LEFT COLUMN: SIGNAL CARD
// ======================================

function buildCard(){

    const card=$("#time_area");

    let h='<h3>Choose a signal</h3><div class="tiles">';

    ORDER.forEach((id,i)=>{
        const wide='';
        h+='<div class="tile" data-type="'+id+'"'+wide+'>'+
           '<svg viewBox="0 0 40 28"><path d="'+TYPES[id].path+
           '" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'+
           TYPES[id].label+'</div>';
    });

    h+='</div>';
    let h2='<div class="formula" id="formula"></div>';

    PARAMS.forEach(q=>{
        h2+='<label class="param" data-for="'+q.types.join(" ")+'">'+q.label+
           '<input type="number" data-p="'+q.p+'" min="'+q.min+'" max="'+q.max+
           '" step="'+q.step+'" value="'+sig[q.p]+'"></label>';
    });

    $("#card_sig").innerHTML=h;
    $("#info_top").innerHTML=h2;

    card.querySelectorAll(".tile").forEach(el=>{
        el.addEventListener("click",()=>{
            sig.type=el.dataset.type;
            refreshCard();
            render();
        });
    });

    card.querySelectorAll(".param input").forEach(inp=>{
        inp.addEventListener("change",()=>{

            const p=inp.dataset.p;
            const q=PARAMS.find(r=>r.p===p);
            let v=Number(inp.value);

            if(!Number.isFinite(v)) v=sig[p];
            if(q.int) v=Math.round(v);
            v=Math.min(q.max,Math.max(q.min,v));

            inp.value=v;
            sig[p]=v;
            render();
        });
    });

    refreshCard();
}

function refreshCard(){

    const card=$("#time_area");

    card.querySelectorAll(".tile").forEach(el=>{
        el.classList.toggle("active",el.dataset.type===sig.type);
    });

    card.querySelectorAll(".param").forEach(el=>{
        el.classList.toggle("hide",!el.dataset.for.split(" ").includes(sig.type));
    });
}

buildCard();

// time axis inputs
const tminIn=$("#tmin"), tmaxIn=$("#tmax");

function applyTime(){

    const a=Number(tminIn.value), b=Number(tmaxIn.value);

    if(!Number.isFinite(a)||!Number.isFinite(b)||b<=a){
        tminIn.value=view.tmin; tmaxIn.value=view.tmax;
        return;
    }

    view.tmin=a; view.tmax=b;
    render();
}

tminIn.addEventListener("change",applyTime);
tmaxIn.addEventListener("change",applyTime);

// ======================================
// THEMES
// ======================================

const themes={
    light:{text:"#1f2a44",tick:"#44506e",axis:"#44506e",zero:"#9aa6bf",grid:"#e0e6f3",
           x:"#2f6fed",pole:"#e5484d",zer:"#12a36a",
           roc:"rgba(47,111,237,0.10)",rocLine:"#2f6fed",jw:"#8b5cf6",glow:5},
    dark:{text:"#e6edf7",tick:"#b4c0d9",axis:"#b4c0d9",zero:"#6e7b96",grid:"#27324a",
          x:"#58a6ff",pole:"#ff6b6b",zer:"#3ddc97",
          roc:"rgba(88,166,255,0.14)",rocLine:"#58a6ff",jw:"#b794ff",glow:14}
};

let darkMode=!!(window.matchMedia &&
    window.matchMedia("(prefers-color-scheme: dark)").matches);
let C=themes.light;
const themeBtn=$("#theme");

function applyTheme(){
    C=darkMode?themes.dark:themes.light;
    root.classList.toggle("dark",darkMode);
    themeBtn.textContent=darkMode?"☀ LIGHT MODE":"🌙 DARK MODE";
}

themeBtn.addEventListener("click",()=>{
    darkMode=!darkMode;
    applyTheme();
    render();
});

applyTheme();

// ======================================
// MATHEMATICS: x(t), X(s), poles and zeros
// ======================================

function num(v){
    const r=Math.round(v*1e4)/1e4;
    return String(r).replace("-","−");
}

function fact(n){ let f=1; for(let i=2;i<=n;i++) f*=i; return f; }

function xValue(t){

    if(t<0) return 0;

    const A=sig.A, a=sig.a, w=sig.w;
    let v;

    switch(sig.type){
        case "step": v=A; break;
        case "ramp": v=A*t; break;
        case "tn":   v=A*Math.pow(t,sig.n)*Math.exp(-a*t); break;
        case "exp":  v=A*Math.exp(-a*t); break;
        case "cos":  v=A*Math.cos(w*t); break;
        case "sin":  v=A*Math.sin(w*t); break;
        case "dcos": v=A*Math.exp(-a*t)*Math.cos(w*t); break;
        case "dsin": v=A*Math.exp(-a*t)*Math.sin(w*t); break;
        default:     v=0;
    }

    // very large values are not drawn
    return (Number.isFinite(v)&&Math.abs(v)<=1e6)?v:NaN;
}

// ---------- text helpers ----------

const coefA=()=>sig.A===1?"":(sig.A===-1?"−":num(sig.A));

function expT(){            // e^(-a t) as text (empty when a = 0)
    return sig.a===0?"":"e<sup>"+num(-sig.a)+"t</sup>";
}

function sPlus(a){          // s + a
    if(a===0) return "s";
    return a>0?"s + "+num(a):"s − "+num(-a);
}

function frac(n,d){
    return '<span class="frac"><span>'+n+'</span><span>'+d+'</span></span>';
}

// x(t) with the actual numbers
function xText(){

    const w=num(sig.w), A=coefA(), e=expT();

    switch(sig.type){
        case "imp":  return "x(t) = "+A+"δ(t)";
        case "step": return "x(t) = "+A+"u(t)";
        case "ramp": return "x(t) = "+A+"t u(t)";
        case "tn":   return "x(t) = "+A+(sig.n===0?"":(sig.n===1?"t":"t<sup>"+sig.n+"</sup>"))+e+" u(t)";
        case "exp":  return "x(t) = "+A+e+" u(t)";
        case "cos":  return "x(t) = "+A+"cos("+w+"t) u(t)";
        case "sin":  return "x(t) = "+A+"sin("+w+"t) u(t)";
        case "dcos": return "x(t) = "+A+e+"cos("+w+"t) u(t)";
        default:     return "x(t) = "+A+e+"sin("+w+"t) u(t)";
    }
}

// X(s) as an HTML formula
function XsHTML(){

    const A=sig.A, a=sig.a, w=sig.w;
    const sa=sPlus(a);
    const w2=num(w*w);

    // numerator with the amplitude in front of an s-expression
    const withA=(expr,paren)=>{
        if(A===1) return expr;
        if(A===-1) return paren?"−("+expr+")":"−"+expr;
        return num(A)+(paren?"("+expr+")":expr);
    };

    let body;

    switch(sig.type){
        case "imp":  body=num(A); break;
        case "step": body=frac(num(A),"s"); break;
        case "ramp": body=frac(num(A),"s<sup>2</sup>"); break;
        case "tn":   body=frac(num(A*fact(sig.n)),
                               (a===0?"s":"("+sa+")")+(sig.n===0?"":"<sup>"+(sig.n+1)+"</sup>")); 
                     if(sig.n===0) body=frac(num(A),sa);
                     break;
        case "exp":  body=frac(num(A),sa); break;
        case "cos":  body=frac(withA("s",false),"s<sup>2</sup> + "+w2); break;
        case "sin":  body=frac(num(A*w),"s<sup>2</sup> + "+w2); break;
        case "dcos": body=frac(withA(sa,true),(a===0?"s":"("+sa+")")+"<sup>2</sup> + "+w2); break;
        default:     body=frac(num(A*w),(a===0?"s":"("+sa+")")+"<sup>2</sup> + "+w2);
    }

    return "X(s) = "+body;
}

// poles / zeros as groups: {re, im (>=0), pair (±im), mult}
function pzData(){

    const a=sig.a, w=sig.w;
    let zeros=[], poles=[];

    switch(sig.type){
        case "imp":  break;
        case "step": poles=[{re:0,im:0,pair:false,mult:1}]; break;
        case "ramp": poles=[{re:0,im:0,pair:false,mult:2}]; break;
        case "tn":   poles=[{re:-a,im:0,pair:false,mult:sig.n+1}]; break;
        case "exp":  poles=[{re:-a,im:0,pair:false,mult:1}]; break;
        case "cos":  zeros=[{re:0,im:0,pair:false,mult:1}];
                     poles=[{re:0,im:w,pair:true,mult:1}]; break;
        case "sin":  poles=[{re:0,im:w,pair:true,mult:1}]; break;
        case "dcos": zeros=[{re:-a,im:0,pair:false,mult:1}];
                     poles=[{re:-a,im:w,pair:true,mult:1}]; break;
        default:     poles=[{re:-a,im:w,pair:true,mult:1}];
    }

    return {zeros,poles};
}

function multWord(m){
    return m===1?"simple":(m===2?"double":(m===3?"triple":"order "+m));
}

function locText(g){
    if(g.pair) return "s = "+(g.re===0?"":num(g.re)+" ")+"± j"+num(g.im);
    return "s = "+num(g.re);
}

function listHTML(groups,kind){

    if(groups.length===0) return '<div class="none">none</div>';

    let h="<ul>";

    groups.forEach(g=>{
        let txt=locText(g);
        if(g.mult>1) txt+="   ("+multWord(g.mult)+" "+kind+")";
        h+="<li>"+txt+"</li>";
    });

    return h+"</ul>";
}

function countOf(groups){
    return groups.reduce((s,g)=>s+g.mult*(g.pair?2:1),0);
}

// region of convergence: Re{s} > sigma0
function rocSigma(poles){
    if(poles.length===0) return -Infinity;
    return Math.max(...poles.map(g=>g.re));
}

// ======================================
// CANVAS HELPERS
// ======================================

const cTime=$("#cTime"), cPZ=$("#cPZ");
const dpr=()=>window.devicePixelRatio||1;

function sizeCanvas(cv,w,h){
    cv._w=w; cv._h=h;
    cv.style.width=w+"px";
    cv.style.height=h+"px";
    cv.width=Math.round(w*dpr());
    cv.height=Math.round(h*dpr());
}

function fit(){

    const w1=Math.max(240,Math.floor(cTime.parentElement.clientWidth-28));
    sizeCanvas(cTime,w1,Math.round(Math.min(260,Math.max(190,w1*0.6))));

    const w2=Math.max(260,Math.floor(cPZ.parentElement.clientWidth-28));
    sizeCanvas(cPZ,w2,Math.round(Math.min(520,Math.max(340,w2*0.62))));
}

function niceTicks(a,b,n){

    const raw=(b-a)/n;
    const mag=Math.pow(10,Math.floor(Math.log10(raw)));
    const r=raw/mag;
    const step=(r<=1?1:r<=2?2:r<=5?5:10)*mag;

    const ticks=[];
    for(let v=Math.ceil(a/step-1e-9)*step; v<=b+1e-9; v+=step){
        ticks.push(Math.abs(v)<step*1e-9?0:v);
    }

    return {ticks,step};
}

function fmt(v,step){

    if(v===0) return "0";

    if(Math.abs(v)>=1e5 || Math.abs(v)<1e-3)
        return v.toExponential(1).replace("e+","e");

    const dec=Math.max(0,-Math.floor(Math.log10(step)+1e-9));
    return v.toFixed(Math.min(dec,6));
}

function padRange(lo,hi){

    lo=Math.min(0,lo);
    hi=Math.max(0,hi);

    let span=hi-lo;
    if(span<1e-12){ lo=-1; hi=1; span=2; }

    return [lo-0.12*span, hi+0.12*span];
}

function niceCeil(v){
    const mag=Math.pow(10,Math.floor(Math.log10(v)));
    const r=v/mag;
    return (r<=1?1:r<=2?2:r<=2.5?2.5:r<=5?5:10)*mag;
}

// ======================================
// TIME-DOMAIN PLOT
// ======================================

function drawTime(){

    const cv=cTime, W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    // samples
    const N=1600;
    const ts=new Float64Array(N+1), vs=new Float64Array(N+1);

    for(let i=0;i<=N;i++){
        ts[i]=view.tmin+(view.tmax-view.tmin)*i/N;
        vs[i]=(sig.type==="imp")?0:xValue(ts[i]);
    }

    let lo=0, hi=0;

    if(sig.type==="imp"){
        lo=Math.min(0,sig.A); hi=Math.max(0,sig.A);
    }
    else{
        for(let i=0;i<=N;i++){
            const v=vs[i];
            if(Number.isNaN(v)) continue;
            if(v<lo) lo=v;
            if(v>hi) hi=v;
        }
    }

    const [ymin,ymax]=padRange(lo,hi);

    const L=52, R=W-14, T=14, B=H-36;
    const X=t=>L+(t-view.tmin)/(view.tmax-view.tmin)*(R-L);
    const Y=v=>B-(v-ymin)/(ymax-ymin)*(B-T);

    const xt=niceTicks(view.tmin,view.tmax,Math.max(3,Math.floor((R-L)/70)));
    const yt=niceTicks(ymin,ymax,Math.max(3,Math.floor((B-T)/45)));

    ctx.font="11px Arial";
    ctx.lineWidth=1;

    xt.ticks.forEach(v=>{
        const x=X(v);
        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(x,T); ctx.lineTo(x,B); ctx.stroke();
        ctx.fillStyle=C.tick;
        ctx.textAlign="center";
        ctx.fillText(fmt(v,xt.step),x,B+15);
    });

    yt.ticks.forEach(v=>{
        const y=Y(v);
        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(L,y); ctx.lineTo(R,y); ctx.stroke();
        ctx.fillStyle=C.tick;
        ctx.textAlign="right";
        ctx.fillText(fmt(v,yt.step),L-6,y+4);
    });

    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.6;
    ctx.beginPath();
    if(ymin<=0&&ymax>=0){ ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0)); }
    if(view.tmin<=0&&view.tmax>=0){ ctx.moveTo(X(0),T); ctx.lineTo(X(0),B); }
    ctx.stroke();

    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.4;
    ctx.beginPath();
    ctx.moveTo(L,T); ctx.lineTo(L,B); ctx.lineTo(R,B);
    ctx.stroke();

    ctx.fillStyle=C.text;
    ctx.textAlign="center";
    ctx.font="12px Arial";
    ctx.fillText("t  (seconds)",(L+R)/2,H-6);

    ctx.save();
    ctx.beginPath(); ctx.rect(L,T,R-L,B-T); ctx.clip();
    ctx.lineCap="round";

    ctx.shadowColor=C.x;
    ctx.shadowBlur=C.glow;
    ctx.strokeStyle=C.x;
    ctx.fillStyle=C.x;
    ctx.lineWidth=3;

    if(sig.type==="imp"){

        if(view.tmin<=0&&view.tmax>=0){

            const x0=X(0), y0=Y(0), y1=Y(sig.A);
            const dir=y1<y0?1:-1;

            ctx.lineWidth=3.6;
            ctx.beginPath(); ctx.moveTo(x0,y0); ctx.lineTo(x0,y1+dir*8); ctx.stroke();

            ctx.beginPath();
            ctx.moveTo(x0,y1);
            ctx.lineTo(x0-7,y1+dir*16);
            ctx.lineTo(x0+7,y1+dir*16);
            ctx.closePath();
            ctx.fill();
        }
    }
    else{

        ctx.beginPath();
        let pen=false;

        for(let i=0;i<=N;i++){

            const v=vs[i];
            if(Number.isNaN(v)){ pen=false; continue; }

            const x=X(ts[i]), y=Math.max(-1e5,Math.min(1e5,Y(v)));

            if(!pen){ ctx.moveTo(x,y); pen=true; } else ctx.lineTo(x,y);
        }

        ctx.stroke();
    }

    ctx.restore();

    if(sig.type==="imp"){
        ctx.fillStyle=C.x;
        ctx.font="bold 12px Arial";
        ctx.textAlign="left";
        if(view.tmin<=0&&view.tmax>=0)
            ctx.fillText("("+num(sig.A)+")",X(0)+10,Math.max(T+14,Math.min(B-6,Y(sig.A)+4)));
    }
}

// ======================================
// POLE-ZERO PLOT
// ======================================

function drawPZ(pz,sigma0){

    const cv=cPZ, W=cv._w, H=cv._h;
    const ctx=cv.getContext("2d");

    ctx.setTransform(dpr(),0,0,dpr(),0,0);
    ctx.clearRect(0,0,W,H);
    ctx.lineJoin="round";

    // axis range (same scale on both axes)
    let m=1;
    pz.zeros.concat(pz.poles).forEach(g=>{
        m=Math.max(m,Math.abs(g.re),Math.abs(g.im));
    });

    const Rg=niceCeil(m*1.45);

    // square plotting area, centred
    const side=Math.min(W-120,H-70);
    const L=(W-side)/2, R=L+side, T=18, B=T+side;

    const X=v=>L+(v+Rg)/(2*Rg)*side;
    const Y=v=>B-(v+Rg)/(2*Rg)*side;

    // ----- region of convergence (shaded)
    const rx=(sigma0===-Infinity)?L:Math.min(R,Math.max(L,X(sigma0)));

    ctx.fillStyle=C.roc;
    ctx.fillRect(rx,T,R-rx,B-T);

    // ----- grid and ticks
    const tk=niceTicks(-Rg,Rg,6);

    ctx.font="11px Arial";
    ctx.lineWidth=1;

    tk.ticks.forEach(v=>{

        ctx.strokeStyle=C.grid;
        ctx.beginPath(); ctx.moveTo(X(v),T); ctx.lineTo(X(v),B); ctx.stroke();
        ctx.beginPath(); ctx.moveTo(L,Y(v)); ctx.lineTo(R,Y(v)); ctx.stroke();

        if(v!==0){
            ctx.fillStyle=C.tick;
            ctx.textAlign="center";
            ctx.fillText(fmt(v,tk.step),X(v),Y(0)+15);
            ctx.textAlign="right";
            ctx.fillText(fmt(v,tk.step)+"j",X(0)-6,Y(v)+4);
        }
    });

    // frame
    ctx.strokeStyle=C.zero;
    ctx.lineWidth=1.2;
    ctx.strokeRect(L,T,side,side);

    // axes
    ctx.strokeStyle=C.axis;
    ctx.lineWidth=1.8;
    ctx.beginPath();
    ctx.moveTo(L,Y(0)); ctx.lineTo(R,Y(0));
    ctx.stroke();

    // the jω-axis is highlighted
    ctx.strokeStyle=C.jw;
    ctx.lineWidth=2.2;
    ctx.beginPath();
    ctx.moveTo(X(0),T); ctx.lineTo(X(0),B);
    ctx.stroke();

    ctx.fillStyle=C.text;
    ctx.font="bold 14px Arial";
    ctx.textAlign="left";
    var sl=(W-R>80)?"σ  (Re{s})":"σ";
    ctx.fillText(sl,R+8,Y(0)+4);

    ctx.textAlign="center";
    ctx.fillStyle=C.jw;
    ctx.fillText("jω  (Im{s})",X(0),T-4);

    // ----- ROC boundary and label
    if(sigma0!==-Infinity){
        ctx.save();
        ctx.strokeStyle=C.rocLine;
        ctx.lineWidth=1.8;
        ctx.setLineDash([7,5]);
        ctx.beginPath(); ctx.moveTo(rx,T); ctx.lineTo(rx,B); ctx.stroke();
        ctx.restore();
    }

    ctx.fillStyle=C.rocLine;
    ctx.font="bold 13px Arial";
    ctx.textAlign="right";
    ctx.fillText(sigma0===-Infinity?"ROC: entire s-plane":"ROC: Re{s} > "+num(sigma0),R-8,B-10);

    // ----- zeros (circles) and poles (crosses)
    function positions(g){
        return g.pair ? [[g.re,g.im],[g.re,-g.im]] : [[g.re,g.im]];
    }

    function badge(x,y,m){
        if(m<=1) return;
        ctx.font="bold 12px Arial";
        ctx.textAlign="left";
        ctx.fillText("("+m+")",x+10,y-10);
    }

    pz.zeros.forEach(g=>{
        positions(g).forEach(([re,im])=>{
            const x=X(re), y=Y(im);
            ctx.save();
            ctx.shadowColor=C.zer; ctx.shadowBlur=C.glow;
            ctx.strokeStyle=C.zer; ctx.fillStyle=C.zer;
            ctx.lineWidth=2.8;
            ctx.beginPath(); ctx.arc(x,y,7.5,0,2*Math.PI); ctx.stroke();
            ctx.restore();
            ctx.fillStyle=C.zer;
            badge(x,y,g.mult);
        });
    });

    pz.poles.forEach(g=>{
        positions(g).forEach(([re,im])=>{
            const x=X(re), y=Y(im), d=7;
            ctx.save();
            ctx.shadowColor=C.pole; ctx.shadowBlur=C.glow;
            ctx.strokeStyle=C.pole; ctx.fillStyle=C.pole;
            ctx.lineWidth=3.2; ctx.lineCap="round";
            ctx.beginPath();
            ctx.moveTo(x-d,y-d); ctx.lineTo(x+d,y+d);
            ctx.moveTo(x+d,y-d); ctx.lineTo(x-d,y+d);
            ctx.stroke();
            ctx.restore();
            ctx.fillStyle=C.pole;
            badge(x,y,g.mult);
        });
    });

    if(pz.zeros.length===0&&pz.poles.length===0){
        ctx.fillStyle=C.tick;
        ctx.font="bold 14px Arial";
        ctx.textAlign="center";
        ctx.fillText("X(s) = constant: no poles and no zeros",(L+R)/2,(T+B)/2-30);
    }
}

// ======================================
// RENDER
// ======================================

function render(){

    const pz=pzData();
    const s0=rocSigma(pz.poles);

    $("#formula").innerHTML=xText();
    $("#xs").innerHTML=XsHTML();

    $("#pill_roc").textContent=(s0===-Infinity)
        ? "ROC: entire s-plane"
        : "ROC: Re{s} > "+num(s0);

    $("#pill_jw").textContent=(s0===-Infinity||s0<0)
        ? "jω-axis is inside the ROC"
        : (s0===0 ? "jω-axis is on the ROC boundary" : "jω-axis is outside the ROC");

    $("#zlist").innerHTML=listHTML(pz.zeros,"zero");
    $("#plist").innerHTML=listHTML(pz.poles,"pole");

    $("#counts").textContent="Number of zeros: "+countOf(pz.zeros)+"   |   Number of poles: "+countOf(pz.poles)+
        "   (repeated roots counted with their multiplicity)";

    drawTime();
    drawPZ(pz,s0);
}

// ======================================
// RESPONSIVE RESIZING
// ======================================

function resize(){ fit(); render(); }

if(typeof ResizeObserver!=="undefined"){
    new ResizeObserver(resize).observe($(".layout"));
}
window.addEventListener("resize",resize);

// initial display
fit();
render();

})();
</script>

</div>
"""

html = html.replace("ROOT_ID", uid)

# Everything runs in the browser (JavaScript), so changing a value
# never triggers a Streamlit rerun.
if hasattr(st, "iframe"):
    st.iframe(html, height=1500)
else:
    components.html(html, height=1500, scrolling=True)
