# -*- coding: utf-8 -*-
"""Generates the 5-slide Instagram carousel. Run: python3 build.py"""
import pathlib, subprocess, json

S = 1080                      # square canvas
M = 84                        # outer margin
INK, SURF, SURF2 = '#0b0c0e', '#131519', '#1a1d22'
LINE, PAPER, MUTED, ACC = '#262a31', '#edecea', '#9b9da2', '#c8f24e'
F = 'Inter'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def text(x, y, s, size=26, w=400, fill=PAPER, anchor='start', ls=0):
    return (f'<text x="{x}" y="{y}" font-family="{F}" font-size="{size}" font-weight="{w}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}">{esc(s)}</text>')

def block(x, y, lines, size=26, w=400, fill=MUTED, lh=42):
    """A paragraph with hand-broken lines — no measuring, no surprises."""
    return ''.join(text(x, y + i * lh, l, size, w, fill) for i, l in enumerate(lines) if l)

def frame(n, left='hastudio-az.vercel.app'):
    """Shared chrome: ground, corner glow, slide number, handle."""
    return (
        f'<rect width="{S}" height="{S}" fill="{INK}"/>'
        f'<circle cx="{S-60}" cy="-40" r="300" fill="{ACC}" opacity="0.07"/>'
        + text(M, S - M + 8, left, 20, 500, MUTED)
        + text(S - M, S - M + 8, f'{n}/5', 20, 700, ACC, anchor='end'))

def principle(x, y, lines):
    """Accent-ruled callout: the rule is the emphasis, not a box."""
    h = 34 + len(lines) * 36
    return (f'<rect x="{x}" y="{y}" width="6" height="{h}" fill="{ACC}" rx="3"/>'
            + text(x + 26, y + 24, 'PRİNSİP', 17, 700, ACC, ls=3)
            + block(x + 26, y + 62, lines, 25, 600, PAPER, 36))

# ---------------------------------------------------------------- mockups ---
def phone(x, y, inner, w=300, h=560):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="34" fill="{SURF}" stroke="{LINE}" stroke-width="2"/>'
            f'<rect x="{x+w/2-34}" y="{y+16}" width="68" height="7" rx="3.5" fill="{LINE}"/>' + inner)

def kafe_mockup(x, y):
    p = x + 20, y + 44
    px, py = p
    g = (f'<rect x="{px}" y="{py}" width="260" height="150" rx="14" fill="{SURF2}"/>'
         f'<circle cx="{px+130}" cy="{py+70}" r="34" fill="none" stroke="{ACC}" stroke-width="3" opacity="0.65"/>'
         f'<rect x="{px+112}" y="{py+62}" width="36" height="22" rx="5" fill="{ACC}" opacity="0.65"/>')
    g += f'<rect x="{px}" y="{py+172}" width="260" height="58" rx="29" fill="{ACC}"/>'
    g += text(px + 130, py + 209, 'MENYU', 24, 800, INK, anchor='middle', ls=1)
    for i, lab in enumerate(['Zəng', 'Xəritə']):
        bx = px + i * 136
        g += (f'<rect x="{bx}" y="{py+248}" width="124" height="50" rx="25" fill="none" stroke="{LINE}" stroke-width="2"/>'
              + text(bx + 62, py + 279, lab, 20, 600, PAPER, anchor='middle'))
    for i, wdt in enumerate([230, 190, 250, 150]):
        g += f'<rect x="{px}" y="{py+322+i*26}" width="{wdt}" height="10" rx="5" fill="{LINE}"/>'
    return phone(x, y, g)

