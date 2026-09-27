# -*- coding: utf-8 -*-
"""Post 3 — «Növbə» booking SaaS, Frame.io-style: near-black ground, violet→blue
glow, glass arcs, product UI crops, one giant stat per slide, pricing tiers."""
import pathlib

S = 1080
BG, BG2, VIO, BLU, MAG = '#08080F', '#0F0F1A', '#7C5CFF', '#3D7BFF', '#C77DFF'
TXT, MUT, LINE, GLASS = '#F2F2F7', '#8B8B9E', '#23233A', '#FFFFFF'
H, B, M = 'Archivo', 'Inter', 'Inter'

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def T(x,y,s,size,w=400,fill=TXT,font=B,anchor='start',ls=0,op=1):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(s)}</text>')
def R(x,y,w,h,fill,rx=0,op=1,extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{op}" {extra}/>'
def glass(x,y,w,h,rx=16): return R(x,y,w,h,GLASS,rx,.05,extra=f'stroke="{GLASS}" stroke-opacity=".10"')

DEFS = f'''<defs>
 <filter id="sh" x="-30%" y="-30%" width="160%" height="180%"><feGaussianBlur stdDeviation="26"/></filter>
 <filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="60"/></filter>
 <filter id="soft" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
 <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".8" numOctaves="2" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>
 <linearGradient id="vb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{VIO}"/><stop offset="1" stop-color="{BLU}"/></linearGradient>
 <linearGradient id="arc" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{MAG}" stop-opacity=".9"/><stop offset=".5" stop-color="{VIO}" stop-opacity=".55"/><stop offset="1" stop-color="{BLU}" stop-opacity=".15"/></linearGradient>
 <linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".12"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
 <radialGradient id="vig" cx=".5" cy=".5" r=".8"><stop offset=".5" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".6"/></radialGradient>
</defs>'''

def ground(): return R(0,0,S,S,BG)
def grain(op=.05): return f'<rect width="{S}" height="{S}" filter="url(#grain)" opacity="{op}"/>'
def glow(cx,cy,r,c=VIO,op=.35): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity="{op}" filter="url(#glow)"/>'
def arc(cx,cy,rx,ry,rot=0,op=1):
    """Frame.io's glass bowl: a thick elliptical ring with gradient + highlight."""
    return (f'<g transform="rotate({rot} {cx} {cy})" opacity="{op}">'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#arc)" stroke-width="{rx*.22}" filter="url(#soft)"/>'
            f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="#fff" stroke-opacity=".25" stroke-width="2"/>'
            f'</g>')

# ── devices ─────────────────────────────────────────────────────────────────
def laptop(x,y,w,screen):
    b=14; sw=w-2*b; sh=sw*750/1200; h=sh+2*b; cid=f'l{int(x)}{int(y)}'
    g=f'<ellipse cx="{x+w/2}" cy="{y+h+42}" rx="{w*.52}" ry="40" fill="#000" opacity=".7" filter="url(#sh)"/>'
    g+=R(x,y,w,h,'#0b0b12',22,extra=f'stroke="{LINE}" stroke-width="2"')
    g+=f'<clipPath id="{cid}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="8"/></clipPath>'
    g+=f'<g clip-path="url(#{cid})"><g transform="translate({x+b} {y+b}) scale({sw/1200})">{screen}</g></g>'
    g+=R(x+b,y+b,sw,sh,'url(#gloss)',8)+R(x-26,y+h,w+52,20,'#14141f',6)+R(x-26,y+h,w+52,4,'#2a2a3a',2)
    return g
def phone(x,y,w,screen,rot=0):
    h=w*844/390+24; b=12; sw=w-2*b; sh=w*844/390; cx,cy=x+w/2,y+h/2; cid=f'p{int(x)}{int(y)}'
    g=f'<g transform="rotate({rot} {cx} {cy})"><ellipse cx="{cx}" cy="{y+h+18}" rx="{w*.55}" ry="26" fill="#000" opacity=".6" filter="url(#sh)"/>'
    g+=R(x,y,w,h,'#0b0b12',w*.16,extra=f'stroke="{LINE}" stroke-width="2"')
    g+=f'<clipPath id="{cid}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="{w*.12}"/></clipPath>'
    g+=f'<g clip-path="url(#{cid})"><g transform="translate({x+b} {y+b}) scale({sw/390})">{screen}</g></g>'
    g+=R(cx-w*.18,y+b+10,w*.36,22,'#0b0b12',11)+R(x+b,y+b,sw,sh,'url(#gloss)',w*.12)+'</g>'
    return g

# ── product UI (1200 x 750) ─────────────────────────────────────────────────
def nav():
    g=R(0,0,1200,750,BG)
    g+=f'<circle cx="24" cy="46" r="10" fill="url(#vb)"/>'+T(44,54,'Növbə',24,700,TXT,H)
    for i,it in enumerate(['Məhsul','Həllər','Qiymət','Bloq']): g+=T(420+i*110,52,it,16,500,TXT,B,op=.7)
    g+=T(1000,52,'Giriş',16,500,TXT,B,op=.7)+R(1050,28,110,44,'url(#vb)',22)+T(1105,56,'Başla',15,700,TXT,B,anchor='middle')
    return g

def dash(x,y,w,h,scale=1):
    """Booking dashboard: sidebar, KPIs, week calendar with coloured blocks."""
    g=R(x,y,w,h,BG2,14,extra=f'stroke="{LINE}" stroke-width="1"')
    g+=R(x,y,150,h,'#0C0C16',14)
    for i,it in enumerate(['Təqvim','Müştərilər','Xidmətlər','Hesabat','Ayarlar']):
        g+=(R(x+14,y+60+i*40,122,30,VIO,8,.9) if i==0 else '')+T(x+26,y+80+i*40,it,13,500,TXT,B,op=1 if i==0 else .6)
    for i,(k,v) in enumerate([('Bu gün','24 rezerv'),('Doluluq','86%'),('Gəlmədi','2'),('Gəlir','1 240 ₼')]):
        cx=x+170+i*((w-190)/4)
        g+=glass(cx,y+20,(w-190)/4-12,70,10)+T(cx+14,y+42,k,11,500,MUT,B)+T(cx+14,y+68,v,18,700,TXT,H)
    cal_y=y+110; cw=(w-190)/7
    for d,day in enumerate(['B.e','Ç.a','Ç','C.a','C','Ş','B']):
        cx=x+170+d*cw
        g+=T(cx+cw/2,cal_y+16,day,11,600,MUT,B,anchor='middle')
        g+=R(cx,cal_y+26,cw-6,h-150,'#0C0C16',8)
    blocks=[(0,40,60,VIO,'Saç kəsimi'),(0,120,50,BLU,'Manikür'),(1,30,80,MAG,'Boyama'),(2,60,40,VIO,'Üz baxımı'),(2,120,60,BLU,'Masaj'),
            (3,40,70,VIO,'Saç kəsimi'),(4,30,50,MAG,'Konsultasiya'),(4,100,80,VIO,'Boyama'),(5,50,60,BLU,'Manikür'),(5,130,40,MAG,'Kirpik')]
    for d,off,ln,c,lab in blocks:
        cx=x+170+d*cw; by=cal_y+30+off
        if by+ln<y+h-16:
            g+=R(cx+4,by,cw-14,ln,c,6,.85)+T(cx+12,by+18,lab,10,600,TXT,B)
    return g

def scr_hero():
    g=nav()
    g+=glow(900,400,340,VIO,.5)
    g+=T(60,236,'Bütün',60,600,TXT,H)+T(60,300,'rezervasiyalar',60,600,TXT,H)+T(60,364,'bir yerdə.',60,600,MAG,H)
    g+=T(60,416,'Salon, klinika və restoran üçün onlayn növbə,',18,400,MUT,B)
    g+=T(60,442,'xatırlatma və müştəri bazası.',18,400,MUT,B)
    g+=R(60,484,150,50,'url(#vb)',25)+T(135,516,'Pulsuz başla',15,700,TXT,B,anchor='middle')
    g+=R(224,484,170,50,'none',25,extra=f'stroke="{LINE}" stroke-width="1.5"')+T(309,516,'Demo izlə  ▶',15,600,TXT,B,anchor='middle')
    g+=dash(600,130,700,560)
    return g

def scr_stat(num,sub1,sub2):
    g=nav()+glow(600,420,380,VIO,.35)
    g+=arc(780,560,360,300,-18,.9)
    g+=T(600,300,num,180,600,TXT,H,anchor='middle',ls=-6)
    g+=T(600,380,sub1,32,600,TXT,H,anchor='middle')+T(600,420,sub2,32,600,TXT,H,anchor='middle')
    return g

def scr_pricing():
    g=nav()+glow(600,200,300,BLU,.3)
    g+=T(600,160,'Sizə uyğun plan.',54,600,TXT,H,anchor='middle')
    plans=[('Pulsuz','0 ₼','1 işçi · 50 rezerv/ay',False),('Pro','29 ₼','5 işçi · limitsiz · SMS',True),('Biznes','79 ₼','filiallar · hesabat · API',False)]
    for i,(n,p,d,hi) in enumerate(plans):
        x=150+i*310
        g+=(R(x,220,280,420,'url(#vb)',18,.18) if hi else glass(x,220,280,420,18))
        g+=R(x,220,280,420,'none',18,extra=f'stroke="{VIO if hi else LINE}" stroke-width="{2 if hi else 1}"')
        g+=T(x+28,270,n,20,600,MUT,B)+T(x+28,330,p,44,700,TXT,H)
        g+=T(x+28,372,d+' · ayda',14,400,MUT,B)
        for j,f in enumerate(['Onlayn növbə','WhatsApp xatırlatma','Müştəri bazası','Hesabatlar'][:2+i]):
            g+=f'<circle cx="{x+36}" cy="{412+j*30}" r="5" fill="url(#vb)"/>'+T(x+52,417+j*30,f,14,400,TXT,B,op=.85)
        g+=R(x+28,580,224,44,'url(#vb)' if hi else 'none',22,extra='' if hi else f'stroke="{LINE}" stroke-width="1.5"')
        g+=T(x+140,608,'Seç',14,700,TXT,B,anchor='middle')
    return g

def mob():
    g=R(0,0,390,844,BG)+glow(200,300,220,VIO,.45)
    g+=f'<circle cx="34" cy="60" r="9" fill="url(#vb)"/>'+T(52,67,'Növbə',20,700,TXT,H)
    g+=T(30,150,'Sabah 14:30',34,600,TXT,H)+T(30,186,'Saç kəsimi · Ləman',16,400,MUT,B)
    g+=glass(30,220,330,120,16)+T(50,256,'Növbəti müştəri',12,500,MUT,B)+T(50,294,'Nigar Ə.',24,700,TXT,H)+T(50,320,'15:30 · Boyama · 90 dəq',14,400,MUT,B)
    for i,(t,n,c) in enumerate([('16:30','Aysel M.',BLU),('17:00','Günel R.',MAG),('18:00','Sevinc T.',VIO)]):
        y=370+i*88
        g+=glass(30,y,330,72,14)+R(30,y+14,4,44,c,2)+T(52,y+30,t,13,600,MUT,B)+T(52,y+54,n,18,600,TXT,B)
    g+=R(30,680,330,56,'url(#vb)',28)+T(195,715,'+ Yeni rezerv',16,700,TXT,B,anchor='middle')
    return g

# ── slides ──────────────────────────────────────────────────────────────────
def chrome(n,label,thesis=None):
    g=T(80,108,label,16,600,MAG,M,ls=5)+T(S-80,108,f'@hastudio.az   ·   {n} / 7',16,500,TXT,M,anchor='end',ls=2,op=.6)
    if thesis: g+=T(80,S-84,thesis,34,600,TXT,H)
    return g

def s1():
    g=ground()+glow(540,260,380,VIO,.45)+glow(900,900,300,BLU,.3)+arc(-40,980,420,340,-15,.8)+grain()
    g+=T(80,108,'KEYS  ·  SAAS MƏHSUL SAYTI',16,600,MAG,M,ls=5)+T(S-80,108,'@hastudio.az   ·   1 / 7',16,500,TXT,M,anchor='end',ls=2,op=.6)
    g+=f'<circle cx="440" cy="235" r="26" fill="url(#vb)"/>'+T(486,254,'Növbə',60,700,TXT,H)
    g+=T(540,330,'REZERVASİYA PLATFORMASI ÜÇÜN SAYT',15,600,MUT,M,anchor='middle',ls=5)
    g+=laptop(120,400,840,scr_hero())
    return g
def s2():
    g=ground()+f'<g transform="translate(0 165) scale(.9)">{scr_hero()}</g>'+R(0,0,S,S,'url(#vig)')+grain()
    g+=chrome(2,'HERO','Bir cümlə. Bir düymə. Məhsul görünür.')
    return g
def s3():
    g=ground()+glow(540,500,420,VIO,.28)+arc(560,640,420,330,-14,1)+grain()
    g+=T(540,470,'3×',220,700,TXT,H,anchor='middle',ls=-10)
    g+=T(540,560,'daha az gəlməyən müştəri',36,600,TXT,H,anchor='middle')
    g+=T(540,606,'WhatsApp xatırlatması sayəsində',20,400,MUT,B,anchor='middle')
    g+=chrome(3,'STATİSTİKA','Rəqəm sübutdur, sifət deyil.')
    return g
def s4():
    g=ground()+glow(300,300,300,BLU,.3)+grain()
    g+=f'<g transform="translate(80 250)">{dash(0,0,920,560)}</g>'
    g+=chrome(4,'MƏHSUL','İnterfeys saytın özündə görünür, PDF-də yox.')
    return g
def s5():
    g=ground()+glow(700,500,300,MAG,.25)+arc(920,180,300,240,20,.7)+grain()
    g+=phone(190,240,300,mob(),rot=-8)+phone(560,300,300,mob(),rot=6)
    g+=chrome(5,'MOBİL','Usta telefondan idarə edir.')
    return g
def s6():
    g=ground()+grain()+laptop(80,250,920,scr_pricing())
    g+=chrome(6,'PLANLAR','Üç seçim, ortadakı vurğulu.')
    return g
def s7():
    g=ground()+glow(540,420,360,VIO,.3)+arc(540,1000,500,380,0,.6)+grain()
    g+=('<g transform="translate(482 200) scale(.95)" fill="%s"><rect x="12" y="22" width="11" height="56"/><rect x="41" y="22" width="11" height="56"/>'
        '<polygon points="84,22 93,22 69,78 58,78"/><polygon points="84,22 93,22 118,78 107,78"/><polygon points="12,44 102.82,44 107.73,55 12,55"/></g>'%TXT)
    g+=T(540,420,'Startapınız üçün',62,600,TXT,H,anchor='middle')+T(540,492,'belə bir sayt?',62,600,MAG,H,anchor='middle')
    g+=T(540,570,'Landing, məhsul UI, planlar — bir həftədə canlıda.',20,400,MUT,B,anchor='middle')
    g+=T(540,700,'099 600 06 78',40,700,TXT,H,anchor='middle')
    g+=T(540,742,'hastudio-az.vercel.app  ·  hastudio.az@gmail.com',16,500,MUT,M,anchor='middle',ls=2)
    g+=T(80,108,'HA STUDIO',16,600,MAG,M,ls=5)+T(S-80,108,'@hastudio.az   ·   7 / 7',16,500,TXT,M,anchor='end',ls=2,op=.6)
    return g

for i,body in enumerate([s1(),s2(),s3(),s4(),s5(),s6(),s7()],1):
    pathlib.Path(f'novbe-{i}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">{DEFS}{body}</svg>',encoding='utf-8')
print('7 written')
