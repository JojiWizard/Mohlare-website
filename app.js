/* Mohlare Group - front-end behaviour (no backend yet) */
(function(){
  const $=s=>document.querySelector(s);

  /* ---- cinematic intro (home page only, once per visit) ---- */
  const intro=$("#intro");
  if(intro){
    const skip=sessionStorage.getItem("mg-intro")||location.hash==="#divisions";
    const nm=$("#nm");
    "MOHLARE GROUP".split("").forEach((c,i)=>{
      const s=document.createElement("span");
      s.className=c===" "?"sp":"m";
      if(c!==" "){const k=document.createElement("i");k.textContent=c;s.appendChild(k)}
      s.style.setProperty("--i",i);nm.appendChild(s);
    });
    const close=()=>{intro.classList.add("gone");sessionStorage.setItem("mg-intro","1");document.body.style.overflow="";scrollTo(0,0)};
    if(skip){intro.style.display="none"}
    else{
      document.body.style.overflow="hidden";
      $("#enter").addEventListener("click",close);
      addEventListener("keydown",e=>{if(e.key==="Enter"&&!intro.classList.contains("gone"))close()});
    }
  }

  /* ---- fade out before navigating, fade in on arrival ---- */
  document.addEventListener("click",e=>{
    const a=e.target.closest("a[href]");
    if(!a||a.target==="_blank"||a.hasAttribute("download"))return;
    const u=new URL(a.href,location.href);
    if(u.origin!==location.origin||u.protocol==="mailto:"||(u.pathname===location.pathname&&u.hash))return;
    e.preventDefault();
    document.body.classList.add("leaving");
    setTimeout(()=>{location.href=a.href},450);
  });
  addEventListener("pageshow",e=>{if(e.persisted)document.body.classList.remove("leaving")});

  /* ---- scroll reveal ---- */
  const io=new IntersectionObserver(es=>es.forEach(x=>{if(x.isIntersecting){x.target.classList.add("in");io.unobserve(x.target)}}),{threshold:.15});
  document.querySelectorAll(".rv").forEach(el=>io.observe(el));
})();
