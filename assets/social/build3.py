# -*- coding: utf-8 -*-
"""Carousel v3 — agency-grade: full-bleed gradients, a laptop + phone showing a
real-looking website for each business, deep shadows, almost no on-image copy.
The explanation lives in the caption, the way international studios do it."""
import pathlib

S = 1080
def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def T(x, y, s, size, w=400, fill='#000', font='Inter', anchor='start', ls=0, op=1):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" fill="{fill}" '
            f'text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(s)}</text>')
def R(x, y, w, h, fill, rx=0, op=1, extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" opacity="{op}" {extra}/>'

DEFS = '''
<defs>
  <filter id="shadow" x="-30%" y="-30%" width="160%" height="180%">
    <feGaussianBlur stdDeviation="28"/>
  </filter>
  <filter id="soft" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="10"/>
  </filter>
  <filter id="grain">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix type="saturate" values="0"/>
  </filter>
  <linearGradient id="gloss" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity=".18"/>
    <stop offset=".45" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
</defs>'''

def grain(op=.05):
    return f'<rect width="{S}" height="{S}" filter="url(#grain)" opacity="{op}"/>'

# ───────────────────────────── devices ─────────────────────────────────────
def laptop(x, y, w, screen_svg, bezel='#0d0d10'):
    """MacBook-ish. `screen_svg` is drawn in a 1200x750 space, scaled to fit."""
    b = 14
    sw, sh = w - 2 * b, (w - 2 * b) * 750 / 1200
    h = sh + 2 * b
    g = f'<ellipse cx="{x+w/2}" cy="{y+h+40}" rx="{w*.52}" ry="38" fill="#000" opacity=".55" filter="url(#shadow)"/>'
    g += R(x, y, w, h, bezel, 22, extra='stroke="#3a3a42" stroke-width="2"')
    g += f'<circle cx="{x+w/2}" cy="{y+b/2+1}" r="3" fill="#2a2a30"/>'
    g += f'<clipPath id="scr{int(x)}{int(y)}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="8"/></clipPath>'
    g += (f'<g clip-path="url(#scr{int(x)}{int(y)})"><g transform="translate({x+b} {y+b}) scale({sw/1200})">'
          f'{screen_svg}</g></g>')
    g += R(x + b, y + b, sw, sh, 'url(#gloss)', 8)
    # base / hinge
    g += R(x - 26, y + h, w + 52, 20, '#1a1a1f', 6)
    g += R(x - 26, y + h, w + 52, 4, '#3a3a42', 2)
    g += R(x + w/2 - 70, y + h, 140, 8, '#2a2a31', 4)
    return g

def phone(x, y, w, screen_svg, rot=0):
    """Phone with `screen_svg` drawn in a 390x844 space."""
    h, b = w * 844 / 390 + 24, 12
    sw, sh = w - 2 * b, w * 844 / 390
    cx, cy = x + w / 2, y + h / 2
    g = f'<g transform="rotate({rot} {cx} {cy})">'
    g += f'<ellipse cx="{cx}" cy="{y+h+18}" rx="{w*.55}" ry="26" fill="#000" opacity=".5" filter="url(#shadow)"/>'
    g += R(x, y, w, h, '#0d0d10', w * .16, extra='stroke="#3a3a42" stroke-width="2"')
    g += f'<clipPath id="ph{int(x)}{int(y)}"><rect x="{x+b}" y="{y+b}" width="{sw}" height="{sh}" rx="{w*.12}"/></clipPath>'
    g += (f'<g clip-path="url(#ph{int(x)}{int(y)})"><g transform="translate({x+b} {y+b}) scale({sw/390})">'
          f'{screen_svg}</g></g>')
    g += R(cx - w * .18, y + b + 10, w * .36, 22, '#0d0d10', 11)      # dynamic island
    g += R(x + b, y + b, sw, sh, 'url(#gloss)', w * .12)
    return g + '</g>'

# ───────────────────────────── website screens (1200 x 750) ────────────────
def nav(bg, fg, logo, items, cta, cta_bg, cta_fg, font='Inter', serif_logo=None):
    g = R(0, 0, 1200, 750, bg)
    g += T(60, 58, logo, 30, 800, fg, serif_logo or font)
    for i, it in enumerate(items):
        g += T(430 + i * 130, 56, it, 19, 500, fg, font, op=.75)
    g += R(1000, 30, 140, 46, cta_bg, 23)
    g += T(1070, 60, cta, 17, 700, cta_fg, font, anchor='middle')
    return g

def site_kafe():
    BG, INK, AMB, CREAM = '#FBF5EC', '#2B241C', '#E8A33D', '#F6EFE4'
    g = nav(BG, INK, 'Dəm.', ['Menyu', 'Haqqımızda', 'Ünvan', 'Rezerv'], 'Stol sifarişi', INK, AMB,
            'IBM Plex Sans', 'Noto Serif')
    g += T(60, 220, 'Səhər burada', 74, 700, INK, 'Noto Serif')
    g += T(60, 300, 'başlayır.', 74, 700, AMB, 'Noto Serif')
    g += T(60, 356, 'Təzə dəmlənmiş qəhvə, ev peçenyesi və pəncərə önündə', 20, 400, INK, 'IBM Plex Sans', op=.7)
    g += T(60, 386, 'sakit bir səhər. Hər gün 08:00–22:00.', 20, 400, INK, 'IBM Plex Sans', op=.7)
    g += R(60, 424, 170, 56, INK, 28) + T(145, 460, 'Menyu', 20, 700, CREAM, 'IBM Plex Sans', anchor='middle')
    g += R(246, 424, 200, 56, 'none', 28, extra=f'stroke="{INK}" stroke-width="2"')
    g += T(346, 460, 'Zəng et', 20, 600, INK, 'IBM Plex Sans', anchor='middle')
    # hero image
    g += '<defs><radialGradient id="cup" cx=".4" cy=".35"><stop offset="0" stop-color="#F3C976"/><stop offset="1" stop-color="#8A4B1E"/></radialGradient></defs>'
    g += R(660, 120, 480, 380, 'url(#cup)', 28)
    g += '<ellipse cx="900" cy="418" rx="150" ry="22" fill="#3A2416" opacity=".55"/>'
    g += '<path d="M810 250 h180 l-18 150 h-144z" fill="#F6EFE4"/>'                 # cup body
    g += '<path d="M990 268 q62 8 52 62 q-8 40 -62 40" fill="none" stroke="#F6EFE4" stroke-width="18" stroke-linecap="round"/>'
    g += '<ellipse cx="900" cy="250" rx="90" ry="20" fill="#5A2E14"/>'
    g += '<ellipse cx="900" cy="250" rx="72" ry="14" fill="#8A4B1E"/>'
    for dx in (-34, 0, 34):
        g += (f'<path d="M{900+dx} 216 c-14 -22 14 -34 0 -56 c-12 -18 10 -30 4 -48" fill="none" '
              f'stroke="#F6EFE4" stroke-width="6" stroke-linecap="round" opacity=".55"/>')
    # menu cards
    for i, (nm, pr) in enumerate([('Espresso', '3 ₼'), ('Flat white', '5 ₼'), ('Çizkeyk', '7 ₼'), ('Səhər seti', '12 ₼')]):
        x = 60 + i * 275
        g += R(x, 560, 250, 150, '#FFFFFF', 18)
        g += R(x + 20, 580, 210, 60, ['#E8A33D', '#C97A2B', '#F0D3A4', '#8A4B1E'][i], 12)
        g += T(x + 20, 676, nm, 19, 600, INK, 'IBM Plex Sans')
        g += T(x + 230, 676, pr, 19, 700, AMB, 'IBM Plex Sans', anchor='end')
    return g

def site_klinika():
    BG, DEEP, TEAL, MINT = '#FFFFFF', '#0E4F57', '#1FA9A0', '#EAF6F5'
    g = nav(BG, DEEP, 'Dent+', ['Xidmətlər', 'Həkimlər', 'Qiymətlər', 'Əlaqə'], 'Qeydiyyat', TEAL, '#fff', 'IBM Plex Sans')
    g += R(60, 130, 200, 36, MINT, 18) + T(160, 155, 'Bakı · Nərimanov', 15, 600, TEAL, 'IBM Plex Sans', anchor='middle')
    g += T(60, 250, 'Gülüşünüzə', 72, 700, DEEP, 'IBM Plex Sans')
    g += T(60, 330, 'peşəkar qayğı.', 72, 700, TEAL, 'IBM Plex Sans')
    g += T(60, 386, 'Ağrısız müalicə, şəffaf qiymət və 15 illik təcrübə.', 20, 400, DEEP, 'IBM Plex Sans', op=.7)
    for i, v in enumerate(['4.9 ★  Google', '2 400+ pasiyent', 'Rəsmi lisenziya']):
        g += R(60 + i * 200, 420, 186, 44, MINT, 22)
        g += T(153 + i * 200, 449, v, 15, 600, DEEP, 'IBM Plex Sans', anchor='middle')
    # booking card
    g += R(700, 110, 440, 400, '#F4FAF9', 28)
    g += T(740, 168, 'Növbə götür', 26, 700, DEEP, 'IBM Plex Sans')
    for i, lab in enumerate(['Ad, soyad', 'Telefon', 'Tarix və saat']):
        g += R(740, 196 + i * 70, 360, 54, '#FFFFFF', 14, extra=f'stroke="#D6E7E5" stroke-width="2"')
        g += T(760, 230 + i * 70, lab, 17, 400, DEEP, 'IBM Plex Sans', op=.55)
    g += R(740, 416, 360, 58, TEAL, 29) + T(920, 453, 'Təsdiqlə', 19, 700, '#fff', 'IBM Plex Sans', anchor='middle')
    # doctors row
    for i, (nm, sp) in enumerate([('Dr. N. Əliyeva', 'Ortodont'), ('Dr. R. Həsənov', 'İmplantoloq'), ('Dr. S. Məmmədli', 'Terapevt')]):
        x = 60 + i * 210
        g += R(x, 540, 190, 170, MINT, 20)
        g += f'<circle cx="{x+95}" cy="{590}" r="30" fill="#C6DEDB"/>'
        g += T(x + 95, 650, nm, 16, 700, DEEP, 'IBM Plex Sans', anchor='middle')
        g += T(x + 95, 676, sp, 14, 400, DEEP, 'IBM Plex Sans', anchor='middle', op=.6)
    return g

def site_magaza():
    BG, INK, YEL, PINK = '#F4F4F6', '#0E0E12', '#F5E11F', '#FF3D78'
    g = nav(BG, INK, 'NÖQTƏ', ['Yeni', 'Kişi', 'Qadın', 'Endirim'], 'Səbət · 2', INK, YEL, 'Space Grotesk')
    g += R(60, 110, 1080, 300, INK, 28)
    g += T(100, 200, 'YENİ', 84, 700, YEL, 'Space Grotesk')
    g += T(100, 290, 'KOLLEKSİYA', 84, 700, '#F4F4F6', 'Space Grotesk')
    g += T(100, 350, 'Payız 26 · Pulsuz çatdırılma', 20, 500, '#F4F4F6', 'Manrope', op=.7)
    g += R(760, 150, 340, 220, '#26262F', 20)
    g += f'<circle cx="930" cy="260" r="80" fill="{PINK}"/><circle cx="1000" cy="200" r="46" fill="{YEL}"/>'
    cols = ['#6C63FF', '#FF9F43', '#1FA9A0', '#FF3D78']
    for i in range(4):
        x = 60 + i * 275
        g += R(x, 440, 250, 280, '#FFFFFF', 20)
        g += R(x + 18, 458, 214, 160, cols[i], 14)
        if i == 1:
            g += R(x + 150, 470, 70, 30, PINK, 15) + T(x + 185, 491, 'YENİ', 14, 700, '#fff', 'Space Grotesk', anchor='middle')
        g += T(x + 18, 660, ['Oversize sviter', 'Kətan köynək', 'Yun palto', 'Klassik jins'][i], 18, 600, INK, 'Manrope')
        g += R(x + 18, 678, 74, 30, YEL, 8) + T(x + 55, 699, ['49 ₼', '35 ₼', '129 ₼', '59 ₼'][i], 16, 800, INK, 'Space Grotesk', anchor='middle')
    return g

def site_ha():
    BG, LIME, PAPER, MUTED = '#0b0c0e', '#c8f24e', '#edecea', '#9b9da2'
    g = nav(BG, PAPER, 'Huseyn Aliyev.', ['Xidmətlər', 'Dizayn', 'İşlər', 'Suallar'], 'Qiymət al', LIME, BG)
    g += T(60, 250, 'Biznesinizi axtaranlar', 66, 800, PAPER)
    g += T(60, 326, 'sizi tapmalıdır.', 66, 800, LIME)
    g += T(60, 384, 'Kiçik biznes üçün səliqəli, sürətli və mobildə düzgün işləyən sayt.', 20, 400, MUTED)
    g += R(60, 424, 160, 56, LIME, 28) + T(140, 460, 'Danışaq', 20, 700, BG, anchor='middle')
    for i, (t1, t2) in enumerate([('Vizit sayt', 'Salon, kafe, usta'), ('Biznes sayt', 'Klinika, şirkət'), ('Onlayn sifariş', 'Mağaza, restoran')]):
        x = 60 + i * 370
        g += R(x, 540, 340, 170, '#131519', 20, extra='stroke="#262a31" stroke-width="2"')
        g += T(x + 28, 596, t1, 24, 800, PAPER) + T(x + 28, 630, t2, 16, 400, MUTED)
        g += R(x + 28, 656, 120, 32, LIME if i == 1 else '#262a31', 16)
    return g

# phone screens (390 x 844)
def mob(bg, fg, acc, title1, title2, btn, font='Inter', tfont=None, img=None):
    g = R(0, 0, 390, 844, bg)
    g += T(30, 90, '≡', 30, 700, fg, font) + R(300, 66, 60, 30, acc, 15)
    g += R(30, 130, 330, 260, img or acc, 24)
    g += T(30, 470, title1, 40, 800, fg, tfont or font)
    g += T(30, 520, title2, 40, 800, acc, tfont or font)
    g += R(30, 580, 330, 60, fg, 30) + T(195, 619, btn, 20, 700, bg, font, anchor='middle')
    g += R(30, 660, 330, 60, 'none', 30, extra=f'stroke="{fg}" stroke-opacity=".3" stroke-width="2"')
    g += T(195, 699, 'WhatsApp', 20, 600, fg, font, anchor='middle')
    return g

# ───────────────────────────── slides ──────────────────────────────────────
def chrome(n, label, thesis, fg, acc, font='Inter', handle='@hastudio.az'):
    g = T(80, 112, label, 22, 700, acc, font, ls=6)
    g += T(S - 80, 112, f'{handle}   ·   {n} / 5', 22, 600, fg, font, anchor='end', op=.7)
    g += T(80, S - 88, thesis, 42, 700, fg, font)
    return g

def bg_gradient(id_, stops, kind='linear', attrs='x1="0" y1="0" x2="1" y2="1"'):
    tag = 'linearGradient' if kind == 'linear' else 'radialGradient'
    inner = ''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o, c in stops)
    return f'<defs><{tag} id="{id_}" {attrs}>{inner}</{tag}></defs>' + R(0, 0, S, S, f'url(#{id_})')

