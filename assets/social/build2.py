# -*- coding: utf-8 -*-
"""Carousel v2 — every slide gets its own design system.

The argument of the post is "one template does not fit three businesses",
so the slides themselves are designed in three different visual languages.
Only the last slide uses the HA brand palette, to land on the identity.
"""
import pathlib

S, M = 1080, 84

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def T(x, y, s, size=26, w=400, fill='#000', font='Inter', anchor='start', ls=0, op=1):
    return (f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{w}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" opacity="{op}">{esc(s)}</text>')

def P(x, y, lines, size=26, w=400, fill='#000', font='Inter', lh=40, op=1):
    return ''.join(T(x, y + i * lh, l, size, w, fill, font, op=op) for i, l in enumerate(lines) if l)

def rule(x, y, wd, fill, h=1, op=1):
    return f'<rect x="{x}" y="{y}" width="{wd}" height="{h}" fill="{fill}" opacity="{op}"/>'

def footer(n, ground_text, accent, font='Inter', left='hastudio-az.vercel.app'):
    return (T(M, S - M + 8, left, 20, 500, ground_text, font, op=.6)
            + T(S - M, S - M + 8, f'{n}/5', 20, 700, accent, font, anchor='end'))

# ══════════════════════════════════════════════════════════ 1 · COVER ═══════
# Light "type specimen": no colour of its own, it previews the three that follow.
def cover():
    BG, INK, GREY = '#FAFAF8', '#121213', '#6B6B67'
    SG = 'Space Grotesk'
    g = f'<rect width="{S}" height="{S}" fill="{BG}"/>'
    g += rule(M, M + 46, S - 2 * M, INK, 2)
    g += T(M, M + 30, 'UX/UI', 21, 700, INK, SG, ls=6)
    g += T(S - M, M + 30, 'HA STUDIO — 01/05', 21, 500, GREY, SG, anchor='end', ls=2)
    for i, l in enumerate(['Hər biznesin', 'öz dili var.']):
        g += T(M, 300 + i * 96, l, 92, 700, INK, SG)
    g += P(M, 470, ['Kafe, klinika və mağaza — eyni şablon üçünə də yaramır.',
                    'Üç fərqli quruluş, üç fərqli palitra, üç fərqli qərar.'],
           27, 400, GREY, 'IBM Plex Sans', 40)
    # Palette previews: each row is literally the next slide's colours.
    sets = [('KAFE', ['#2B241C', '#E8A33D', '#F6EFE4']),
            ('KLİNİKA', ['#F1F6F7', '#1FA9A0', '#0E4F57']),
            ('MAĞAZA', ['#0E0E12', '#EBFF38', '#FF3D78'])]
    for i, (lab, cols) in enumerate(sets):
        y = 636 + i * 86
        g += rule(M, y - 18, S - 2 * M, INK, 1, .12)
        g += T(M, y + 22, lab, 22, 700, INK, SG, ls=3)
        for j, c in enumerate(cols):
            g += (f'<rect x="{S - M - 210 + j * 70}" y="{y - 8}" width="58" height="44" rx="8" '
                  f'fill="{c}" stroke="{INK}" stroke-opacity=".12"/>')
    g += footer(1, INK, INK, SG)
    return g

# ═══════════════════════════════════════════════════════════ 2 · KAFE ══════
# Warm, printed-menu feel. Serif display, paper card, single amber accent.
def kafe():
    BG, CREAM, ACC, DIM = '#2B241C', '#F6EFE4', '#E8A33D', '#A2937F'
    SER, SANS = 'Noto Serif', 'IBM Plex Sans'
    g = f'<rect width="{S}" height="{S}" fill="{BG}"/>'
    g += f'<circle cx="{S+40}" cy="160" r="260" fill="{ACC}" opacity=".10"/>'
    g += T(M, M + 30, '01 · KAFE', 21, 700, ACC, SANS, ls=5)
    g += T(M, M + 122, 'Menyu birinci,', 60, 700, CREAM, SER)
    g += T(M, M + 196, 'mətn sonra.', 60, 700, ACC, SER)
    # Menu card — a printed card, not a phone.
    cx, cy, cw = M, 344, 396
    g += f'<rect x="{cx}" y="{cy}" width="{cw}" height="470" rx="10" fill="{CREAM}"/>'
    g += T(cx + 32, cy + 64, 'MENYU', 26, 700, BG, SER, ls=6)
    g += rule(cx + 32, cy + 86, cw - 64, BG, 2, .85)
    items = [('Espresso', '3 ₼'), ('Latte', '5 ₼'), ('Çizkeyk', '7 ₼'), ('Səhər yeməyi', '12 ₼')]
    for i, (nm, pr) in enumerate(items):
        y = cy + 136 + i * 52
        g += T(cx + 32, y, nm, 24, 400, '#3A3229', SANS)
        g += T(cx + cw - 32, y, pr, 24, 700, BG, SANS, anchor='end')
        g += rule(cx + 32, y + 16, cw - 64, '#3A3229', 1, .18)
    g += f'<rect x="{cx+32}" y="{cy+362}" width="{cw-64}" height="62" rx="31" fill="{BG}"/>'
    g += T(cx + cw / 2, cy + 402, 'STOL SİFARİŞ ET', 22, 700, ACC, SANS, anchor='middle', ls=1)
    tx = M + 452
    g += P(tx, 396, ['Kafe saytına girən adam üç şeyi',
                     'axtarır: menyu, ünvan, iş saatı.',
                     '',
                     'Ona görə ilk ekranda uzun mətn',
                     'olmur — menyu, zəng və xəritə.'], 26, 400, DIM, SANS, 40)
    g += rule(tx, 640, 5, ACC, 96)
    g += T(tx + 26, 668, 'PRİNSİP', 17, 700, ACC, SANS, ls=3)
    g += P(tx + 26, 706, ['Ən çox istənilən əməliyyat', 'ən böyük düymədir.'], 25, 600, CREAM, SANS, 36)
    g += footer(2, CREAM, ACC, SANS)
    return g

# ════════════════════════════════════════════════════════ 3 · KLİNİKA ══════
# Light, clinical, airy. Institutional sans, soft cards, teal.
def klinika():
    BG, DEEP, ACC, BODY, CARD = '#F1F6F7', '#0E4F57', '#1FA9A0', '#4A6B70', '#FFFFFF'
    SANS = 'IBM Plex Sans'
    g = f'<rect width="{S}" height="{S}" fill="{BG}"/>'
    g += T(M, M + 30, '02 · KLİNİKA', 21, 700, ACC, SANS, ls=5)
    g += T(M, M + 126, 'Burada qərarı', 58, 700, DEEP, SANS)
    g += T(M, M + 196, 'etibar verir.', 58, 700, ACC, SANS)
    cx, cy, cw = M, 348, 404
    g += f'<rect x="{cx}" y="{cy}" width="{cw}" height="188" rx="20" fill="{CARD}"/>'
    g += f'<circle cx="{cx+74}" cy="{cy+92}" r="44" fill="{BG}"/>'
    g += f'<circle cx="{cx+74}" cy="{cy+78}" r="17" fill="#C6D8DA"/>'
    g += f'<path d="M{cx+45} {cy+118} a29 29 0 0 1 58 0z" fill="#C6D8DA"/>'
    g += T(cx + 140, cy + 76, 'Dr. Nərmin Əliyeva', 25, 700, DEEP, SANS)
    g += T(cx + 140, cy + 110, 'Stomatoloq · 15 il', 21, 400, BODY, SANS)
    for i in range(5):
        g += f'<circle cx="{cx+148+i*20}" cy="{cy+140}" r="6" fill="{ACC}"/>'
    g += T(cx + 262, cy + 147, '4.9', 20, 700, DEEP, SANS)
    g += f'<rect x="{cx}" y="{cy+212}" width="{cw}" height="248" rx="20" fill="{CARD}"/>'
    for i, lab in enumerate(['Ad, soyad', 'Telefon']):
        g += (f'<rect x="{cx+24}" y="{cy+240+i*62}" width="{cw-48}" height="50" rx="12" fill="{BG}"/>'
              + T(cx + 44, cy + 272 + i * 62, lab, 20, 400, BODY, SANS))
    g += f'<rect x="{cx+24}" y="{cy+364}" width="{cw-48}" height="58" rx="29" fill="{ACC}"/>'
    g += T(cx + cw / 2, cy + 402, 'QEYDİYYAT', 22, 700, '#FFFFFF', SANS, anchor='middle', ls=1)
    tx = M + 460
    g += P(tx, 400, ['Klinika seçimi emosional deyil,',
                     'ehtiyatlı qərardır. Həkimin şəkli,',
                     'ixtisası və rəylər ön plana çıxır.',
                     '',
                     'Form qısa olur: ad, nömrə, tarix.'], 26, 400, BODY, SANS, 40)
    g += rule(tx, 640, 5, ACC, 96)
    g += T(tx + 26, 668, 'PRİNSİP', 17, 700, ACC, SANS, ls=3)
    g += P(tx + 26, 706, ['Hər əlavə xana', 'müraciəti azaldır.'], 25, 600, DEEP, SANS, 36)
    g += footer(3, DEEP, ACC, SANS)
    return g

# ═════════════════════════════════════════════════════════ 4 · MAĞAZA ══════
# Loud retail: acid yellow, hot pink stickers, dense grid, ticker strip.
def magaza():
    BG, YEL, PINK, PAPER, DIM = '#0E0E12', '#EBFF38', '#FF3D78', '#F2F2F0', '#8A8A93'
    SG, SANS = 'Space Grotesk', 'Manrope'
    g = f'<rect width="{S}" height="{S}" fill="{BG}"/>'
    g += T(M, M + 30, '03 · MAĞAZA', 21, 700, YEL, SG, ls=5)
    g += T(M, M + 128, 'Qiymət', 62, 700, PAPER, SG)
    g += T(M, M + 204, 'gizlənmir.', 62, 700, YEL, SG)
    gx, gy, cwd = M, 352, 196
    for i in range(4):
        x, y = gx + (i % 2) * (cwd + 16), gy + (i // 2) * 216
        g += f'<rect x="{x}" y="{y}" width="{cwd}" height="200" rx="16" fill="#1A1A21"/>'
        g += f'<rect x="{x+18}" y="{y+18}" width="{cwd-36}" height="102" rx="10" fill="#26262F"/>'
        g += rule(x + 18, y + 138, 96, '#3A3A45', 8)
        g += T(x + 18, y + 178, ['18 ₼', '27 ₼', '36 ₼', '45 ₼'][i], 24, 700, YEL, SG)
        if i == 1:      # one sticker only — a badge everywhere is no badge
            g += (f'<g transform="rotate(-9 {x+cwd-44} {y+34})">'
                  f'<rect x="{x+cwd-96}" y="{y+16}" width="80" height="34" rx="17" fill="{PINK}"/>'
                  + T(x + cwd - 56, y + 39, 'YENİ', 17, 700, '#FFFFFF', SG, anchor='middle', ls=1) + '</g>')
    g += f'<rect x="{gx}" y="{gy+446}" width="{cwd*2+16}" height="64" rx="32" fill="{YEL}"/>'
    g += T(gx + cwd + 8, gy + 487, 'SƏBƏT · 2 məhsul · 45 ₼', 22, 700, BG, SG, anchor='middle')
    tx = M + 484
    g += P(tx, 404, ['Mağazada gözü şəkil və qiymət',
                     'aparır. Qiymət məhsulun altında,',
                     'düymədən əvvəl durur.',
                     '',
                     'Səbət həmişə ekranda qalır.'], 26, 400, DIM, SANS, 40)
    g += rule(tx, 644, 5, PINK, 96)
    g += T(tx + 26, 672, 'PRİNSİP', 17, 700, PINK, SG, ls=3)
    g += P(tx + 26, 710, ['Sifariş üç toxunuşdan', 'uzun olmasın.'], 25, 700, PAPER, SANS, 36)
    g += footer(4, PAPER, YEL, SG)
    return g

# ══════════════════════════════════════════════════════════ 5 · BRAND ══════
def brand():
    BG, LIME, PAPER, MUTED, LINE = '#0b0c0e', '#c8f24e', '#edecea', '#9b9da2', '#262a31'
    g = f'<rect width="{S}" height="{S}" fill="{BG}"/>'
    g += f'<circle cx="{S-60}" cy="-40" r="300" fill="{LIME}" opacity="0.07"/>'
    g += ('<g transform="translate(84 104) scale(1.15)" fill="%s">'
          '<rect x="12" y="22" width="11" height="56"/><rect x="41" y="22" width="11" height="56"/>'
          '<polygon points="84,22 93,22 69,78 58,78"/><polygon points="84,22 93,22 118,78 107,78"/>'
          '<polygon points="12,44 102.82,44 107.73,55 12,55"/></g>' % LIME)
    g += T(M, 340, 'Üç biznes,', 74, 800, PAPER)
    g += T(M, 424, 'üç fərqli sayt.', 74, 800, LIME)
    g += P(M, 500, ['Şablon satmırıq. Rəngi, şrifti və quruluşu',
                    'sizin işinizə görə seçirik.'], 27, 400, MUTED, 'Inter', 42)
    # Chips instead of a price tag: what you actually get, not what it costs.
    chips, cx = ['Pulsuz məsləhət', '5–10 günə hazır', 'AZ / RU / EN'], M
    for c in chips:
        wdt = int(len(c) * 13.4) + 48
        g += f'<rect x="{cx}" y="{600}" width="{wdt}" height="56" rx="28" fill="none" stroke="{LINE}" stroke-width="2"/>'
        g += f'<circle cx="{cx+26}" cy="628" r="5" fill="{LIME}"/>'
        g += T(cx + 44, 637, c, 22, 600, PAPER, 'Inter')
        cx += wdt + 14
    for i, (k, v) in enumerate([('Telefon / WhatsApp', '099 600 06 78'),
                                ('E-poçt', 'hastudio.az@gmail.com'),
                                ('Sayt', 'hastudio-az.vercel.app')]):
        y = 726 + i * 72
        g += rule(M, y, S - 2 * M, LINE)
        g += T(M, y + 44, k, 22, 500, MUTED)
        g += T(S - M, y + 44, v, 26, 700, PAPER, anchor='end')
    g += footer(5, PAPER, LIME, left='@hastudio.az')
    return g

out = pathlib.Path('.')
for i, body in enumerate([cover(), kafe(), klinika(), magaza(), brand()], 1):
    (out / f'v2-{i}.svg').write_text(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">{body}</svg>',
        encoding='utf-8')
print('5 slides written')
