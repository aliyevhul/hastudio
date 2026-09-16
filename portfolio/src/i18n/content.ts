/**
 * Every visible string on the site lives here, in Azerbaijani and English.
 * Edit this file to change the site's copy — you should not need to touch
 * the components for a wording or price change.
 *
 * !!! BEFORE YOU GO LIVE, REPLACE EVERYTHING MARKED  TODO  !!!
 */

export const site = {
  brand: 'Huseyn Aliyev',
  // TODO: your real contact details.
  email: 'it@burma.az',
  phone: '+994 00 000 00 00',
  phoneHref: '+99400000000',
  whatsapp: 'https://wa.me/99400000000',
  github: 'https://github.com/',
  linkedin: 'https://www.linkedin.com/in/',
} as const;

export type Lang = 'az' | 'en';

export const content = {
  az: {
    htmlLang: 'az',
    meta: {
      title: 'Sayt və brend dizaynı — kiçik biznes üçün | ' + site.brand,
      description:
        'Kiçik və orta biznes üçün sürətli, mobil uyğun və Google-da tapılan saytlar. Loqo və brend dizaynı da daxil. Sabit qiymət, aydın müddət, işlək nəticə.',
    },
    nav: {
      services: 'Xidmətlər',
      design: 'Dizayn',
      process: 'Necə işləyirik',
      work: 'İşlər',
      faq: 'Suallar',
      contact: 'Əlaqə',
      cta: 'Qiymət al',
      switch: 'EN',
      switchLabel: 'Switch to English',
    },
    hero: {
      eyebrow: 'Bakıda sayt hazırlanması',
      title: 'Biznesinizi axtaranlar sizi tapmalıdır.',
      lede:
        'Kiçik biznes üçün səliqəli, sürətli və mobildə düzgün işləyən sayt qururuq. Şablon yığmırıq — sizin işinizə uyğun qururuq və canlıya çıxarırıq.',
      primary: 'Danışaq',
      secondary: 'Paketlərə bax',
      points: [
        'Adətən 5–10 gün ərzində canlıda',
        'Telefonda mükəmməl görünür',
        'Çoxdilli — AZ, RU, EN və daha çox',
        'Domen, hostinq, quraşdırma — bizim üzərimizdə',
      ],
    },
    problem: {
      title: 'Sizin üçün tanış səslənir?',
      items: [
        {
          title: 'Saytınız yoxdur',
          body:
            'Müştəri sizi Google-da axtarır, tapmır və rəqibə keçir. Instagram səhifəsi saytı əvəz etmir — orada qiymət, ünvan və xidmətləri normal göstərə bilmirsiniz.',
        },
        {
          title: 'Sayt var, amma köhnədir',
          body:
            'Telefonda dağılır, yavaş açılır, nömrə işləmir. Belə sayt müştəri qazandırmır — əksinə, etibarı azaldır.',
        },
        {
          title: 'Kimsə başladı, yarımçıq qoydu',
          body:
            'Ödəniş etdiniz, nəticə yoxdur, əlaqə kəsilib. Biz sabit qiymət və aydın müddətlə işləyirik, hər mərhələni göstəririk.',
        },
      ],
    },
    services: {
      eyebrow: 'Paketlər',
      title: 'Nə qururuq',
      lede:
        'Qiymətlər başlanğıc qiymətidir. Dəqiq rəqəmi 15 dəqiqəlik söhbətdən sonra, yazılı şəkildə veririk — sonradan artan “gizli” məbləğ olmur.',
      packages: [
        {
          name: 'Vizit sayt',
          price: '320 ₼-dən',
          for: 'Salon, kafe, usta, kiçik xidmət',
          items: [
            'Bir səhifə, hər şey bir yerdə',
            'Xidmətlər, qiymət, ünvan, xəritə',
            'WhatsApp və zəng düymələri',
            'Mobil üçün qurulub',
            'İkinci dil — istəyə görə',
            'Domen və hostinq quraşdırması',
          ],
          cta: 'Bunu istəyirəm',
          featured: false,
        },
        {
          name: 'Biznes sayt',
          price: '720 ₼-dən',
          for: 'Klinika, şirkət, mağaza, agentlik',
          items: [
            '4–6 səhifə (Ana, Haqqımızda, Xidmətlər, Əlaqə…)',
            'Müraciət formu — birbaşa e-poçtunuza',
            'Google-da tapılmaq üçün əsas SEO',
            'Çoxdilli qurulum (AZ / RU / EN) — istəyə görə',
            'Google Xəritə və Analytics',
            'Özünüz mətn dəyişə biləsiniz deyə idarə paneli (istəyə görə)',
          ],
          cta: 'Bunu istəyirəm',
          featured: true,
        },
        {
          name: 'Onlayn sifariş',
          price: '1440 ₼-dən',
          for: 'Mağaza, restoran, rezervasiya',
          items: [
            'Məhsul / menyu kataloqu',
            'Səbət və onlayn sifariş',
            'Onlayn ödəniş inteqrasiyası',
            'Çoxdilli kataloq və sifariş axını',
            'Sifarişlərin idarə paneli',
            'İlk ay dəstək daxildir',
          ],
          cta: 'Danışaq',
          featured: false,
        },
      ],
      note:
        'Hər paketə daxildir: mobil uyğunluq, SSL (kilid işarəsi), sürət optimizasiyası və canlıya çıxarma. Çoxdilli sayt istənilən paketə əlavə oluna bilər — BUTA otelinin saytını dörd dildə qurmuşuq.',
    },
    extras: {
      eyebrow: 'Dizayn',
      title: 'Brend dizaynı — sayt ilə eyni üslubda',
      lede:
        'Çox biznesin loqosu yoxdur, ya da hər yerdə fərqli görünür: saytda bir cür, Instagramda başqa cür, vizit kartda üçüncü cür. Bunu da düzəldirik — istər saytla birlikdə, istər ayrıca.',
      items: [
        {
          name: 'Loqo və brend kimliyi',
          price: '200 ₼-dən',
          body: 'Loqo, rəng palitrası və şriftlər. Sayt, vizit kart və sosial şəbəkə — hamısı eyni ailədən görünür.',
        },
        {
          name: 'Sosial şəbəkə şablonları',
          price: '120 ₼-dən',
          body: 'Instagram post və story şablonları. Sizə redaktə oluna bilən fayl veririk — hər paylaşım üçün dizaynerə qayıtmırsınız.',
        },
        {
          name: 'Çap materialları',
          price: '80 ₼-dən',
          body: 'Vizit kart, menyu, flayer, banner, lövhə. Mətbəəyə birbaşa göndərilə bilən, çapa hazır fayllar.',
        },
        {
          name: 'Brend qaydaları',
          price: '160 ₼-dən',
          body: 'Loqonun necə (və necə yox) istifadə olunacağı, rənglər, şriftlər, boşluqlar — bir sənəddə. Komandanız dəyişəndə brend dağılmır.',
        },
      ],
      note: 'Saytla birlikdə sifariş edəndə dizaynı paketə güzəştlə əlavə edirik.',
    },
    process: {
      eyebrow: 'Proses',
      title: 'Necə işləyirik',
      steps: [
        {
          n: '01',
          title: 'Danışırıq — 15 dəqiqə',
          body:
            'Biznesiniz, müştəriniz və saytdan gözləntiniz. Pulsuzdur və heç nəyə öhdəlik yaratmır.',
        },
        {
          n: '02',
          title: 'Yazılı təklif',
          body:
            'Nə daxildir, nə daxil deyil, qiymət və müddət — hamısı yazılı. Razılaşırıqsa, 50% ilkin ödəniş.',
        },
        {
          n: '03',
          title: 'Qururuq və göstəririk',
          body:
            'İş gedişində linki görürsünüz. İki dəfə pulsuz düzəliş — rəyinizi deyirsiniz, tətbiq edirik.',
        },
        {
          n: '04',
          title: 'Canlıya çıxırıq',
          body:
            'Domen, hostinq, Google. Qalan ödəniş. Hər şeyin açarı sizdə qalır — sayt sizindir.',
        },
      ],
    },
    work: {
      eyebrow: 'İşlər',
      title: 'Nə qurmuşuq',
      lede:
        'Hər layihədə problem, gördüyüm iş və nəticə.',
      // TODO: replace these with your real projects. Delete the ones you don't have.
      items: [
        {
          title: 'BUTA Boutique Hotel, Tbilisi',
          tag: 'Otel / rezervasiya',
          body:
            'Tbilisinin tarixi mərkəzində 13 otaqlı butik otel. Otaq kataloqu və qiymətlər, ilkin ödənişsiz rezervasiya formu (administrator təsdiqləyir), restoran menyusu, yol təlimatı və FAQ. Dörd dildə qurulub: ingilis, gürcü, rus və Azərbaycan.',
          result: 'Canlıdır — 4 dil, birbaşa rezervasiya',
          href: 'https://butatbilisi.com/',
        },
        {
          title: 'HR və davamiyyət platforması',
          tag: 'Daxili məhsul',
          body:
            'Çoxfiliallı şirkət üçün işçi, davamiyyət və məzuniyyət sistemi. Geobərkidilmiş qeydiyyat, rol əsaslı icazələr, hesabatlar.',
          result: 'Gündəlik istifadədə, canlı sistem',
          href: '',
        },
        {
          title: 'Layihəniz burada ola bilər',
          tag: 'Boş yer',
          body:
            'İlk müştərilərimiz üçün qiymətdə güzəşt edirik — əvəzində işi portfelimizdə göstərmək icazəsi.',
          result: 'Yer var',
          href: '',
        },
      ],
    },
    faq: {
      eyebrow: 'Suallar',
      title: 'Tez-tez soruşulanlar',
      items: [
        {
          q: 'Nə qədər çəkir?',
          a: 'Vizit sayt adətən 5–7 gün, biznes sayt 10–14 gün. Ən çox gecikdirən şey mətn və şəkillərin gec verilməsidir — onu əvvəldən planlaşdırırıq.',
        },
        {
          q: 'Mətnləri və şəkilləri kim hazırlayır?',
          a: 'Sizdə varsa, istifadə edirik. Yoxdursa, ilkin variantı biz yazırıq, siz təsdiqləyirsiniz. Şəkil üçün keyfiyyətli stok və ya sizin fotolarınız.',
        },
        {
          q: 'Domen və hostinq nə qədərdir?',
          a: 'Domen ildə təxminən 20–40 ₼, hostinq çox vaxt kiçik saytlar üçün pulsuz plana sığır. Bunlar bizim qiymətimizə daxil deyil, amma quraşdırmasını biz edirik və hesablar sizin adınıza olur.',
        },
        {
          q: 'Sonradan özüm dəyişiklik edə bilərəmmi?',
          a: 'Bəli. İstəsəniz, mətn və şəkilləri özünüz dəyişə biləsiniz deyə sadə idarə paneli qururuq və necə istifadə olunduğunu göstəririk.',
        },
        {
          q: 'Təhvildən sonra dəstək varmı?',
          a: 'İlk 30 gün xırda düzəlişlər pulsuzdur. Sonrası üçün aylıq baxım paketi təklif edirik — məcburi deyil.',
        },
        {
          q: 'Ödəniş necə olur?',
          a: 'Başlayanda 50%, canlıya çıxanda 50%. Yazılı təklifdəki qiymət son qiymətdir.',
        },
      ],
    },
    contact: {
      eyebrow: 'Əlaqə',
      title: 'Saytınızdan danışaq',
      lede:
        'Biznesinizi qısa yazın — bir iş günü ərzində cavab veririk. Söhbət pulsuzdur, satış təzyiqi yoxdur.',
      form: {
        name: 'Adınız',
        contact: 'E-poçt və ya nömrə',
        message: 'Biznesiniz və nəyə ehtiyacınız var',
        messagePlaceholder: 'Məsələn: Bakıda diş klinikası, rezervasiya üçün sayt lazımdır…',
        submit: 'Göndər',
        note: 'Göndər düyməsi e-poçt proqramınızı açır.',
      },
      direct: 'Və ya birbaşa:',
    },
    footer: {
      tagline: 'Kiçik biznes üçün sayt hazırlanması.',
      rights: 'Bütün hüquqlar qorunur.',
      built: 'Bu sayt Astro ilə qurulub.',
    },
  },

  en: {
    htmlLang: 'en',
    meta: {
      title: 'Websites & brand design for small business | ' + site.brand,
      description:
        'Fast, mobile-first websites for small and medium businesses, plus logo and brand design. Fixed price, clear timeline, actually shipped.',
    },
    nav: {
      services: 'Services',
      design: 'Design',
      process: 'Process',
      work: 'Work',
      faq: 'FAQ',
      contact: 'Contact',
      cta: 'Get a quote',
      switch: 'AZ',
      switchLabel: 'Azərbaycancaya keç',
    },
    hero: {
      eyebrow: 'Web design & development, Baku',
      title: 'People are looking for your business. Let them find it.',
      lede:
        'We build clean, fast websites for small businesses — built for your business, not dropped from a template, and taken all the way to live.',
      primary: "Let's talk",
      secondary: 'See packages',
      points: [
        'Live in 5–10 days, typically',
        'Looks right on a phone',
        'Multilingual — AZ, RU, EN and more',
        'Domain, hosting, setup — handled',
      ],
    },
    problem: {
      title: 'Sound familiar?',
      items: [
        {
          title: 'You have no website',
          body:
            "Customers search for you, find nothing, and go to a competitor. An Instagram page isn't a website — it can't show your prices, address and services properly.",
        },
        {
          title: 'You have one, but it is old',
          body:
            "It breaks on phones, loads slowly, the phone number doesn't work. A site like that doesn't win customers — it costs you trust.",
        },
        {
          title: 'Someone started it and vanished',
          body:
            'You paid, nothing shipped, they stopped replying. We work to a fixed price and a stated deadline, and you see every stage.',
        },
      ],
    },
    services: {
      eyebrow: 'Packages',
      title: 'What we build',
      lede:
        'Prices are starting points. You get the exact number in writing after a 15-minute call — no figure that quietly grows later.',
      packages: [
        {
          name: 'One-pager',
          price: 'from 320 ₼',
          for: 'Salons, cafés, tradespeople, small services',
          items: [
            'One page, everything in one place',
            'Services, prices, address, map',
            'WhatsApp and call buttons',
            'Built mobile-first',
            'A second language — optional',
            'Domain and hosting set up',
          ],
          cta: 'I want this',
          featured: false,
        },
        {
          name: 'Business site',
          price: 'from 720 ₼',
          for: 'Clinics, companies, shops, agencies',
          items: [
            '4–6 pages (Home, About, Services, Contact…)',
            'Enquiry form straight to your inbox',
            'Core SEO so Google can find you',
            'Multilingual setup (AZ / RU / EN) — optional',
            'Google Maps and Analytics',
            'Optional admin panel so you can edit text yourself',
          ],
          cta: 'I want this',
          featured: true,
        },
        {
          name: 'Online orders',
          price: 'from 1440 ₼',
          for: 'Shops, restaurants, bookings',
          items: [
            'Product or menu catalogue',
            'Cart and online ordering',
            'Payment integration',
            'Multilingual catalogue and checkout',
            'Order dashboard',
            'First month of support included',
          ],
          cta: "Let's talk",
          featured: false,
        },
      ],
      note:
        'Every package includes: mobile layout, SSL (the padlock), speed work, and going live. A multilingual site can be added to any package — we built the BUTA hotel site in four languages.',
    },
    extras: {
      eyebrow: 'Design',
      title: 'Brand design, matching the site',
      lede:
        'Plenty of businesses have no logo, or one that looks different everywhere: one way on the site, another on Instagram, a third on the business card. We fix that too — alongside a site or on its own.',
      items: [
        {
          name: 'Logo and brand identity',
          price: 'from 200 ₼',
          body: 'Logo, colour palette and typefaces. Site, business card and social media all look like they come from the same family.',
        },
        {
          name: 'Social media templates',
          price: 'from 120 ₼',
          body: 'Instagram post and story templates. You get editable files, so you are not going back to a designer for every post.',
        },
        {
          name: 'Print materials',
          price: 'from 80 ₼',
          body: 'Business cards, menus, flyers, banners, signage. Print-ready files you can send straight to the printer.',
        },
        {
          name: 'Brand guidelines',
          price: 'from 160 ₼',
          body: 'How the logo should and should not be used, colours, type, spacing — in one document. The brand survives your team changing.',
        },
      ],
      note: 'Ordered together with a site, design goes onto the package at a discount.',
    },
    process: {
      eyebrow: 'Process',
      title: 'How it works',
      steps: [
        {
          n: '01',
          title: 'We talk — 15 minutes',
          body:
            'Your business, your customers, what the site has to do. Free, and it commits you to nothing.',
        },
        {
          n: '02',
          title: 'Written proposal',
          body:
            "What's included, what isn't, the price and the deadline — in writing. If you agree, 50% up front.",
        },
        {
          n: '03',
          title: 'We build it in the open',
          body:
            'You get a link while it is being built. Two rounds of revisions included — you tell us, we fix it.',
        },
        {
          n: '04',
          title: 'We go live',
          body:
            'Domain, hosting, Google. Final 50%. You keep every login — the site is yours, not rented from us.',
        },
      ],
    },
    work: {
      eyebrow: 'Work',
      title: 'What we have built',
      lede: 'The problem, what we did, and what came of it.',
      // TODO: replace these with your real projects. Delete the ones you don't have.
      items: [
        {
          title: 'BUTA Boutique Hotel, Tbilisi',
          tag: 'Hotel / bookings',
          body:
            'A 13-room boutique hotel in the historical centre of Tbilisi. Room catalogue with prices, a no-prepayment booking form the front desk confirms, restaurant menu, directions and FAQ. Built in four languages: English, Georgian, Russian and Azerbaijani.',
          result: 'Live — 4 languages, direct bookings',
          href: 'https://butatbilisi.com/',
        },
        {
          title: 'HR & attendance platform',
          tag: 'Internal product',
          body:
            'Employee, attendance and leave system for a multi-branch company. Geofenced check-in, role-based permissions, reporting.',
          result: 'Live, in daily use',
          href: '',
        },
        {
          title: 'Your project could go here',
          tag: 'Open slot',
          body:
            'We discount our first few clients in exchange for permission to show the work in this portfolio.',
          result: 'Slot open',
          href: '',
        },
      ],
    },
    faq: {
      eyebrow: 'Questions',
      title: 'Frequently asked',
      items: [
        {
          q: 'How long does it take?',
          a: 'A one-pager is usually 5–7 days, a business site 10–14. The usual delay is waiting on text and photos, so we plan that from the start.',
        },
        {
          q: 'Who writes the text and supplies photos?',
          a: 'If you have them, we use them. If not, we draft the text and you approve it, and we use your photos or good stock images.',
        },
        {
          q: 'What do domain and hosting cost?',
          a: 'A domain is roughly 20–40 ₼ a year; hosting is often free for a small site. These are not in our price, but we set them up and the accounts are in your name.',
        },
        {
          q: 'Can I edit the site myself afterwards?',
          a: 'Yes. If you want it, we add a simple admin panel for text and images, and walk you through using it.',
        },
        {
          q: 'Is there support after handover?',
          a: 'Small fixes are free for the first 30 days. After that we offer a monthly maintenance plan — optional, never required.',
        },
        {
          q: 'How does payment work?',
          a: '50% to start, 50% when it goes live. The price in the written proposal is the final price.',
        },
      ],
    },
    contact: {
      eyebrow: 'Contact',
      title: "Let's talk about your site",
      lede:
        'Tell us briefly about your business — we reply within one working day. The call is free and there is no sales pressure.',
      form: {
        name: 'Your name',
        contact: 'Email or phone',
        message: 'Your business and what you need',
        messagePlaceholder: 'e.g. Dental clinic in Baku, need a site with online booking…',
        submit: 'Send',
        note: 'Send opens your email app.',
      },
      direct: 'Or reach us directly:',
    },
    footer: {
      tagline: 'Websites for small business.',
      rights: 'All rights reserved.',
      built: 'This site is built with Astro.',
    },
  },
} as const;

export const getContent = (lang: Lang) => content[lang];