def slide_kafe():
    g = bg_gradient('bg2', [(0, '#3B2A1B'), (.55, '#1E140C'), (1, '#120B06')], 'radial', 'cx=".2" cy=".15" r="1.1"')
    g += f'<circle cx="920" cy="140" r="260" fill="#E8A33D" opacity=".16" filter="url(#shadow)"/>'
    g += grain(.06)
    g += laptop(120, 226, 840, site_kafe())
    g += phone(770, 560, 190, mob('#FBF5EC', '#2B241C', '#E8A33D', 'Səhər', 'burada.', 'Menyu', 'IBM Plex Sans', 'Noto Serif'), rot=-7)
    g += chrome(2, '01 — KAFE', 'Menyu birinci, mətn sonra.', '#F6EFE4', '#E8A33D', 'IBM Plex Sans')
    return g

def slide_klinika():
    g = bg_gradient('bg3', [(0, '#F3FAF9'), (.6, '#D7ECE9'), (1, '#BFDFDB')])
    g += f'<circle cx="160" cy="900" r="300" fill="#1FA9A0" opacity=".18" filter="url(#shadow)"/>'
    g += f'<circle cx="980" cy="120" r="220" fill="#fff" opacity=".6" filter="url(#shadow)"/>'
    g += grain(.04)
    g += laptop(120, 226, 840, site_klinika(), bezel='#12181a')
    g += phone(770, 560, 190, mob('#FFFFFF', '#0E4F57', '#1FA9A0', 'Növbə', 'götür.', 'Qeydiyyat', 'IBM Plex Sans'), rot=-7)
    g += chrome(3, '02 — KLİNİKA', 'Burada qərarı etibar verir.', '#0E4F57', '#1FA9A0', 'IBM Plex Sans')
    return g