def klinika_mockup(x, y):
    px, py = x + 20, y + 44
    g = (f'<rect x="{px}" y="{py}" width="260" height="118" rx="14" fill="{SURF2}"/>'
         f'<circle cx="{px+52}" cy="{py+59}" r="34" fill="{LINE}"/>'
         f'<circle cx="{px+52}" cy="{py+50}" r="13" fill="{SURF}"/>'
         f'<path d="M{px+30} {py+84} a22 22 0 0 1 44 0z" fill="{SURF}"/>')
    for i, wdt in enumerate([120, 90]):
        g += f'<rect x="{px+102}" y="{py+40+i*24}" width="{wdt}" height="11" rx="5.5" fill="{LINE}"/>'
    for i in range(5):                                    # rating stars
        g += f'<circle cx="{px+108+i*17}" cy="{py+92}" r="5" fill="{ACC}"/>'
    for i, lab in enumerate(['15 il təcrübə', 'Rəylər 4.9']):
        bx = px + i * 134
        g += (f'<rect x="{bx}" y="{py+136}" width="126" height="38" rx="19" fill="none" stroke="{LINE}" stroke-width="2"/>'
              + text(bx + 63, py + 161, lab, 16, 600, MUTED, anchor='middle'))
    for i, lab in enumerate(['Ad, soyad', 'Telefon', 'Tarix']):
        g += (f'<rect x="{px}" y="{py+194+i*56}" width="260" height="46" rx="12" fill="none" stroke="{LINE}" stroke-width="2"/>'
              + text(px + 16, py + 224 + i * 56, lab, 18, 400, MUTED))
    g += f'<rect x="{px}" y="{py+366}" width="260" height="56" rx="28" fill="{ACC}"/>'
    g += text(px + 130, py + 402, 'QEYDİYYAT', 22, 800, INK, anchor='middle', ls=1)
    return phone(x, y, g)

