# -*- coding: utf-8 -*-
"""Post 2 — «Ocaq» restaurant website concept, 7 slides.

Pattern study (Dribbble, ~25 dark restaurant sites): fine-dining sites pair a
charcoal-brown ground with copper/gold, serif display type, tracked uppercase
eyebrows, thin gold rules, and present the work as section crops + a laptop +
fanned phones. Photos carry those shots; here drawn plates and ember light do
that job, with vignette and grain for depth."""
import pathlib, math

S = 1080
INK, INK2, BROWN, WOOD = '#15100C', '#1F160F', '#3A2A1D', '#5A3E2A'
COPPER, GOLD, CREAM, MUTED, MUTED2 = '#C4823A', '#E0B36B', '#F1E6D3', '#A08A70', '#6E5B48'
SERIF, SERIF2, COND, SANS = 'Playfair Display', 'Cormorant Garamond', 'Barlow Condensed', 'IBM Plex Sans'

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def T(x, y, s, size, w=400, fill=CREAM, font=SANS, anchor='start', ls=0, op=1, style='normal'):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" font-style="{style}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(s)}</text>')
def R(x, y, w, h, fill, rx=0, op=1, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{op}" {extra}/>'
def rule(x, y, w, fill=GOLD, op=.5, h=1): return R(x, y, w, h, fill, 0, op)

DEFS = f'''<defs>
  <filter id="sh" x="-30%" y="-30%" width="160%" height="180%"><feGaussianBlur stdDeviation="26"/></filter>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="40"/></filter>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/></filter>
  <radialGradient id="vig" cx=".5" cy=".5" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/>
    <stop offset="1" stop-color="#000" stop-opacity=".65"/></radialGradient>
  <radialGradient id="ember" cx=".5" cy=".55" r=".6"><stop offset="0" stop-color="#F0A24A"/>
    <stop offset=".35" stop-color="#B8511C"/><stop offset="1" stop-color="{INK}" stop-opacity="0"/></radialGradient>
  <linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".14"/>
    <stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2A1D14"/><stop offset="1" stop-color="#150E09"/></linearGradient>
</defs>'''

def ground():
    return R(0, 0, S, S, 'url(#wood)') + R(0, 0, S, S, 'url(#vig)') + R(0, 0, S, S, '#000', 0, .0)
def grain(op=.07): return f'<rect width="{S}" height="{S}" filter="url(#grain)" opacity="{op}"/>'
def glow(cx, cy, r, c=COPPER, op=.22): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" opacity="{op}" filter="url(#glow)"/>'

# ── illustrated food: dark stoneware plate, top-down ─────────────────────────
def plate(cx, cy, r, main='#B5561F', deep='#6E2A10', garnish='#7F9B4A', sauce=COPPER, seed=0):
    g = f'<ellipse cx="{cx}" cy="{cy+r*.12}" rx="{r*1.05}" ry="{r*.35}" fill="#000" opacity=".45" filter="url(#sh)"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#2B211A"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#4A3A2E" stroke-width="{r*.05}"/>'
    g += f'<circle cx="{cx}" cy="{cy}" r="{r*.8}" fill="#1B140F"/>'
    g += f'<path d="M{cx-r*.55} {cy+r*.25} q{r*.5} {-r*.6} {r*1.1} {-r*.1}" fill="none" stroke="{sauce}" stroke-width="{r*.06}" stroke-linecap="round" opacity=".8"/>'
    g += f'<ellipse cx="{cx-r*.05}" cy="{cy-r*.02}" rx="{r*.42}" ry="{r*.34}" fill="{deep}"/>'
    g += f'<ellipse cx="{cx-r*.1}" cy="{cy-r*.08}" rx="{r*.34}" ry="{r*.26}" fill="{main}"/>'
    g += f'<ellipse cx="{cx-r*.16}" cy="{cy-r*.14}" rx="{r*.16}" ry="{r*.1}" fill="#F0B063" opacity=".55"/>'
    for i in range(6):
        a = seed + i * 1.05
        g += f'<circle cx="{cx+math.cos(a)*r*.38}" cy="{cy+math.sin(a)*r*.3}" r="{r*.045}" fill="{garnish}"/>'
    g += f'<circle cx="{cx+r*.3}" cy="{cy+r*.22}" r="{r*.07}" fill="#D93B2B" opacity=".9"/>'
    return g

# ── devices ─────────────────────────────────────────────────────────────────
def laptop(x, y, w, screen, bezel='#0e0b09'):
    b = 14; sw = w - 2*b; sh = sw * 750/1200; h = sh + 2*b
    cid = f'l{int(x)}{int(y)}'
    g = f'<ellipse cx="{x+w/2}" cy="{y+h+42}" rx="{w*.52}" ry="40" fill="#000" opacity=".7" filter="url(#sh)"/>'
    g += R(x, y, w, h, bezel, 22, extra='stroke="#3a2f27" stroke-width="2"')
    g += f'<clipPath id="{cid}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="8"/></clipPath>'
    g += f'<g clip-path="url(#{cid})"><g transform="translate({x+b} {y+b}) scale({sw/1200})">{screen}</g></g>'
    g += R(x+b, y+b, sw, sh, 'url(#gloss)', 8)
    g += R(x-26, y+h, w+52, 20, '#1a1410', 6) + R(x-26, y+h, w+52, 4, '#3a2f27', 2)
    return g

def phone(x, y, w, screen, rot=0):
    h = w*844/390 + 24; b = 12; sw = w-2*b; sh = w*844/390; cx, cy = x+w/2, y+h/2
    cid = f'p{int(x)}{int(y)}'
    g = f'<g transform="rotate({rot} {cx} {cy})">'
    g += f'<ellipse cx="{cx}" cy="{y+h+18}" rx="{w*.55}" ry="26" fill="#000" opacity=".6" filter="url(#sh)"/>'
    g += R(x, y, w, h, '#0e0b09', w*.16, extra='stroke="#3a2f27" stroke-width="2"')
    g += f'<clipPath id="{cid}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="{w*.12}"/></clipPath>'
    g += f'<g clip-path="url(#{cid})"><g transform="translate({x+b} {y+b}) scale({sw/390})">{screen}</g></g>'
    g += R(cx-w*.18, y+b+10, w*.36, 22, '#0e0b09', 11) + R(x+b, y+b, sw, sh, 'url(#gloss)', w*.12)
    return g + '</g>'

# ── the website, 1200 x 750 screens ─────────────────────────────────────────
def nav(items_light=True):
    g = R(0, 0, 1200, 750, INK)
    g += T(60, 58, 'Ocaq', 34, 700, CREAM, SERIF)
    for i, it in enumerate(['Menyu', 'Hekayə', 'Tədbirlər', 'Əlaqə']):
        g += T(470 + i*120, 55, it.upper(), 15, 600, CREAM, COND, ls=2, op=.8)
    g += R(1000, 28, 140, 46, 'none', 0, extra=f'stroke="{GOLD}" stroke-width="1.5"')
    g += T(1070, 58, 'STOL SİFARİŞİ', 14, 600, GOLD, COND, anchor='middle', ls=2)
    return g

def scr_hero():
    g = nav()
    g += f'<ellipse cx="880" cy="420" rx="520" ry="360" fill="url(#ember)" opacity=".85"/>'
    g += plate(880, 400, 170, seed=.4)
    g += T(60, 190, 'ATƏŞ ÜSTÜNDƏ · 2009-DAN', 15, 600, GOLD, COND, ls=4)
    g += T(60, 300, 'Od üstündə', 86, 400, CREAM, SERIF)
    g += T(60, 390, 'bişən hekayələr.', 86, 400, CREAM, SERIF, style='italic')
    g += T(60, 450, 'Sac, təndir və manqal. Bakının köhnə küçəsində, yeni dadlarla.', 20, 400, MUTED, SANS)
    g += R(60, 500, 210, 58, COPPER, 0) + T(165, 537, 'STOL SİFARİŞİ', 15, 700, INK, COND, anchor='middle', ls=2)
    g += T(310, 537, 'Menyuya bax  →', 17, 500, CREAM, SANS, op=.85)
    g += rule(60, 640, 1080, GOLD, .35)
    for i, (k, v) in enumerate([('İŞ SAATI', '12:00 – 00:00'), ('ÜNVAN', 'İçərişəhər, Kiçik Qala 14'), ('REZERV', '+994 12 000 00 00')]):
        g += T(60 + i*380, 680, k, 12, 600, GOLD, COND, ls=3) + T(60 + i*380, 712, v, 18, 400, CREAM, SANS, op=.9)
    return g

def scr_menu():
    g = nav()
    g += T(600, 150, 'MENYU', 14, 600, GOLD, COND, anchor='middle', ls=5)
    g += T(600, 215, 'İmza yeməkləri', 58, 400, CREAM, SERIF, anchor='middle')
    g += rule(540, 240, 120, GOLD, .6)
    dishes = [('Sac içi', 'quzu, kartof, göyərti', '24', '#B5561F', '#6E2A10'),
              ('Lavəngi', 'toyuq, qoz, alça', '22', '#C98A3E', '#7A4A1A'),
              ('Düşbərə', 'əl xəmiri, nanə', '14', '#D9C7A6', '#8A7250'),
              ('Şah plov', 'qazmaq, zəfəran', '28', '#E0A24A', '#8A5A16')]
    for i, (nm, d, pr, m, dp) in enumerate(dishes):
        x = 60 + i*275
        g += R(x, 290, 250, 400, INK2, 6, extra=f'stroke="#2E2219" stroke-width="1"')
        g += plate(x+125, 400, 78, m, dp, seed=i*.9)
        g += T(x+125, 540, nm, 26, 400, CREAM, SERIF, anchor='middle')
        g += T(x+125, 570, d, 14, 400, MUTED, SANS, anchor='middle')
        g += rule(x+95, 598, 60, GOLD, .5)
        g += T(x+125, 640, f'{pr} ₼', 20, 600, GOLD, COND, anchor='middle', ls=1)
    return g

def scr_story():
    g = nav()
    g += R(60, 130, 520, 560, '#0F0A07', 4)
    # clay wall texture: soft horizontal bands
    for i in range(6):
        g += R(60, 150 + i*90, 520, 44, '#1A120C', 0, .55)
    # tandoor mouth - an arch cut into the wall, glowing inside
    g += '<path d="M150 690 V420 a170 170 0 0 1 340 0 V690 Z" fill="#050302"/>'
    g += '<path d="M150 690 V420 a170 170 0 0 1 340 0 V690 Z" fill="url(#ember)" opacity=".95"/>'
    g += '<path d="M150 690 V420 a170 170 0 0 1 340 0 V690 Z" fill="none" stroke="#5A3E2A" stroke-width="10"/>'
    g += '<ellipse cx="320" cy="660" rx="150" ry="26" fill="#F0A24A" opacity=".55"/>'
    for i, (px, py, r) in enumerate([(300, 500, 5), (345, 450, 3.5), (270, 430, 4), (330, 380, 2.5), (290, 340, 2), (360, 320, 1.8)]):
        g += f'<circle cx="{px}" cy="{py}" r="{r}" fill="#F5B75A" opacity="{.95 - i*.13}"/>'
    g += R(60, 130, 520, 560, 'none', 4, extra=f'stroke="{GOLD}" stroke-opacity=".35" stroke-width="1"')
    g += T(660, 190, 'HEKAYƏMİZ', 14, 600, GOLD, COND, ls=5)
    g += T(660, 280, 'Ocaq sözü', 62, 400, CREAM, SERIF)
    g += T(660, 350, 'evin ürəyidir.', 62, 400, CREAM, SERIF, style='italic')
    for i, l in enumerate(['2009-cu ildə İçərişəhərdə bir təndir və altı stolla',
                           'başladıq. Bu gün üç baş aşpaz, eyni təndir və',
                           'hər gün təzə yoğrulan xəmir.']):
        g += T(660, 410 + i*30, l, 18, 400, MUTED, SANS)
    for i, (n, k) in enumerate([('16', 'il'), ('3', 'baş aşpaz'), ('48', 'yer')]):
        g += T(660 + i*160, 590, n, 54, 400, GOLD, SERIF) + T(660 + i*160, 620, k.upper(), 12, 600, MUTED, COND, ls=3)
    return g

def scr_reserve():
    g = nav()
    g += glow(600, 380, 300, COPPER, .18)
    g += T(600, 200, 'REZERVASİYA', 14, 600, GOLD, COND, anchor='middle', ls=5)
    g += T(600, 300, 'Stolunuz sizi', 74, 400, CREAM, SERIF, anchor='middle')
    g += T(600, 380, 'gözləyir.', 74, 400, GOLD, SERIF, anchor='middle', style='italic')
    for i, (lab, val) in enumerate([('TARİX', '18 sentyabr'), ('SAAT', '20:00'), ('QONAQ', '2 nəfər')]):
        x = 210 + i*270
        g += R(x, 450, 240, 70, 'none', 0, extra=f'stroke="{GOLD}" stroke-opacity=".5" stroke-width="1"')
        g += T(x+20, 478, lab, 11, 600, GOLD, COND, ls=3) + T(x+20, 506, val, 19, 400, CREAM, SANS)
    g += R(210, 550, 780, 62, COPPER, 0) + T(600, 590, 'STOLU TƏSDİQLƏ', 16, 700, INK, COND, anchor='middle', ls=3)
    g += T(600, 660, 'Təsdiq 5 dəqiqə ərzində WhatsApp-a gəlir · ilkin ödəniş yoxdur', 15, 400, MUTED, SANS, anchor='middle')
    return g

def mob_hero():
    g = R(0, 0, 390, 844, INK)
    g += f'<ellipse cx="200" cy="330" rx="230" ry="200" fill="url(#ember)" opacity=".9"/>'
    g += plate(195, 300, 105, seed=.4)
    g += T(30, 66, 'Ocaq', 26, 700, CREAM, SERIF) + T(360, 62, '≡', 26, 400, CREAM, SANS, anchor='end')
    g += T(30, 500, 'ATƏŞ ÜSTÜNDƏ', 12, 600, GOLD, COND, ls=4)
    g += T(30, 560, 'Od üstündə', 48, 400, CREAM, SERIF) + T(30, 612, 'bişən', 48, 400, CREAM, SERIF, style='italic')
    g += T(30, 664, 'hekayələr.', 48, 400, CREAM, SERIF, style='italic')
    g += R(30, 720, 330, 60, COPPER, 0) + T(195, 758, 'STOL SİFARİŞİ', 15, 700, INK, COND, anchor='middle', ls=3)
    return g

def mob_menu():
    g = R(0, 0, 390, 844, INK)
    g += T(30, 66, 'Ocaq', 26, 700, CREAM, SERIF) + T(360, 62, '≡', 26, 400, CREAM, SANS, anchor='end')
    g += T(30, 140, 'MENYU', 12, 600, GOLD, COND, ls=4) + T(30, 190, 'İmza yeməkləri', 36, 400, CREAM, SERIF)
    for i, (nm, d, pr, m, dp) in enumerate([('Sac içi', 'quzu, kartof', '24', '#B5561F', '#6E2A10'),
                                              ('Lavəngi', 'toyuq, qoz', '22', '#C98A3E', '#7A4A1A'),
                                              ('Şah plov', 'qazmaq, zəfəran', '28', '#E0A24A', '#8A5A16')]):
        y = 230 + i*180
        g += R(30, y, 330, 160, INK2, 6)
        g += plate(105, y+80, 52, m, dp, seed=i)
        g += T(180, y+66, nm, 22, 400, CREAM, SERIF) + T(180, y+92, d, 13, 400, MUTED, SANS)
        g += T(180, y+128, f'{pr} ₼', 16, 600, GOLD, COND, ls=1)
    return g

# ── slides ───────────────────────────────────────────────────────────────────
def chrome(n, label, thesis=None, font=COND):
    g = T(80, 108, label, 16, 600, GOLD, COND, ls=5)
    g += T(S-80, 108, f'@hastudio.az   ·   {n} / 7', 16, 500, CREAM, COND, anchor='end', ls=2, op=.6)
    if thesis: g += T(80, S-84, thesis, 34, 400, CREAM, SERIF, style='italic')
    return g

def s1_cover():
    g = ground() + glow(540, 300, 340, COPPER, .16) + grain()
    g += T(80, 108, 'KEYS  ·  RESTORAN SAYTI', 16, 600, GOLD, COND, ls=5)
    g += T(S-80, 108, '@hastudio.az   ·   1 / 7', 16, 500, CREAM, COND, anchor='end', ls=2, op=.6)
    g += T(540, 300, 'Ocaq', 150, 400, CREAM, SERIF, anchor='middle')
    g += rule(440, 330, 200, GOLD, .7)
    g += T(540, 372, 'RESTORAN ÜÇÜN SAYT KONSEPTİ', 15, 600, GOLD, COND, anchor='middle', ls=5)
    g += laptop(150, 440, 780, scr_hero())
    return g

def s2_hero():
    # section crop: the screen fills the slide, no device
    g = R(0, 0, S, S, INK)
    g += f'<g transform="translate(-60 120) scale(1)">' + f'<g transform="scale({1200/1200})">' + '</g></g>'
    g += f'<g transform="translate(0 165) scale(0.9)">{scr_hero()}</g>'
    g += R(0, 0, S, S, 'url(#vig)') + grain(.06)
    g += chrome(2, 'HERO  ·  İLK EKRAN', 'Bir cümlə, bir düymə, bir boşqab.')
    return g

def s3_menu():
    g = ground() + grain()
    g += laptop(80, 250, 920, scr_menu())
    g += chrome(3, 'MENYU', 'Yemək əvvəl gözlə yeyilir.')
    return g

def s4_story():
    g = R(0, 0, S, S, INK) + f'<g transform="translate(-30 165) scale(0.9)">{scr_story()}</g>'
    g += R(0, 0, S, S, 'url(#vig)') + grain(.06)
    g += chrome(4, 'HEKAYƏ', 'Rəqəmlər də hekayə danışır.')
    return g

def s5_reserve():
    g = ground() + glow(540, 560, 320, COPPER, .14) + grain()
    g += laptop(80, 250, 920, scr_reserve())
    g += chrome(5, 'REZERVASİYA', 'Üç xana. Bir düymə. Stol sizindir.')
    return g

def s6_mobile():
    g = ground() + glow(700, 500, 300, COPPER, .16) + grain()
    g += phone(190, 250, 300, mob_hero(), rot=-8)
    g += phone(560, 300, 300, mob_menu(), rot=6)
    g += chrome(6, 'MOBİL', 'Qonaqların 80%-i telefondan girir.')
    return g

def s7_cta():
    g = ground() + glow(540, 420, 320, COPPER, .12) + grain()
    g += ('<g transform="translate(482 200) scale(.95)" fill="%s">'
          '<rect x="12" y="22" width="11" height="56"/><rect x="41" y="22" width="11" height="56"/>'
          '<polygon points="84,22 93,22 69,78 58,78"/><polygon points="84,22 93,22 118,78 107,78"/>'
          '<polygon points="12,44 102.82,44 107.73,55 12,55"/></g>' % CREAM)
    g += T(540, 420, 'Restoranınız üçün', 62, 400, CREAM, SERIF, anchor='middle')
    g += T(540, 492, 'belə bir sayt?', 62, 400, GOLD, SERIF, anchor='middle', style='italic')
    g += rule(440, 540, 200, GOLD, .7)
    g += T(540, 600, 'Menyu, rezervasiya, üç dil — bir həftədə canlıda.', 20, 400, MUTED, SANS, anchor='middle')
    g += T(540, 720, '099 600 06 78', 40, 400, CREAM, SERIF, anchor='middle')
    g += T(540, 762, 'hastudio-az.vercel.app  ·  hastudio.az@gmail.com', 16, 500, MUTED, COND, anchor='middle', ls=2)
    g += T(S-80, 108, '@hastudio.az   ·   7 / 7', 16, 500, CREAM, COND, anchor='end', ls=2, op=.6)
    g += T(80, 108, 'HA STUDIO', 16, 600, GOLD, COND, ls=5)
    return g

out = pathlib.Path('.')
slides = [s1_cover(), s2_hero(), s3_menu(), s4_story(), s5_reserve(), s6_mobile(), s7_cta()]
for i, body in enumerate(slides, 1):
    (out / f'ocaq-{i}.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">{DEFS}{body}</svg>', encoding='utf-8')
print('7 slides written')