def slide_magaza():
    g = bg_gradient('bg4', [(0, '#FFE94A'), (.5, '#F5D60F'), (1, '#E8B800')], 'linear', 'x1="0" y1="0" x2="1" y2="1"')
    g += f'<circle cx="940" cy="980" r="260" fill="#FF3D78" opacity=".55" filter="url(#shadow)"/>'
    g += grain(.05)
    g += laptop(120, 226, 840, site_magaza())
    g += phone(770, 560, 190, mob('#0E0E12', '#F4F4F6', '#F5E11F', 'Yeni', 'kolleksiya', 'Səbətə at', 'Space Grotesk', img='#26262F'), rot=-7)
    g += chrome(4, '03 — MAĞAZA', 'Qiymət gizlənmir, səbət itmir.', '#0E0E12', '#0E0E12', 'Space Grotesk')
    return g

def slide_cover():
    g = bg_gradient('bg1', [(0, '#15171c'), (1, '#0b0c0e')], 'radial', 'cx=".5" cy=".1" r="1"')
    g += f'<circle cx="540" cy="120" r="360" fill="#c8f24e" opacity=".12" filter="url(#shadow)"/>'
    g += grain(.06)
    g += T(80, 112, 'UX / UI  ·  HA STUDIO', 22, 700, '#c8f24e', 'Inter', ls=6)
    g += T(80, 250, 'Hər biznesin', 88, 800, '#edecea', 'Inter')
    g += T(80, 346, 'öz dili var.', 88, 800, '#c8f24e', 'Inter')
    # three fanned browser windows, each in its own palette
    def win(x, y, w, rot, body, bar):
        h = w * .62
        cx, cy = x + w/2, y + h/2
        s = f'<g transform="rotate({rot} {cx} {cy})">'
        s += f'<ellipse cx="{cx}" cy="{y+h+20}" rx="{w*.5}" ry="26" fill="#000" opacity=".55" filter="url(#shadow)"/>'
        s += R(x, y, w, h, bar, 18)
        for i, c in enumerate(['#FF5F57', '#FEBC2E', '#28C840']):
            s += f'<circle cx="{x+22+i*20}" cy="{y+20}" r="6" fill="{c}"/>'
        s += f'<clipPath id="w{int(x)}"><rect x="{x}" y="{y+40}" width="{w}" height="{h-40}" rx="0"/></clipPath>'
        s += f'<g clip-path="url(#w{int(x)})"><g transform="translate({x} {y+40}) scale({w/1200})">{body}</g></g>'
        return s + '</g>'
    g += win(90, 470, 520, -6, site_klinika(), '#E4EFEE')
    g += win(470, 500, 520, 5, site_magaza(), '#E9E9EC')
    g += win(270, 600, 540, -1, site_kafe(), '#EFE6D8')
    g += T(S - 80, 112, '@hastudio.az   ·   1 / 5', 22, 600, '#edecea', 'Inter', anchor='end', op=.7)
    return g