def magaza_mockup(x, y):
    px, py = x + 20, y + 44
    g = ''
    for i in range(4):
        cx, cy = px + (i % 2) * 136, py + (i // 2) * 186
        g += (f'<rect x="{cx}" y="{cy}" width="124" height="168" rx="14" fill="{SURF2}"/>'
              f'<rect x="{cx+14}" y="{cy+14}" width="96" height="86" rx="10" fill="{LINE}"/>'
              f'<rect x="{cx+14}" y="{cy+112}" width="72" height="9" rx="4.5" fill="{LINE}"/>'
              + text(cx + 14, cy + 150, f'{(i+2)*9} ₼', 21, 800, ACC))
    g += f'<rect x="{px}" y="{py+400}" width="260" height="60" rx="30" fill="{ACC}"/>'
    g += text(px + 130, py + 438, 'SƏBƏT · 2 məhsul', 21, 800, INK, anchor='middle')
    return phone(x, y, g)

def thumb(x, y, kind):
    """Tiny wireframes for the cover — three visibly different layouts."""
    g = f'<rect x="{x}" y="{y}" width="248" height="168" rx="16" fill="{SURF}" stroke="{LINE}" stroke-width="2"/>'
    if kind == 'kafe':
        g += (f'<rect x="{x+18}" y="{y+18}" width="212" height="66" rx="8" fill="{SURF2}"/>'
              f'<rect x="{x+18}" y="{y+96}" width="212" height="30" rx="15" fill="{ACC}"/>'
              f'<rect x="{x+18}" y="{y+136}" width="96" height="8" rx="4" fill="{LINE}"/>')
    elif kind == 'klinika':
        g += (f'<circle cx="{x+46}" cy="{y+48}" r="22" fill="{LINE}"/>'
              f'<rect x="{x+80}" y="{y+36}" width="100" height="9" rx="4.5" fill="{LINE}"/>'
              f'<rect x="{x+80}" y="{y+56}" width="70" height="9" rx="4.5" fill="{LINE}"/>'
              f'<rect x="{x+18}" y="{y+88}" width="212" height="26" rx="8" fill="none" stroke="{LINE}" stroke-width="2"/>'
              f'<rect x="{x+18}" y="{y+124}" width="212" height="26" rx="13" fill="{ACC}"/>')
    else:
        for i in range(4):
            cx, cy = x + 18 + (i % 2) * 110, y + 18 + (i // 2) * 62
            g += f'<rect x="{cx}" y="{cy}" width="102" height="54" rx="8" fill="{SURF2}"/>'
        g += f'<rect x="{x+18}" y="{y+142}" width="212" height="12" rx="6" fill="{ACC}"/>'
    return g

# ----------------------------------------------------------------- slides ---
def slide1():
    g = frame(1)
    g += text(M, M + 30, 'UX/UI  ·  SAYT DİZAYNI', 21, 700, ACC, ls=4)
    for i, l in enumerate(['Eyni şablon', 'üç fərqli biznesə']):
        g += text(M, 250 + i * 88, l, 78, 800, PAPER)
    g += text(M, 426, 'yaramır.', 78, 800, ACC)
    g += block(M, 500, ['Kafe, klinika və mağaza — hər biri başqa qərar',
                        'tələb edir. Üç real nümunə, üç fərqli quruluş.'], 27, 400, MUTED, 40)
    for i, k in enumerate(['kafe', 'klinika', 'magaza']):
        g += thumb(M + i * 276, 636, k)
    for i, lab in enumerate(['KAFE', 'KLİNİKA', 'MAĞAZA']):
        g += text(M + i * 276, 842, lab, 19, 700, MUTED, ls=2)
    g += text(S - M, 330, '→', 96, 800, ACC, anchor='end')
    return g

def case(n, eyebrow, title_a, title_b, mockup, body, rule):
    g = frame(n)
    g += text(M, M + 30, eyebrow, 21, 700, ACC, ls=4)
    g += text(M, M + 108, title_a, 56, 800, PAPER)
    g += text(M, M + 176, title_b, 56, 800, ACC)
    g += mockup(M, 330)
    tx = M + 372
    g += block(tx, 372, body, 26, 400, MUTED, 40)
    g += principle(tx, 372 + len(body) * 40 + 44, rule)
    return g

def slide2():
    return case(2, '01 · KAFE', 'Menyu birinci,', 'mətn sonra.', kafe_mockup,
                ['Kafe saytına girən adam üç şeyi',
                 'axtarır: menyu, ünvan, iş saatı.',
                 '',
                 'Ona görə ilk ekranda uzun mətn',
                 'olmur — böyük «Menyu» düyməsi,',
                 'zəng və xəritə düymələri olur.'],
                ['Ən çox istənilən əməliyyat', 'ən böyük düymədir.'])

def slide3():
    return case(3, '02 · KLİNİKA', 'Burada qərarı', 'etibar verir.', klinika_mockup,
                ['Klinika seçimi emosional deyil,',
                 'ehtiyatlı qərardır. Həkimin şəkli,',
                 'ixtisası və rəylər ön plana çıxır.',
                 '',
                 'Rezervasiya formu qısa olur:',
                 'ad, nömrə, tarix — vəssalam.'],
                ['Hər əlavə xana', 'müraciəti azaldır.'])

def slide4():
    return case(4, '03 · MAĞAZA', 'Qiymət', 'gizlənmir.', magaza_mockup,
                ['Mağazada gözü şəkil və qiymət',
                 'aparır. Qiymət məhsulun altında,',
                 'düymədən əvvəl durur.',
                 '',
                 'Səbət həmişə ekranda qalır —',
                 'müştəri yolunu itirməməlidir.'],
                ['Sifariş üç toxunuşdan', 'uzun olmasın.'])

def slide5():
    g = frame(5, left='@hastudio.az')
    mark = ('<g transform="translate(84 104) scale(1.15)" fill="%s">'
            '<rect x="12" y="22" width="11" height="56"/><rect x="41" y="22" width="11" height="56"/>'
            '<polygon points="84,22 93,22 69,78 58,78"/><polygon points="84,22 93,22 118,78 107,78"/>'
            '<polygon points="12,44 102.82,44 107.73,55 12,55"/></g>' % ACC)
    g += mark
    g += text(M, 340, 'Sizin biznesiniz', 74, 800, PAPER)
    g += text(M, 424, 'hansıdır?', 74, 800, ACC)
    g += block(M, 500, ['Saytınızı işinizə uyğun qururuq — hazır şablon yox.',
                        'Loqo və brend dizaynı da bizdədir.'], 27, 400, MUTED, 42)
    g += f'<rect x="{M}" y="600" width="446" height="62" rx="31" fill="{ACC}"/>'
    g += text(M + 223, 640, '300 ₼-dən  ·  5–10 günə hazır', 25, 800, INK, anchor='middle')
    rows = [('Telefon / WhatsApp', '099 600 06 78'),
            ('E-poçt', 'hastudio.az@gmail.com'),
            ('Sayt', 'hastudio-az.vercel.app')]
    for i, (k, v) in enumerate(rows):
        y = 730 + i * 74
        g += f'<rect x="{M}" y="{y}" width="{S-2*M}" height="1" fill="{LINE}"/>'
        g += text(M, y + 44, k, 22, 500, MUTED)
        g += text(S - M, y + 44, v, 26, 700, PAPER, anchor='end')
    return g

# ------------------------------------------------------------------ build ---
out = pathlib.Path('.')
slides = [slide1(), slide2(), slide3(), slide4(), slide5()]
for i, body in enumerate(slides, 1):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" '
           f'viewBox="0 0 {S} {S}">{body}</svg>')
    (out / f'slide-{i}.svg').write_text(svg, encoding='utf-8')
print('svg written:', len(slides))
