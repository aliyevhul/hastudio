# -*- coding: utf-8 -*-
"""Rəşid & Aysu wedding-invitation site — 6-slide case carousel, 4:5.
Same skeleton as the Doggie Couture case: cover → task/what we did → signature
feature → invitation → countdown & venue → CTA. Real screenshots inside frames."""
import pathlib, base64, sys
W = pathlib.Path(sys.argv[1]); OUT = pathlib.Path('.')
S_W, S_H, M = 1080, 1350, 80
NIGHT, COCOA, PARCH, CHAMP, GOLD, GRAPE, INK, MUT = '#0F1627', '#2A1F1A', '#EAD9BE', '#F3E6D0', '#C9A75B', '#6B3F7A', '#2B2118', '#7A6652'
SER, SANS = 'Cormorant Garamond', 'Manrope'

def esc(t): return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def T(x,y,s,size,w=400,fill=INK,font=SANS,anchor='start',ls=0,op=1,style='normal'):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" font-style="{style}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(s)}</text>')
def R(x,y,w,h,fill,rx=0,op=1,extra=''): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{op}" {extra}/>'
def P(x,y,lines,size,w=400,fill=INK,font=SANS,lh=40): return ''.join(T(x,y+i*lh,l,size,w,fill,font) for i,l in enumerate(lines))

_cache={}
def img64(name):
    if name not in _cache:
        _cache[name]='data:image/jpeg;base64,'+base64.b64encode((W/name).read_bytes()).decode()
    return _cache[name]
_n=[0]
def IMG(name,x,y,w,h,rx=0,crop=None,fit='cover'):
    """Place a screenshot, cover-fit, rounded. crop=(cx,cy,cw,ch) in source px (1536x674)."""
    _n[0]+=1; cid=f'c{_n[0]}'
    sw,sh=1536,674
    if crop: cx,cy,cw,ch=crop
    else: cx,cy,cw,ch=0,0,sw,sh
    sc=(max if fit=='cover' else min)(w/cw,h/ch); iw,ih=sw*sc,sh*sc
    ox=x-cx*sc-(cw*sc-w)/2; oy=y-cy*sc-(ch*sc-h)/2
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}"/></clipPath>'
            f'<g clip-path="url(#{cid})"><image href="{img64(name)}" x="{ox:.1f}" y="{oy:.1f}" width="{iw:.1f}" height="{ih:.1f}"/></g>')

DEFS='''<defs><filter id="sh" x="-20%" y="-20%" width="140%" height="160%"><feGaussianBlur stdDeviation="22"/></filter>
<linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".10"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient></defs>'''

def browser(x,y,w,h,name,crop=None,bar=PARCH):
    g=f'<rect x="{x}" y="{y+30}" width="{w}" height="{h}" rx="22" fill="#000" opacity=".35" filter="url(#sh)"/>'
    g+=R(x,y,w,h,bar,22)
    for i,c in enumerate(['#D9A59A','#D9C79A','#B9C9A0']): g+=f'<circle cx="{x+26+i*22}" cy="{y+22}" r="6" fill="{c}"/>'
    g+=R(x+110,y+11,w-140,22,'#fff',11,.6)
    g+=IMG(name,x,y+44,w,h-44,0,crop)
    g+=f'<clipPath id="b{x}{y}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22"/></clipPath>'
    return f'<g clip-path="url(#b{x}{y})">{g}</g>'

def phone(x,y,w,name,crop,rot=0):
    h=w*2.05; b=12; cx,cy=x+w/2,y+h/2
    g=f'<g transform="rotate({rot} {cx} {cy})"><rect x="{x}" y="{y+28}" width="{w}" height="{h}" rx="{w*.16}" fill="#000" opacity=".4" filter="url(#sh)"/>'
    g+=R(x,y,w,h,'#111',w*.16,extra='stroke="#3a3a3a" stroke-width="2"')
    if crop=='HERO':
        _n[0]+=1; cid=f'ph{_n[0]}'; sw,sh=w-2*b,h-2*b
        g+=f'<clipPath id="{cid}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="{w*.12}"/></clipPath><g clip-path="url(#{cid})">'
        band=sw*150/600
        g+=R(x+b,y+b,sw,band,'#0E1526')
        g+=IMG(name,x+b,y+b,sw,band,0,(470,20,600,150),fit='contain')   # full names + sky
        g+=IMG(name,x+b,y+b+band,sw,sh-band,0,(540,170,460,504))         # palace column
        g+='</g>'
    else:
        g+=IMG(name,x+b,y+b,w-2*b,h-2*b,w*.12,crop)
    g+=R(cx-w*.17,y+b+10,w*.34,20,'#111',10)+R(x+b,y+b,w-2*b,h-2*b,'url(#gloss)',w*.12)+'</g>'
    return g

def head(n,dark):
    fg=PARCH if dark else INK
    g=T(M,M+26,'Rəşid & Aysu',26,500,fg,SER,style='italic')
    g+=T(S_W-M,M+26,f'0{n} / 06',18,500,fg,SANS,anchor='end',ls=2,op=.7)
    return g
def logo_row(dark):
    fg=GOLD if dark else '#8B6550'
    return T(M,S_H-M+10,'@hastudio.az',18,500,fg,SANS,ls=1,op=.8)

# center column of a desktop shot ≈ what the phone shows (site is centred)
PH_HERO='HERO'; PH_ENV=(540,0,456,674)