def slide_cta():
    g = bg_gradient('bg5', [(0, '#15171c'), (1, '#0b0c0e')], 'radial', 'cx=".8" cy=".9" r="1"')
    g += f'<circle cx="900" cy="980" r="320" fill="#c8f24e" opacity=".14" filter="url(#shadow)"/>'
    g += grain(.06)
    g += ('<g transform="translate(80 80) scale(.9)" fill="#c8f24e">'
          '<rect x="12" y="22" width="11" height="56"/><rect x="41" y="22" width="11" height="56"/>'
          '<polygon points="84,22 93,22 69,78 58,78"/><polygon points="84,22 93,22 118,78 107,78"/>'
          '<polygon points="12,44 102.82,44 107.73,55 12,55"/></g>')
    g += T(80, 250, 'Sizin saytınız', 78, 800, '#edecea', 'Inter')
    g += T(80, 336, 'növbəti ola bilər.', 78, 800, '#c8f24e', 'Inter')
    g += laptop(230, 410, 700, site_ha(), bezel='#16171c')
    g += T(80, S - 118, 'hastudio-az.vercel.app', 26, 700, '#edecea', 'Inter')
    g += T(80, S - 80, '099 600 06 78  ·  hastudio.az@gmail.com', 22, 500, '#9b9da2', 'Inter')
    g += T(S - 80, 112, '@hastudio.az   ·   5 / 5', 22, 600, '#edecea', 'Inter', anchor='end', op=.7)
    return g

out = pathlib.Path('.')
for i, body in enumerate([slide_cover(), slide_kafe(), slide_klinika(), slide_magaza(), slide_cta()], 1):
    (out / f'v3-{i}.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">{DEFS}{body}</svg>',
        encoding='utf-8')
print('v3 written')