def s1():
    g=R(0,0,S_W,S_H,NIGHT)+R(0,0,S_W,S_H,'#000',0,.0)
    g+=head(1,True)
    g+=T(M,262,'Keys',30,400,GOLD,SER,style='italic')
    g+=T(M,352,'Toy dəvətnaməsi',88,400,CHAMP,SER,style='italic')
    g+=T(M,444,'üçün sayt',88,400,CHAMP,SER,style='italic')
    g+=P(M,520,['Rəşid & Aysu, Bakı. Möhürlə açılan zərf, musiqi,','geri sayım və xəritə — iki dildə.'],26,400,PARCH,SANS,38)
    g+=browser(M,640,760,500,'hero-az.jpg',(140,0,1256,674))
    g+=phone(690,700,250,'env-closed-en.jpg',PH_ENV,rot=0)
    g+=T(M,S_H-M+10,'Sürüşdürün  →',22,500,GOLD,SANS)
    return g

def s2():
    g=R(0,0,S_W,S_H,PARCH)+head(2,False)
    g+=T(M,262,'Tapşırıq',72,400,'#6E4B3A',SER,style='italic')
    g+=P(M,320,['Cütlük kağız dəvətnamə əvəzinə link','istəyirdi: açanda hiss olunsun, tarix və','məkan bir toxunuşla tapılsın, qonaqlar','telefondan rahat baxsın.'],27,400,INK,SANS,40)
    g+=T(M,560,'Nə etdik',72,400,'#6E4B3A',SER,style='italic')
    for i,l in enumerate(['Möhürlə açılan interaktiv zərf','Fon musiqisi və ulduzlu gecə animasiyası','Toya qalan vaxtın canlı geri sayımı','Google Maps və Waze ilə bir toxunuşla yol','İki dil: Azərbaycan və ingilis','Telefon, planşet və kompüter']):
        g+=R(M,604+i*58,22,2,'#B08A7A')+T(M+40,612+i*58,l,26,400,INK,SANS)
    g+=phone(700,250,300,'hero-az.jpg',PH_HERO,rot=0)
    g+=logo_row(False)
    return g

def s3():
    g=R(0,0,S_W,S_H,COCOA)+head(3,True)
    g+=T(M,262,'Möhürə toxun —',72,400,CHAMP,SER,style='italic')
    g+=T(M,342,'zərf açılır.',72,400,GOLD,SER,style='italic')
    g+=P(M,404,['Kağız dəvətnamənin ən yaxşı anı — zərfi açmaqdır.','Saytda da elədir: mum möhür, toxunuş, sonra saray.'],25,400,PARCH,SANS,36)
    g+=phone(M+40,520,300,'env-closed-en.jpg',PH_ENV)
    g+=T(M+190,1200,'Əvvəl',20,500,GOLD,SANS,anchor='middle',ls=3)
    g+=T(540,840,'→',60,400,GOLD,SANS,anchor='middle')
    g+=phone(S_W-M-340,520,300,'hero-az.jpg',PH_HERO)
    g+=T(S_W-M-190,1200,'Sonra',20,500,GOLD,SANS,anchor='middle',ls=3)
    g+=logo_row(True)
    return g

def s4():
    g=R(0,0,S_W,S_H,PARCH)+head(4,False)
    g+=T(M,262,'Dəvətnamə',72,400,'#6E4B3A',SER,style='italic')
    g+=P(M,318,['Antik qravüra üslubu, üzüm salxımları və zeytun —','saray dekorunun özündən gələn motivlər.'],25,400,INK,SANS,36)
    g+=browser(M,400,S_W-2*M,300,'fresco.jpg',(0,0,1536,674))
    g+=browser(M,730,S_W-2*M,500,'names-date.jpg',(263,140,1010,500))
    g+=logo_row(False)
    return g

def s5():
    g=R(0,0,S_W,S_H,NIGHT)+head(5,True)
    g+=T(M,262,'Geri sayım',72,400,CHAMP,SER,style='italic')
    g+=T(M,342,'və yol',72,400,GOLD,SER,style='italic')
    g+=P(M,404,['Toya nə qədər qaldığını sayt özü sayır. Məkan','Google Maps və Waze-də bir toxunuşla açılır.'],25,400,PARCH,SANS,36)
    g+=browser(M,480,S_W-2*M,330,'countdown-title.jpg',(100,260,1336,417))
    g+=browser(M,850,S_W-2*M,340,'venue.jpg',(400,300,736,300))
    g+=logo_row(True)
    return g

def s6():
    g=R(0,0,S_W,S_H,PARCH)+head(6,False)
    g+=browser(M,180,S_W-2*M,420,'monogram.jpg',(0,0,1536,674))
    g+=T(M,720,'Belə dəvətnamə',92,400,'#6E4B3A',SER,style='italic')
    g+=T(M,812,'istəyirsiniz?',92,400,'#6E4B3A',SER,style='italic')
    g+=T(M,868,'Direktə yazın, tarixinizi müzakirə edək.',27,400,INK,SANS)
    chips=[['Möhürlə açılan zərf','Musiqi','Geri sayım'],['Xəritə + Waze','AZ / EN','Telefon üçün']]
    for r,row in enumerate(chips):
        x=M
        for c in row:
            wdt=int(len(c)*14.5)+52
            g+=R(x,920+r*72,wdt,56,'none',28,extra='stroke="#8B6550" stroke-width="1.5"')+T(x+26,956+r*72,c,22,500,INK,SANS)
            x+=wdt+14
    g+=R(M,1090,380,84,'#8B6550',42)+T(M+190,1143,'Direktə yazın  →',28,500,PARCH,SER,anchor='middle')
    g+=logo_row(False)
    return g

for i,b in enumerate([s1(),s2(),s3(),s4(),s5(),s6()],1):
    (OUT/f'wed-{i}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{S_W}" height="{S_H}" viewBox="0 0 {S_W} {S_H}">{DEFS}{b}</svg>',encoding='utf-8')
print('6 svg written')
