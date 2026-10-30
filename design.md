# YUCG Design System

Design reference derived from the Yale Undergraduate Consulting Group website (yaleconsulting.org). Values below were measured from the live site's computed styles (Oct 2026). The site is built on Wix, so some values are Wix defaults rather than deliberate brand choices. Those are flagged.

**How to use this file:** sections 1–10 are the rules. Section 11 is a component library: every component has a name (`yucg-…`), when to use it, its markup and its CSS. To build a page, ask for components by name, for example *"Build a page from `yucg-header`, `yucg-hero`, `yucg-split`, `yucg-logo-wall` and `yucg-footer`."*

---

## 1. Brand Personality

- **Institutional, confident, understated.** Yale navy + white, a Yale-specific serif, square-cornered controls, lots of white space.
- **Prestige through proof, not decoration.** The page leans on client, sponsor and alumni-placement logo walls and press mentions rather than illustrations or icons.
- **People-forward.** Large, full-bleed photos of members carry the warmth; the UI itself stays restrained.

Tone of copy: polished and aspirational but plain, e.g. "high-impact, cross-industry business challenges," "the next generation of talent at Yale."

## 2. Color

| Token | Hex | RGB | Usage |
|---|---|---|---|
| `--yucg-navy` | `#1C366A` | 28, 54, 106 | Primary brand color. Headings, nav links, solid section bands, image overlays |
| `--yucg-navy-alt` | `#203869` | 32, 56, 105 | Near-identical navy used on one band; treat as an alias of `--yucg-navy` |
| `--yucg-navy-overlay` | `rgba(28,54,106,.72)` | — | Tint over hero photography so white text stays legible |
| `--yucg-white` | `#FFFFFF` | 255, 255, 255 | Page background, text on navy, ghost-button outlines |
| `--yucg-ink` | `#2F2E2E` | 47, 46, 46 | Body / lead paragraph text (softer than pure black) |
| `--yucg-gray` | `#A0A09F` | 160, 160, 159 | Neutral blocks and dividers (secondary; use sparingly) |
| `--yucg-link` | `#116DFF` | 17, 109, 255 | Wix default link blue. Not brand; avoid in new work |

**Rules**
- The palette is essentially two-color: navy and white. Introduce no accent hues.
- Navy text on white for headings; white text on navy for bands and hero.
- Body copy uses `--yucg-ink`, never navy, to keep headings distinct.

## 3. Typography

| Role | Family on site | Notes |
|---|---|---|
| Display / headings | YaleNew Bold | Yale's proprietary serif (Matthew Carter). Licensed for Yale affiliates through Yale's identity resources |
| Body / UI | YaleNew Roman | Used for paragraphs, nav and buttons alike |

Fallback stack: `"YaleNew", "Mallory", Georgia, "Times New Roman", serif`. Web-safe alternatives with a similar feel: **Libre Caslon Text** or **Source Serif 4** (Google Fonts). The site also loads Avenir and DIN Next (Wix theme defaults), but they don't appear in visible content. Don't use them.

### Type scale (desktop)

| Style | Font | Size / line-height | Tracking | Color | Align | Example |
|---|---|---|---|---|---|---|
| Hero title | YaleNew Bold | 56 / 56px (1.0) | 0.02em | White | Left | "Yale Undergraduate Consulting Group" |
| Feature heading | YaleNew Bold | 50 / 70px (1.4) | normal | Navy | Left | "Explore YUCG", "Who Are We?" |
| Section title | YaleNew Bold | 46 / 64.4px (1.4) | normal | Navy | Center | "Our Recent Clients", "After YUCG" |
| Band title | YaleNew Bold | 38 / 53.2px (1.4) | normal | White | Left | "Featured In" |
| Lead paragraph | YaleNew Roman | 22 / 30.8px (1.4) | normal | Ink | Left | "YUCG is a student-led…" |
| Nav link | YaleNew Roman 700 | 16px | normal | Navy | Right | "Services", "About Us" |
| Button label | YaleNew Roman 400 | 16px | normal | White | Center | "About Us", "Join Us" |

**Rules**
- Line-height is a consistent 1.4× across headings and body (hero title is the exception at 1.0 for a tight, stacked lockup).
- No uppercase transforms anywhere. Sentence/title case only.
- Headings are often broken across two lines for rhythm ("Who / Are We?", "Yale Undergraduate / Consulting Group").

## 4. Layout

- Full-width horizontal bands, stacked vertically, alternating white and photo/navy backgrounds.
- Hero and feature sections are tall (~690–900px desktop) with a two-column split: heading block on one side, copy or photo on the other.
- Logo-wall sections are centered: centered title, then a grid of logos below.
- Generous vertical padding between sections; content never feels dense.

**Page structure (home)**
1. Header: logo left (~106×86px), nav right: Services · About Us · Join Us · Contact · Blog · FAQ · More
2. Hero: full-bleed member photo with navy overlay (72%), white title, two ghost buttons (About Us, Join Us)
3. Who Are We?: split heading + lead paragraph mission statement
4. Explore YUCG: photo + culture paragraph (retreats, project dinners, formals, NYC trips) + Join Us CTA
5. Our Recent Clients: large logo grid (Fortune 500s, startups, nonprofits, IMF, etc.)
6. Our Sponsors: single row of sponsor logos on white
7. After YUCG: alumni-placement logo grid (McKinsey, Citadel, Morgan Stanley, Meta, Google…)
8. Featured In: navy band with press thumbnails (Business Insider, The Economist, Yale Daily News)
9. Footer: logo, "New Haven, CT", email, Instagram / Facebook / LinkedIn icons

## 5. Components (as measured on the site)

- **Ghost button**: transparent, 1px white border, 0 radius, white 16px label, 12px × 32px padding (~146 × 41px). Hover fills white with navy text. On white backgrounds, invert: navy border + navy text, filling navy on hover.
- **Navigation**: text-only links, YaleNew Roman Bold 16px, navy, right-aligned. No underlines, no pill highlights. Overflow items collapse into "More."
- **Logo walls**: native-color logos on white, uniform max-height (~100–160px), centered in a grid. No borders, cards or shadows.
- **Press thumbnails**: small square thumbnails (~129px) on the navy band, each linking to the article.
- **Social icons**: 24px monochrome icons in the footer.

Section 11 turns each of these into a ready-to-use component, and adds the UI pieces the site doesn't have yet (forms, data, charts).

## 6. Imagery

- Real member photography: candid group and event shots in natural, warm light. No stock photos, no illustrations.
- Hero photos are full-bleed and tinted with `rgba(28, 54, 106, 0.72)` navy.
- Logos are the only other visual content.

## 7. Shape, Depth & Spacing

- **Corners:** 0px radius everywhere: buttons, images, sections.
- **Shadows:** none.
- **Borders:** the 1px outline on ghost buttons. (Section 11 also allows 1px gray hairline dividers and input underlines; see 11.0.)
- **Spacing:** large section padding (roughly 80–120px vertical on desktop); content blocks cap well short of full width.

## 8. CSS Tokens

```css
:root {
  /* Color */
  --yucg-navy: #1C366A;
  --yucg-navy-overlay: rgba(28, 54, 106, 0.72);
  --yucg-white: #FFFFFF;
  --yucg-ink: #2F2E2E;
  --yucg-gray: #A0A09F;

  /* Type */
  --yucg-font-display: "YaleNew", "Libre Caslon Text", Georgia, serif; /* Bold weight */
  --yucg-font-body: "YaleNew", "Libre Caslon Text", Georgia, serif;    /* Roman weight */
  --yucg-lh: 1.4;
  --yucg-size-hero: 56px;
  --yucg-size-h2: 50px;
  --yucg-size-section: 46px;
  --yucg-size-band: 38px;
  --yucg-size-lead: 22px;
  --yucg-size-ui: 16px;

  /* Shape */
  --yucg-radius: 0;
  --yucg-border: 1px solid currentColor;
}
```

## 9. Do / Don't

**Do**
- Keep it navy + white with a single serif family.
- Use square corners and outline buttons.
- Let photography and logo walls carry the visual weight.
- Center section titles above logo grids; left-align heading/copy splits.

**Don't**
- Add accent colors, gradients or drop shadows.
- Round corners or use pill buttons.
- Use the Wix default link blue (`#116DFF`) or the unused Avenir/DIN fonts.
- Set headings in all caps or a sans-serif.

## 10. Applying to Charts & Slides

Charts and slides follow the **YUCG Data Visualization studio** house style, not the website's serif. Every graph component in section 11.6 is built to these rules.

- **Font:** Lato for every word in a chart or on a slide (`"Lato", "Helvetica Neue", Arial, sans-serif`). YaleNew stays on web pages and documents.
- **Text color:** all chart text is `#00346B`: title, subtitle, legend, axis labels, axis titles, data labels and the source line. No gray text.
- **Background:** white on screen, transparent when exported, so the chart sits on any slide or page. No logo on charts.
- **Title** centered above the chart in Lato Bold, stating the takeaway ("Visits doubled after the October launch"). The subtitle names the measure, unit and base.
- **Legend** centered under the title. Line charts use short line samples, solid or dotted like the series; bar charts use square swatches.
- **Vertical axis title** rotated and centered on the axis, with the unit ("Visits (thousands)").
- **Gridlines** horizontal only, thin (0.8px) and dashed, in `rgba(0, 52, 107, .6)`. Line charts have no axis line; bar charts keep a thin baseline.
- **Lines** 2.8px with no point markers. A fitted, forecast, projected or estimated series is **dotted, in the same color as its actual series**.
- **Series colors**, in order, never cycled (a ninth series folds into "Other"):

  | Token | Hex | | Token | Hex |
  |---|---|---|---|---|
  | `chart-1` navy | `#1C366A` | | `chart-5` steel | `#909AB1` |
  | `chart-2` mid blue | `#3465A8` | | `chart-6` pale blue | `#C4D4E8` |
  | `chart-3` sky | `#7AA7D6` | | `chart-7` deep navy | `#0B1F3A` |
  | `chart-4` slate | `#445469` | | `chart-8` mist blue | `#DFE6EF` |

- **Highlight style** when one series carries the message: focus `#1C366A` for it, context `#C9CED6` for the rest.
- **Heat maps and maps:** sequential `#F1F5FA` → `#C4D4E8` → `#7AA7D6` → `#1164A3` → `#1C366A` (low to high). Never a rainbow.
- **Sentiment:** positive = `chart-1` navy, neutral = context gray, negative = `chart-3` sky. Always show the sign or a word as well; never rely on color alone.
- **Data labels** off by default; label only the value the reader needs.
- **One value axis per chart.** Two measures on different scales become two charts.
- **Source line** bottom left in every data chart: "Source: …; YUCG analysis". Illustrative figures say "Example data".
- **Type sizes** (px at 960 × 540): title 24, subtitle 14.7, legend 13.5, data label 12.5, axis 12, source 11.7.
- **Slides:** 16:9, all text Lato in `#00346B` (white on navy title and section slides), title top left, source bottom left, logo bottom right.

---

## 11. Component Library

Every component below works on its own once **11.0 Foundation** is on the page (graph components also need `yucg-chart-tokens`). Class names are prefixed `yucg-`. Modifiers use `--` (e.g. `yucg-btn--light`). Copy the CSS of the components you use, or paste the whole section into one stylesheet.

### Index

| Group | Component | Call it for |
|---|---|---|
| Foundation | `yucg-foundation` | Tokens, reset, font loading. Always include |
| | `yucg-container` | Centered max-width content with side gutters |
| | `yucg-band` | Any full-width section (white, navy or photo) |
| Page frame | `yucg-header` | Logo left, nav right |
| | `yucg-nav` | Text-only nav links with a "More" overflow |
| | `yucg-footer` | Logo, location, email, social icons |
| Sections | `yucg-hero` | Full-bleed photo + 72% navy overlay + title + ghost buttons |
| | `yucg-page-hero` | Compact navy band that opens an inner page or tool |
| | `yucg-split` | Two-line feature heading left, lead copy right ("Who Are We?") |
| | `yucg-feature` | Photo + copy + CTA ("Explore YUCG") |
| | `yucg-section-title` | Centered 46px title above a grid |
| | `yucg-navy-band` | Navy band with band title + copy ("Featured In") |
| | `yucg-columns` | 2–4 text columns separated by hairlines (services, tools) |
| Proof | `yucg-logo-wall` | Client / alumni-placement logo grid |
| | `yucg-logo-row` | Single row of sponsor logos |
| | `yucg-press` | Square press thumbnails on navy |
| | `yucg-social` | 24px monochrome social icons |
| | `yucg-stat-row` | Large proof numbers (projects, clients, members) |
| | `yucg-quote` | Client or member testimonial |
| Actions | `yucg-btn` | Ghost button: navy (default) or `--light` on navy/photos |
| | `yucg-btn-group` | Row of buttons |
| | `yucg-segmented` | Two to four mutually exclusive options |
| | `yucg-link` | Inline text link |
| Forms | `yucg-field` | Label + underlined input / select / textarea + hint |
| | `yucg-range` | Slider with live value |
| | `yucg-check` | Checkbox or radio row |
| | `yucg-dropzone` | File upload area |
| | `yucg-note` | Instructions / callout block |
| | `yucg-form-group` | Titled group of fields ("Settings") |
| Data | `yucg-chart-tokens` | Lato, chart text color, studio palette. Include with any chart |
| | `yucg-kpis` | Row of headline numbers for dashboards |
| | `yucg-chart-block` | Studio chart layout: centered title, legend, chart, source |
| | `yucg-legend` | Centered legend: square swatches or line samples |
| | `yucg-bars` | Horizontal bar chart with baseline (HTML) |
| | `yucg-diverging` | Diverging bars for scores from −1 to +1 |
| | `yucg-mix` | 100% stacked bar (e.g. positive / neutral / negative) |
| | `yucg-line-chart` | SVG line chart, dotted fitted/forecast series |
| | `yucg-table` | Data table with navy header rule |
| | `yucg-chip` | Tags / keywords |
| Disclosure | `yucg-accordion` | Expandable rows (FAQ, per-location detail) |
| | `yucg-tabs` | Switch between views on one page |
| | `yucg-gate` | Small centered form (password, sign-up) |

---

### 11.0 Foundation — `yucg-foundation`, `yucg-container`, `yucg-band`

Always include. Loads the fallback serif, defines the tokens, and sets the square-corner reset. Sizes scale down on phones with `clamp()`; the max values are the desktop scale from section 3.

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap">
```

```css
:root {
  --yucg-navy: #1C366A;
  --yucg-navy-overlay: rgba(28, 54, 106, .72);
  --yucg-navy-45: rgba(28, 54, 106, .45);
  --yucg-navy-20: rgba(28, 54, 106, .20);
  --yucg-navy-06: rgba(28, 54, 106, .06);   /* faint fill for notes and drop zones */
  --yucg-white: #FFFFFF;
  --yucg-ink: #2F2E2E;
  --yucg-muted: #6E6D6C;                    /* hints, captions */
  --yucg-gray: #A0A09F;
  --yucg-rule: #E2E2E1;                     /* hairline dividers */

  --yucg-font-display: "YaleNew", "Libre Caslon Text", Georgia, "Times New Roman", serif;
  --yucg-font-body: "YaleNew", "Libre Caslon Text", Georgia, "Times New Roman", serif;
  --yucg-lh: 1.4;
  --yucg-size-hero: clamp(38px, 6.4vw, 56px);
  --yucg-size-h2: clamp(34px, 5.4vw, 50px);
  --yucg-size-section: clamp(32px, 5vw, 46px);
  --yucg-size-band: clamp(28px, 4.2vw, 38px);
  --yucg-size-lead: clamp(18px, 2.2vw, 22px);
  --yucg-size-ui: 16px;

  --yucg-radius: 0;
  --yucg-border: 1px solid currentColor;
  --yucg-section-pad: clamp(56px, 9vw, 104px);
  --yucg-gutter: clamp(16px, 4vw, 40px);
  --yucg-max: 1180px;
}
*, *::before, *::after { box-sizing: border-box; border-radius: 0; }
body { margin: 0; background: var(--yucg-white); color: var(--yucg-ink);
  font: 400 var(--yucg-size-ui)/var(--yucg-lh) var(--yucg-font-body); -webkit-font-smoothing: antialiased; }
h1, h2, h3, h4 { font-family: var(--yucg-font-display); font-weight: 700; color: var(--yucg-navy);
  line-height: var(--yucg-lh); margin: 0; text-wrap: balance; }
p { margin: 0; }
img { max-width: 100%; display: block; }
:focus-visible { outline: 2px solid var(--yucg-navy); outline-offset: 3px; }
.yucg-lead { font-size: var(--yucg-size-lead); max-width: 36em; }

/* yucg-container */
.yucg-container { max-width: var(--yucg-max); margin: 0 auto;
  padding-left: max(var(--yucg-gutter), env(safe-area-inset-left, 0px));
  padding-right: max(var(--yucg-gutter), env(safe-area-inset-right, 0px)); }

/* yucg-band: full-width section. Modifiers: --navy, --photo, --tight, --flush-top */
.yucg-band { padding-block: var(--yucg-section-pad); background: var(--yucg-white); }
.yucg-band--navy { background: var(--yucg-navy); color: var(--yucg-white); }
.yucg-band--navy :is(h1, h2, h3, .yucg-lead) { color: var(--yucg-white); }
.yucg-band--navy :focus-visible { outline-color: var(--yucg-white); }
.yucg-band--tight { padding-block: clamp(48px, 7vw, 80px); }
.yucg-band--flush-top { padding-top: 0; }
```

```html
<section class="yucg-band yucg-band--navy">
  <div class="yucg-container">…</div>
</section>
```

---

### 11.1 Page frame

#### `yucg-header` + `yucg-nav`

Logo left, bold navy text links right. Current page is full strength; others sit at 62% (no underline or pill, per section 5). Up to six links, then a "More" menu.

```html
<header class="yucg-header">
  <div class="yucg-container yucg-header__inner">
    <a class="yucg-header__brand" href="/">
      <img src="logo-light.png" alt="YUCG">
      <span>Analytics</span>               <!-- optional product name -->
    </a>
    <nav class="yucg-nav" aria-label="Main">
      <a href="/services">Services</a>
      <a href="/about" aria-current="page">About Us</a>
      <a href="/join">Join Us</a>
      <a href="/contact">Contact</a>
      <details class="yucg-nav__more">
        <summary>More</summary>
        <div><a href="/blog">Blog</a><a href="/faq">FAQ</a></div>
      </details>
    </nav>
  </div>
</header>
```

```css
.yucg-header { background: var(--yucg-white); border-bottom: 1px solid var(--yucg-rule); }
.yucg-header__inner { display: flex; align-items: center; justify-content: space-between;
  gap: 24px; flex-wrap: wrap; padding-block: 14px; }
.yucg-header__brand { display: flex; align-items: center; gap: 16px; text-decoration: none; }
.yucg-header__brand img { height: 52px; width: auto; }              /* site uses ~86px */
.yucg-header__brand span { font: 700 22px/1.1 var(--yucg-font-display); color: var(--yucg-navy);
  padding-left: 16px; border-left: 1px solid var(--yucg-gray); }

.yucg-nav { display: flex; align-items: center; gap: clamp(16px, 2.4vw, 32px); }
.yucg-nav a, .yucg-nav summary { font: 700 var(--yucg-size-ui)/1 var(--yucg-font-body);
  color: var(--yucg-navy); text-decoration: none; white-space: nowrap; padding-block: 6px;
  opacity: .62; transition: opacity .15s; cursor: pointer; list-style: none; }
.yucg-nav a:hover, .yucg-nav a[aria-current="page"], .yucg-nav summary:hover { opacity: 1; }
.yucg-nav__more { position: relative; }
.yucg-nav__more summary::-webkit-details-marker { display: none; }
.yucg-nav__more > div { position: absolute; right: 0; top: 100%; background: var(--yucg-white);
  border: 1px solid var(--yucg-navy); padding: 8px 18px; display: flex; flex-direction: column; z-index: 5; }
.yucg-nav__more > div a { padding-block: 8px; }
@media (max-width: 560px) {
  .yucg-header__inner { flex-direction: column; align-items: flex-start; gap: 10px; }
  .yucg-nav { overflow-x: auto; max-width: 100%; }
}
```

#### `yucg-footer` + `yucg-social`

```html
<footer class="yucg-footer">
  <div class="yucg-container yucg-footer__inner">
    <div>
      <img src="logo-light.png" alt="YUCG">
      <p>Yale Undergraduate Consulting Group<br>New Haven, CT</p>
      <p><a class="yucg-link" href="mailto:EMAIL">EMAIL</a></p>   <!-- replace EMAIL with the club address -->
    </div>
    <ul class="yucg-social">
      <li><a href="https://instagram.com/…" aria-label="Instagram"><svg>…</svg></a></li>
      <li><a href="https://facebook.com/…" aria-label="Facebook"><svg>…</svg></a></li>
      <li><a href="https://linkedin.com/…" aria-label="LinkedIn"><svg>…</svg></a></li>
    </ul>
  </div>
</footer>
```

```css
.yucg-footer { padding-block: 56px; border-top: 1px solid var(--yucg-rule); }
.yucg-footer__inner { display: flex; justify-content: space-between; align-items: flex-end; gap: 32px; flex-wrap: wrap; }
.yucg-footer img { height: 56px; width: auto; margin-bottom: 14px; }
.yucg-footer p { font-size: 15px; }
.yucg-social { display: flex; gap: 20px; list-style: none; margin: 0; padding: 0; }
.yucg-social svg { width: 24px; height: 24px; fill: var(--yucg-navy); display: block; }  /* monochrome */
.yucg-social a:hover svg { opacity: .7; }
```

---

### 11.2 Sections

#### `yucg-hero`

Full-bleed member photo, 72% navy overlay, stacked white title at line-height 1.0, two ghost buttons. Without a photo it falls back to solid navy.

```html
<section class="yucg-hero" style="--yucg-hero-img: url('members.jpg')">
  <div class="yucg-container">
    <h1>Yale Undergraduate<br>Consulting Group</h1>
    <p class="yucg-lead">High-impact, cross-industry business challenges, solved by the next generation of talent at Yale.</p>
    <div class="yucg-btn-group">
      <a class="yucg-btn yucg-btn--light" href="/about">About Us</a>
      <a class="yucg-btn yucg-btn--light" href="/join">Join Us</a>
    </div>
  </div>
</section>
```

```css
.yucg-hero { position: relative; color: var(--yucg-white); background: var(--yucg-navy) var(--yucg-hero-img, none) center/cover;
  min-height: clamp(520px, 80vh, 820px); display: flex; align-items: center; padding-block: var(--yucg-section-pad); }
.yucg-hero::before { content: ""; position: absolute; inset: 0; background: var(--yucg-navy-overlay); }
.yucg-hero > * { position: relative; width: 100%; }
.yucg-hero h1 { color: var(--yucg-white); font-size: var(--yucg-size-hero); line-height: 1; letter-spacing: .02em; }
.yucg-hero .yucg-lead { color: var(--yucg-white); margin-top: 24px; }
.yucg-hero .yucg-btn-group { margin-top: 40px; }
```

#### `yucg-page-hero`

Compact navy band that opens an inner page or tool. Kicker is sentence case, never uppercase.

```html
<section class="yucg-page-hero">
  <div class="yucg-container">
    <p class="yucg-page-hero__kicker">Reddit tool</p>
    <h1>Reddit Analyzer</h1>
    <p class="yucg-lead">Analyze sentiment of Reddit discussions on any topic across subreddits.</p>
  </div>
</section>
```

```css
.yucg-page-hero { background: var(--yucg-navy); color: var(--yucg-white); padding-block: clamp(48px, 7vw, 80px); }
.yucg-page-hero h1 { color: var(--yucg-white); font-size: var(--yucg-size-hero); line-height: 1; letter-spacing: .02em; }
.yucg-page-hero__kicker { opacity: .78; margin-bottom: 18px; }
.yucg-page-hero .yucg-lead { color: var(--yucg-white); margin-top: 20px; }
```

#### `yucg-split`

The "Who Are We?" pattern: feature heading broken over two lines on the left, lead copy on the right. Add `yucg-split--center` to vertically center (used inside navy bands).

```html
<section class="yucg-band">
  <div class="yucg-container yucg-split">
    <h2>Who<br>Are We?</h2>
    <div class="yucg-split__body">
      <p class="yucg-lead">YUCG is a student-led consulting group that partners with companies, startups and nonprofits on high-impact, cross-industry business challenges.</p>
    </div>
  </div>
</section>
```

```css
.yucg-split { display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: clamp(32px, 6vw, 96px); align-items: start; }
.yucg-split--center { align-items: center; }
.yucg-split > h2 { font-size: var(--yucg-size-h2); }
.yucg-split__body { display: flex; flex-direction: column; gap: 20px; min-width: 0; }
@media (max-width: 900px) { .yucg-split { grid-template-columns: minmax(0, 1fr); } }
```

#### `yucg-feature`

The "Explore YUCG" pattern: photo on one side, heading + copy + CTA on the other. Add `yucg-feature--reverse` to put the photo on the right.

```html
<section class="yucg-band">
  <div class="yucg-container yucg-feature">
    <img src="retreat.jpg" alt="YUCG members at the fall retreat">
    <div class="yucg-feature__body">
      <h2>Explore<br>YUCG</h2>
      <p class="yucg-lead">Beyond client work, members bond over retreats, project dinners, formals and trips to New York.</p>
      <a class="yucg-btn" href="/join">Join Us</a>
    </div>
  </div>
</section>
```

```css
.yucg-feature { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(32px, 6vw, 96px); align-items: center; }
.yucg-feature--reverse > img { order: 2; }
.yucg-feature > img { width: 100%; aspect-ratio: 4 / 3; object-fit: cover; }
.yucg-feature__body { display: flex; flex-direction: column; gap: 24px; align-items: flex-start; min-width: 0; }
.yucg-feature__body h2 { font-size: var(--yucg-size-h2); }
@media (max-width: 900px) { .yucg-feature { grid-template-columns: minmax(0, 1fr); } .yucg-feature--reverse > img { order: 0; } }
```

#### `yucg-section-title`

```html
<h2 class="yucg-section-title">Our Recent Clients</h2>
```

```css
.yucg-section-title { font-size: var(--yucg-size-section); text-align: center; margin-bottom: clamp(36px, 5vw, 64px); }
```

#### `yucg-navy-band`

The "Featured In" pattern. Combine with `yucg-split--center` for title-left, copy-right, or with `yucg-press` for thumbnails.

```html
<section class="yucg-band yucg-band--navy">
  <div class="yucg-container yucg-split yucg-split--center">
    <h2 class="yucg-band-title">Featured In</h2>
    <p class="yucg-lead">Business Insider, The Economist and the Yale Daily News have covered YUCG's work.</p>
  </div>
</section>
```

```css
.yucg-band-title { font-size: var(--yucg-size-band); color: var(--yucg-white); }
```

#### `yucg-columns`

Two to four text columns separated by gray hairlines, no cards. Good for services, practice areas or a tool list.

```html
<div class="yucg-columns" style="--cols: 3">
  <article>
    <h3>Strategy</h3>
    <p>Market entry, growth and competitive positioning.</p>
    <a class="yucg-btn" href="/services#strategy">Learn more</a>
  </article>
  <article>…</article>
  <article>…</article>
</div>
```

```css
.yucg-columns { display: grid; grid-template-columns: repeat(var(--cols, 3), minmax(0, 1fr)); }
.yucg-columns > * { padding: 8px clamp(20px, 3vw, 40px); display: flex; flex-direction: column; gap: 16px; }
.yucg-columns > * + * { border-left: 1px solid var(--yucg-rule); }
.yucg-columns h3 { font-size: 28px; }
.yucg-columns p { flex: 1; }
.yucg-columns .yucg-btn { align-self: flex-start; margin-top: 8px; }
@media (max-width: 900px) {
  .yucg-columns { grid-template-columns: minmax(0, 1fr); }
  .yucg-columns > * { padding: 28px 0; }
  .yucg-columns > * + * { border-left: 0; border-top: 1px solid var(--yucg-rule); }
}
```

---

### 11.3 Proof

#### `yucg-logo-wall`

Native-color logos, uniform height, centered grid, no borders or cards. Use `--logo-h` to set the height (100–160px on desktop).

```html
<section class="yucg-band">
  <div class="yucg-container">
    <h2 class="yucg-section-title">After YUCG</h2>
    <ul class="yucg-logo-wall" style="--logo-h: 72px">
      <li><img src="mckinsey.svg" alt="McKinsey & Company"></li>
      <li><img src="citadel.svg" alt="Citadel"></li>
      <li><img src="morgan-stanley.svg" alt="Morgan Stanley"></li>
    </ul>
  </div>
</section>
```

```css
.yucg-logo-wall { list-style: none; margin: 0; padding: 0; display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(160px, 40%), 1fr)); gap: clamp(28px, 4vw, 56px) clamp(24px, 4vw, 64px);
  align-items: center; justify-items: center; }
.yucg-logo-wall img { max-height: var(--logo-h, 80px); max-width: 100%; width: auto; object-fit: contain; }
```

#### `yucg-logo-row`

Single row of sponsor logos.

```html
<ul class="yucg-logo-row"><li><img src="sponsor-a.svg" alt="Sponsor A"></li>…</ul>
```

```css
.yucg-logo-row { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap;
  justify-content: center; align-items: center; gap: clamp(32px, 6vw, 96px); }
.yucg-logo-row img { max-height: var(--logo-h, 64px); width: auto; }
```

#### `yucg-press`

Square thumbnails on a navy band, each linking to the article.

```html
<section class="yucg-band yucg-band--navy">
  <div class="yucg-container">
    <h2 class="yucg-band-title">Featured In</h2>
    <ul class="yucg-press">
      <li><a href="https://…"><img src="economist.png" alt=""><span>The Economist</span></a></li>
      …
    </ul>
  </div>
</section>
```

```css
.yucg-press { list-style: none; margin: 32px 0 0; padding: 0; display: flex; flex-wrap: wrap; gap: 32px; }
.yucg-press a { display: flex; flex-direction: column; gap: 10px; color: var(--yucg-white); text-decoration: none; width: 129px; }
.yucg-press img { width: 129px; height: 129px; object-fit: cover; background: var(--yucg-white); }
.yucg-press a:hover img { opacity: .85; }
```

#### `yucg-stat-row`

Large proof numbers. Not on the current site; use it where logos can't carry the claim.

```html
<div class="yucg-stat-row">   <!-- placeholder numbers: use real figures -->
  <div><strong>120+</strong><span>Client projects</span></div>
  <div><strong>15</strong><span>Years at Yale</span></div>
  <div><strong>60</strong><span>Members</span></div>
</div>
```

```css
.yucg-stat-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); }
.yucg-stat-row > div { padding: 4px 24px; display: flex; flex-direction: column; }
.yucg-stat-row > div + div { border-left: 1px solid var(--yucg-rule); }
.yucg-stat-row strong { font: 700 clamp(40px, 5vw, 56px)/1.1 var(--yucg-font-display); color: var(--yucg-navy); font-variant-numeric: tabular-nums; }
.yucg-stat-row span { color: var(--yucg-muted); }
.yucg-band--navy .yucg-stat-row strong, .yucg-band--navy .yucg-stat-row span { color: var(--yucg-white); }
```

#### `yucg-quote`

```html
<figure class="yucg-quote">   <!-- placeholder quote -->
  <blockquote>The YUCG team gave us a market sizing we used in our Series A deck.</blockquote>
  <figcaption>Founder, consumer health startup</figcaption>
</figure>
```

```css
.yucg-quote { margin: 0; padding-left: 24px; border-left: 1px solid var(--yucg-navy); max-width: 40em; }
.yucg-quote blockquote { margin: 0; font: italic 400 var(--yucg-size-lead)/var(--yucg-lh) var(--yucg-font-body); }
.yucg-quote figcaption { margin-top: 12px; color: var(--yucg-muted); font-size: 15px; }
```

---

### 11.4 Actions

#### `yucg-btn`, `yucg-btn-group`

Navy ghost by default (white backgrounds). `yucg-btn--light` for navy bands and photos. `yucg-btn--block` for full width. Never rounded, never filled at rest.

```html
<div class="yucg-btn-group">
  <a class="yucg-btn" href="/about">About Us</a>
  <button class="yucg-btn" type="submit">Run analysis</button>
</div>
<a class="yucg-btn yucg-btn--light" href="/join">Join Us</a>
```

```css
.yucg-btn { display: inline-flex; align-items: center; justify-content: center; gap: 10px;
  background: transparent; border: 1px solid var(--yucg-navy); color: var(--yucg-navy);
  font: 400 var(--yucg-size-ui)/1 var(--yucg-font-body); padding: 13px 32px;
  cursor: pointer; text-decoration: none; white-space: nowrap; transition: background .15s, color .15s; }
.yucg-btn:hover { background: var(--yucg-navy); color: var(--yucg-white); }
.yucg-btn[disabled] { opacity: .45; cursor: not-allowed; background: transparent; color: var(--yucg-navy); }
.yucg-btn--light { border-color: var(--yucg-white); color: var(--yucg-white); }
.yucg-btn--light:hover { background: var(--yucg-white); color: var(--yucg-navy); }
.yucg-btn--block { width: 100%; }
.yucg-btn-group { display: flex; gap: 16px; flex-wrap: wrap; }
```

#### `yucg-segmented`

Mutually exclusive options. The selected one fills navy.

```html
<div class="yucg-segmented" role="group" aria-label="Mode">
  <button type="button" aria-pressed="true">Single subreddit</button>
  <button type="button" aria-pressed="false">Multi-subreddit</button>
</div>
```

```css
.yucg-segmented { display: grid; grid-auto-flow: column; grid-auto-columns: 1fr; }
.yucg-segmented button { font: 400 var(--yucg-size-ui)/1 var(--yucg-font-body); padding: 12px;
  border: 1px solid var(--yucg-navy); background: transparent; color: var(--yucg-navy); cursor: pointer; }
.yucg-segmented button + button { border-left: 0; }
.yucg-segmented button[aria-pressed="true"] { background: var(--yucg-navy); color: var(--yucg-white); }
```

```js
document.querySelectorAll('.yucg-segmented').forEach(g => g.addEventListener('click', e => {
  const b = e.target.closest('button'); if (!b) return;
  g.querySelectorAll('button').forEach(x => x.setAttribute('aria-pressed', x === b));
}));
```

#### `yucg-link`

Inline text link. Navy with an offset underline, never the Wix blue.

```css
.yucg-link { color: var(--yucg-navy); text-decoration: underline; text-underline-offset: 3px; text-decoration-thickness: 1px; }
.yucg-link:hover { text-decoration-thickness: 2px; }
```

---

### 11.5 Forms

Inputs have no box. A 1px gray underline turns navy on focus, which keeps "borders only on buttons" while still reading as a field.

#### `yucg-field` (text, number, password, select, textarea)

```html
<div class="yucg-field">
  <label for="sub">Subreddit</label>
  <div class="yucg-field__control"><span class="yucg-field__prefix">r/</span><input id="sub" type="text" placeholder="travel"></div>
  <span class="yucg-field__hint">Without "r/".</span>
</div>

<div class="yucg-field">
  <label for="range">Time range</label>
  <div class="yucg-field__control"><select id="range"><option>Past year</option></select></div>
</div>
```

```css
.yucg-field { display: flex; flex-direction: column; gap: 6px; }
.yucg-field > label { font-weight: 700; color: var(--yucg-navy); font-size: 15px; }
.yucg-field__hint { font-size: 14px; color: var(--yucg-muted); }
.yucg-field__error { font-size: 14px; color: var(--yucg-ink); }
.yucg-field__control { display: flex; align-items: center; gap: 6px; border-bottom: 1px solid var(--yucg-gray); transition: border-color .15s; }
.yucg-field__control:focus-within { border-color: var(--yucg-navy); box-shadow: 0 1px 0 var(--yucg-navy); }
.yucg-field__prefix { color: var(--yucg-navy); font-weight: 700; }
.yucg-field__control :is(input, select, textarea) { font: 400 var(--yucg-size-ui)/1.4 var(--yucg-font-body);
  color: var(--yucg-ink); background: transparent; border: 0; padding: 10px 0; width: 100%; min-width: 0; outline: none; }
.yucg-field__control input::placeholder { color: var(--yucg-gray); }
.yucg-field__control select { appearance: none; cursor: pointer; padding-right: 28px;
  background-image: linear-gradient(45deg, transparent 50%, var(--yucg-navy) 50%), linear-gradient(135deg, var(--yucg-navy) 50%, transparent 50%);
  background-position: calc(100% - 12px) 55%, calc(100% - 7px) 55%; background-size: 5px 5px; background-repeat: no-repeat; }
```

#### `yucg-range`

```html
<div class="yucg-field">
  <label for="n">Max locations</label>
  <div class="yucg-range"><input id="n" type="range" min="1" max="20" value="10"><output for="n">10</output></div>
</div>
```

```css
.yucg-range { display: flex; align-items: center; gap: 14px; }
.yucg-range input { width: 100%; accent-color: var(--yucg-navy); }
.yucg-range output { font-weight: 700; color: var(--yucg-navy); min-width: 2ch; text-align: right; font-variant-numeric: tabular-nums; }
```

```js
document.querySelectorAll('.yucg-range input').forEach(r => r.addEventListener('input', () => r.nextElementSibling.value = r.value));
```

#### `yucg-check`

```html
<label class="yucg-check"><input type="checkbox"> Include comments</label>
```

```css
.yucg-check { display: flex; gap: 10px; align-items: baseline; padding: 6px 0; cursor: pointer; }
.yucg-check input { accent-color: var(--yucg-navy); }
```

#### `yucg-dropzone`

```html
<label class="yucg-dropzone" for="files">
  <strong>Drop transcript files here or click to browse</strong>
  <span>.docx and .txt</span>
  <input id="files" type="file" multiple hidden>
</label>
```

```css
.yucg-dropzone { display: flex; flex-direction: column; align-items: center; gap: 8px; text-align: center;
  padding: 40px 20px; background: var(--yucg-navy-06); outline: 1px dashed var(--yucg-gray); outline-offset: -1px;
  cursor: pointer; transition: background .15s; }
.yucg-dropzone:hover, .yucg-dropzone.is-over { background: var(--yucg-navy-20); }
.yucg-dropzone strong { color: var(--yucg-navy); font-size: 18px; }
.yucg-dropzone span { color: var(--yucg-muted); }
```

```js
document.querySelectorAll('.yucg-dropzone').forEach(z => {
  ['dragenter', 'dragover'].forEach(t => z.addEventListener(t, e => { e.preventDefault(); z.classList.add('is-over'); }));
  ['dragleave', 'drop'].forEach(t => z.addEventListener(t, e => { e.preventDefault(); z.classList.remove('is-over'); }));
  // on 'drop', read e.dataTransfer.files
});
```

#### `yucg-note`

Instructions or a short callout. Faint navy fill, no border.

```html
<p class="yucg-note"><strong>Instructions:</strong> Enter a subreddit and a search query.</p>
```

```css
.yucg-note { background: var(--yucg-navy-06); padding: 16px 18px; font-size: 15px; }
.yucg-note strong { color: var(--yucg-navy); }
```

#### `yucg-form-group`

Titled group of fields with a navy rule under the title.

```html
<fieldset class="yucg-form-group">
  <legend>Settings</legend>
  <!-- yucg-field, yucg-range … -->
</fieldset>
```

```css
.yucg-form-group { border: 0; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 18px; }
.yucg-form-group > legend { width: 100%; padding: 0 0 8px; margin-bottom: 18px; border-bottom: 1px solid var(--yucg-navy);
  font: 700 20px/1.4 var(--yucg-font-display); color: var(--yucg-navy); }
```

---

### 11.6 Data

Graph components (`yucg-chart-tokens`, `yucg-chart-block`, `yucg-legend`, `yucg-bars`, `yucg-diverging`, `yucg-mix`, `yucg-line-chart`) follow the Data Visualization studio rules in section 10: Lato, all text `#00346B`, centered title and legend, dashed gridlines, studio series colors. `yucg-kpis`, `yucg-table` and `yucg-chip` are page UI and stay in the website serif.

#### `yucg-chart-tokens`

Include once on any page with a chart. The Lato link replaces the one in 11.0 (it loads both families).

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lato:wght@400;700&family=Libre+Caslon+Text:ital,wght@0,400;0,700;1,400&display=swap">
```

```css
:root {
  --yucg-font-chart: "Lato", "Helvetica Neue", Arial, sans-serif;
  --yucg-chart-text: #00346B;                   /* every word in a chart */
  --yucg-chart-1: #1C366A;  --yucg-chart-2: #3465A8;  --yucg-chart-3: #7AA7D6;  --yucg-chart-4: #445469;
  --yucg-chart-5: #909AB1;  --yucg-chart-6: #C4D4E8;  --yucg-chart-7: #0B1F3A;  --yucg-chart-8: #DFE6EF;
  --yucg-chart-focus: #1C366A;
  --yucg-chart-context: #C9CED6;
  --yucg-chart-grid: rgba(0, 52, 107, .6);      /* dashed, 0.8px, horizontal only */
  --yucg-chart-axis: rgba(0, 52, 107, .6);      /* bar baselines; line charts have none */
  --yucg-seq-1: #F1F5FA;  --yucg-seq-2: #C4D4E8;  --yucg-seq-3: #7AA7D6;  --yucg-seq-4: #1164A3;  --yucg-seq-5: #1C366A;
}
/* Series swatch classes: set --c, which every graph component paints with */
.is-c1 { --c: var(--yucg-chart-1); } .is-c2 { --c: var(--yucg-chart-2); } .is-c3 { --c: var(--yucg-chart-3); } .is-c4 { --c: var(--yucg-chart-4); }
.is-c5 { --c: var(--yucg-chart-5); } .is-c6 { --c: var(--yucg-chart-6); } .is-c7 { --c: var(--yucg-chart-7); } .is-c8 { --c: var(--yucg-chart-8); }
.is-focus { --c: var(--yucg-chart-focus); }
.is-context, .is-secondary { --c: var(--yucg-chart-context); }
.is-pos { --c: var(--yucg-chart-1); }         /* sentiment: positive */
.is-neu { --c: var(--yucg-chart-context); }   /* neutral */
.is-neg { --c: var(--yucg-chart-3); }         /* negative */
```

#### `yucg-kpis`

Page UI, not a chart: stays in the website serif.

```html
<div class="yucg-kpis">
  <div><strong>260</strong><span>Posts analyzed</span></div>
  <div><strong>+0.21</strong><span>Mean sentiment</span></div>
  <div><strong>58%</strong><span>Positive posts</span></div>
</div>
```

```css
.yucg-kpis { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); row-gap: 20px; }
.yucg-kpis > div { padding: 4px 20px; display: flex; flex-direction: column; }
.yucg-kpis > div:first-child { padding-left: 0; }
.yucg-kpis > div + div { border-left: 1px solid var(--yucg-rule); }
.yucg-kpis strong { font: 700 clamp(28px, 3.4vw, 38px)/1.2 var(--yucg-font-display); color: var(--yucg-navy); font-variant-numeric: tabular-nums; }
.yucg-kpis span { font-size: 14px; color: var(--yucg-muted); }
```

#### `yucg-chart-block` (wrapper for any chart)

The studio layout: centered takeaway title, centered subtitle, centered legend, the chart, then the source line bottom left. Transparent background, no logo.

```html
<figure class="yucg-chart-block">
  <figcaption>
    <strong>Visits doubled after the October launch</strong>
    <span>Daily visits and analyses run, last 30 days</span>
  </figcaption>
  <div class="yucg-legend">…</div>
  <!-- yucg-bars / yucg-diverging / yucg-mix / yucg-line-chart -->
  <p class="yucg-chart-source">Source: YUCG Analytics logs; YUCG analysis</p>
</figure>
```

```css
.yucg-chart-block { margin: 0; display: flex; flex-direction: column; gap: 14px; background: transparent;
  font-family: var(--yucg-font-chart); color: var(--yucg-chart-text); }
.yucg-chart-block figcaption { display: flex; flex-direction: column; gap: 4px; text-align: center; }
.yucg-chart-block figcaption strong { font: 700 clamp(18px, 2.2vw, 24px)/1.3 var(--yucg-font-chart); color: var(--yucg-chart-text); text-wrap: balance; }
.yucg-chart-block figcaption span { font: 400 14.7px/1.4 var(--yucg-font-chart); }
.yucg-chart-source { margin: 0; font: 400 11.7px/1.4 var(--yucg-font-chart); color: var(--yucg-chart-text); text-align: left; }
```

#### `yucg-legend`

Centered under the title. Square swatches for bars; add `is-line` for a line sample, plus `is-dotted` for a fitted or forecast series. Color comes from a swatch class (`is-c1`…`is-c8`, `is-pos`…) or an inline `--c`.

```html
<div class="yucg-legend">
  <span><i class="is-line is-c1"></i>Actual</span>
  <span><i class="is-line is-dotted is-c1"></i>Fitted</span>
  <span><i class="is-c3"></i>Bar series</span>
</div>
```

```css
.yucg-legend { display: flex; justify-content: center; gap: 8px 22px; flex-wrap: wrap;
  font: 400 13.5px/1.3 var(--yucg-font-chart); color: var(--yucg-chart-text); }
.yucg-legend span { display: inline-flex; align-items: center; gap: 8px; }
.yucg-legend i { width: 12px; height: 12px; display: inline-block; background: var(--c, var(--yucg-chart-1)); }
.yucg-legend i.is-line { width: 28px; height: 0; background: none; border-top: 2.8px solid var(--c, var(--yucg-chart-1)); }
.yucg-legend i.is-dotted { border-top-style: dotted; }
```

#### `yucg-bars`

Horizontal bars in HTML with a thin baseline. Width is a percentage of the largest value. Bars default to navy; use `is-c2`…`is-c8` for categories, or `is-focus` / `is-context` to highlight one bar. The value `<b>` is a data label: keep it only where the reader needs the number.

```html
<div class="yucg-bars">
  <div><span>Reddit Analyzer</span><i class="is-focus" style="width:100%"></i><b>96</b></div>
  <div><span>Sentiment Analyzer</span><i class="is-context" style="width:64%"></i><b>61</b></div>
  <div><span>Google Reviews</span><i class="is-context" style="width:57%"></i><b>55</b></div>
</div>
```

```css
.yucg-bars { --label-w: 150px; position: relative; display: flex; flex-direction: column; gap: 8px;
  font: 400 12.5px/1.3 var(--yucg-font-chart); color: var(--yucg-chart-text); }
.yucg-bars::before { content: ""; position: absolute; top: -4px; bottom: -4px; left: calc(var(--label-w) + 12px);
  border-left: 1px solid var(--yucg-chart-axis); }                         /* thin baseline */
.yucg-bars > div { display: grid; grid-template-columns: var(--label-w) minmax(0, 1fr) 48px; gap: 12px; align-items: center; }
.yucg-bars span { text-align: right; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.yucg-bars i { display: block; height: 20px; background: var(--c, var(--yucg-chart-1)); }
.yucg-bars b { font-weight: 700; font-variant-numeric: tabular-nums; }
@media (max-width: 560px) { .yucg-bars { --label-w: 96px; } }
```

#### `yucg-diverging`

Scores from −1 to +1. Positive grows right in navy, negative grows left in sky (`is-neg`). The signed value always shows, so color is never the only cue. `left` and `width` are percentages of the track (center = 50%).

```html
<div class="yucg-diverging">
  <div><span>Erin Yoon</span><p><i style="left:50%;width:21%"></i></p><b>+0.42</b></div>
  <div><span>Marcus Lee</span><p><i class="is-neg" style="left:44%;width:6%"></i></p><b>−0.12</b></div>
</div>
```

```css
.yucg-diverging { --label-w: 150px; display: flex; flex-direction: column; gap: 8px;
  font: 400 12.5px/1.3 var(--yucg-font-chart); color: var(--yucg-chart-text); }
.yucg-diverging > div { display: grid; grid-template-columns: var(--label-w) minmax(0, 1fr) 48px; gap: 12px; align-items: center; }
.yucg-diverging span { text-align: right; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.yucg-diverging p { position: relative; height: 20px; margin: 0;
  background: linear-gradient(var(--yucg-chart-axis), var(--yucg-chart-axis)) center / 1px 100% no-repeat; }  /* zero line */
.yucg-diverging i { position: absolute; top: 0; bottom: 0; background: var(--c, var(--yucg-chart-1)); }
.yucg-diverging b { font-weight: 700; font-variant-numeric: tabular-nums; }
@media (max-width: 560px) { .yucg-diverging { --label-w: 96px; } }
```

```js
// value in [-1, 1] → inline style for the <i>; add class="is-neg" when v < 0
const divStyle = v => `left:${v >= 0 ? 50 : 50 + v * 50}%;width:${Math.abs(v) * 50}%`;
```

#### `yucg-mix`

100% stacked bar for shares. Sentiment uses `is-pos` (navy), `is-neu` (context gray), `is-neg` (sky); other shares use `is-c1`…`is-c8` in order. Percent labels sit inside segments wider than 8%.

```html
<div class="yucg-legend"><span><i class="is-pos"></i>Positive</span><span><i class="is-neu"></i>Neutral</span><span><i class="is-neg"></i>Negative</span></div>
<div class="yucg-mix" role="img" aria-label="Positive 58%, neutral 27%, negative 15%">
  <i class="is-pos" style="width:58%">58%</i><i class="is-neu" style="width:27%">27%</i><i class="is-neg" style="width:15%">15%</i>
</div>
```

```css
.yucg-mix { display: flex; height: 36px; }
.yucg-mix i { display: flex; align-items: center; justify-content: center; overflow: hidden;
  font: 700 12.5px/1 var(--yucg-font-chart); font-style: normal; font-variant-numeric: tabular-nums;
  background: var(--c, var(--yucg-chart-1)); color: var(--yucg-chart-text); }
.yucg-mix i:is(.is-pos, .is-focus, .is-c1, .is-c2, .is-c4, .is-c7) { color: #FFFFFF; }   /* white on dark fills */
```

#### `yucg-line-chart`

SVG line chart from `yucgLineChart()`. Lato, all text `#00346B`, horizontal dashed gridlines, no axis line, 2.8px lines with no markers, optional rotated y-axis title. Colors come from `chart-1`…`chart-8` in order. A series whose name contains *fitted*, *forecast*, *projected* or *estimated* is drawn dotted in the color of the series before it. Pair it with `yucgLegend()` inside a `yucg-chart-block`.

```css
.yucg-line-chart svg { width: 100%; height: auto; display: block; overflow: visible; background: transparent; }
.yucg-line-chart text { font-family: var(--yucg-font-chart); font-size: 12px; fill: var(--yucg-chart-text); }
.yucg-line-chart .y-title { font-size: 12.5px; font-weight: 700; }
```

```js
const YUCG_CHART = ['#1C366A', '#3465A8', '#7AA7D6', '#445469', '#909AB1', '#C4D4E8', '#0B1F3A', '#DFE6EF'];
const yucgIsDotted = name => /fitted|forecast|projected|estimated/i.test(name || '');
// Studio color order; a dotted series reuses the color of the series before it. Never cycles past chart-8.
function yucgSeriesColors(series) {
  let k = 0, last;
  return series.map(s => {
    if (s.color) return (last = s.color);
    if (yucgIsDotted(s.name) && last) return last;
    return (last = YUCG_CHART[Math.min(k++, 7)]);
  });
}
// yucgLegend(series, 'line' | 'bar') → centered legend markup
function yucgLegend(series, kind = 'line') {
  const c = yucgSeriesColors(series);
  return `<div class="yucg-legend">${series.map((s, i) =>
    `<span><i class="${kind === 'line' ? 'is-line' + (yucgIsDotted(s.name) ? ' is-dotted' : '') : ''}" style="--c:${c[i]}"></i>${s.name}</span>`).join('')}</div>`;
}
// yucgLineChart({ labels: [...], series: [{ name, values, color? }], min, max, yTitle, fmtY })
function yucgLineChart({ labels, series, min = 0, max, yTitle = '', fmtY = v => v.toLocaleString('en-US') }) {
  const W = 720, H = 280, m = { t: 12, r: 16, b: 34, l: yTitle ? 72 : 48 };
  const hi = max ?? (v => { const p = 10 ** Math.floor(Math.log10(v || 1)); return Math.ceil(v / p) * p; })(Math.max(...series.flatMap(s => s.values)));
  const x = i => m.l + (W - m.l - m.r) * i / Math.max(labels.length - 1, 1);
  const y = v => H - m.b - (H - m.t - m.b) * (v - min) / (hi - min);
  const colors = yucgSeriesColors(series);
  let g = '';
  for (let k = 0; k <= 4; k++) {
    const v = min + (hi - min) * k / 4;
    g += `<line x1="${m.l}" x2="${W - m.r}" y1="${y(v)}" y2="${y(v)}" stroke="rgba(0,52,107,.6)" stroke-width=".8" stroke-dasharray="4 4"/>`
       + `<text x="${m.l - 8}" y="${y(v) + 4}" text-anchor="end">${fmtY(v)}</text>`;
  }
  if (yTitle) g += `<text class="y-title" transform="rotate(-90)" x="${-(m.t + (H - m.t - m.b) / 2)}" y="16" text-anchor="middle">${yTitle}</text>`;
  const step = Math.ceil(labels.length / 8);
  labels.forEach((l, i) => { if (i % step === 0 || i === labels.length - 1) g += `<text x="${x(i)}" y="${H - 10}" text-anchor="middle">${l}</text>`; });
  series.forEach((s, n) => {
    const d = s.values.map((v, i) => `${i ? 'L' : 'M'}${x(i).toFixed(1)},${y(v).toFixed(1)}`).join('');
    const dots = yucgIsDotted(s.name) ? ' stroke-dasharray="0.1 6" stroke-linecap="round"' : '';
    g += `<path d="${d}" fill="none" stroke="${colors[n]}" stroke-width="2.8" stroke-linejoin="round"${dots}/>`;
  });
  return `<div class="yucg-line-chart"><svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${series.map(s => s.name).join(', ')}">${g}</svg></div>`;
}
```

Full example:

```js
const series = [{ name: 'Actual', values: actual }, { name: 'Fitted', values: fitted }];
document.querySelector('#chart').innerHTML = `
  <figure class="yucg-chart-block">
    <figcaption><strong>Arrivals track the model closely</strong><span>Monthly arrivals, millions</span></figcaption>
    ${yucgLegend(series)}
    ${yucgLineChart({ labels: months, series, yTitle: 'Arrivals (Millions)' })}
    <p class="yucg-chart-source">Source: Turkish Ministry of Culture and Tourism; YUCG analysis</p>
  </figure>`;
```

#### `yucg-table`

```html
<div class="yucg-table">
  <table>
    <thead><tr><th>Post</th><th>Subreddit</th><th class="is-num">Upvotes</th></tr></thead>
    <tbody><tr><td>Upgraded today and loved it</td><td>r/travel</td><td class="is-num">1,204</td></tr></tbody>
  </table>
</div>
```

```css
.yucg-table { overflow-x: auto; }
.yucg-table table { border-collapse: collapse; width: 100%; font-size: 15px; }
.yucg-table th { text-align: left; font-weight: 700; color: var(--yucg-navy); padding: 10px 12px 10px 0;
  border-bottom: 1px solid var(--yucg-navy); white-space: nowrap; }
.yucg-table td { padding: 12px 12px 12px 0; border-bottom: 1px solid var(--yucg-rule); vertical-align: top; }
.yucg-table .is-num { text-align: right; font-variant-numeric: tabular-nums; }
```

#### `yucg-chip`

```html
<div class="yucg-chips"><span class="yucg-chip">friendly · +0.71</span><span class="yucg-chip is-neg">slow · −0.45</span></div>
```

```css
.yucg-chips { display: flex; flex-wrap: wrap; gap: 8px; }
.yucg-chip { font-size: 14px; padding: 6px 12px; border: 1px solid var(--yucg-navy); color: var(--yucg-navy); }
.yucg-chip.is-neg { border-color: var(--yucg-gray); color: var(--yucg-ink); }
```

---

### 11.7 Disclosure

#### `yucg-accordion`

FAQ rows or per-item detail. Uses native `<details>`, so it works with no script.

```html
<div class="yucg-accordion">
  <details open>
    <summary>How do I apply to YUCG?</summary>
    <div>Applications open at the start of each semester…</div>
  </details>
</div>
```

```css
.yucg-accordion details { border-bottom: 1px solid var(--yucg-rule); }
.yucg-accordion details:first-child { border-top: 1px solid var(--yucg-rule); }
.yucg-accordion summary { cursor: pointer; padding: 18px 0; list-style: none;
  font: 700 20px/1.4 var(--yucg-font-display); color: var(--yucg-navy); }
.yucg-accordion summary::-webkit-details-marker { display: none; }
.yucg-accordion summary::before { content: "+ "; color: var(--yucg-gray); }
.yucg-accordion details[open] summary::before { content: "– "; }
.yucg-accordion details > div { padding-bottom: 22px; max-width: 40em; }
```

#### `yucg-tabs`

Text tabs in the nav style; the active tab is full strength with a navy rule beneath.

```html
<div class="yucg-tabs" role="tablist">
  <button role="tab" aria-selected="true">Overview</button>
  <button role="tab" aria-selected="false">Results</button>
</div>
```

```css
.yucg-tabs { display: flex; gap: 28px; border-bottom: 1px solid var(--yucg-rule); overflow-x: auto; }
.yucg-tabs button { background: none; border: 0; padding: 12px 0; margin-bottom: -1px; cursor: pointer;
  font: 700 var(--yucg-size-ui)/1 var(--yucg-font-body); color: var(--yucg-navy); opacity: .62;
  border-bottom: 1px solid transparent; white-space: nowrap; }
.yucg-tabs button[aria-selected="true"] { opacity: 1; border-bottom-color: var(--yucg-navy); }
```

#### `yucg-gate`

Small centered form for a password, newsletter sign-up or one-question prompt.

```html
<form class="yucg-gate">
  <h2>Analytics Access</h2>
  <p>Enter the analytics password to continue.</p>
  <div class="yucg-field"><label for="pw">Password</label><div class="yucg-field__control"><input id="pw" type="password"></div></div>
  <button class="yucg-btn yucg-btn--block" type="submit">Unlock</button>
</form>
```

```css
.yucg-gate { max-width: 420px; margin: 0 auto; display: flex; flex-direction: column; gap: 22px; }
.yucg-gate h2 { font-size: 32px; }
```

---

### 11.8 Recipes

Ready-made page outlines. Ask for a recipe by name.

| Recipe | Components, top to bottom |
|---|---|
| **Home page** | `yucg-header` → `yucg-hero` → `yucg-split` ("Who Are We?") → `yucg-feature` ("Explore YUCG") → `yucg-section-title` + `yucg-logo-wall` (clients) → `yucg-section-title` + `yucg-logo-row` (sponsors) → `yucg-section-title` + `yucg-logo-wall` (After YUCG) → `yucg-press` on `yucg-band--navy` → `yucg-footer` |
| **Inner page** | `yucg-header` → `yucg-page-hero` → `yucg-split` → `yucg-columns` → `yucg-navy-band` → `yucg-footer` |
| **Tool page** | `yucg-header` → `yucg-page-hero` → two columns: form (`yucg-note`, `yucg-segmented`, `yucg-form-group` of `yucg-field`s, `yucg-btn--block`) and results (`yucg-kpis`, `yucg-chart-block`s, `yucg-table`) → `yucg-footer` |
| **Dashboard** | `yucg-header` → `yucg-page-hero` → `yucg-kpis` → `yucg-chart-block` with `yucg-line-chart` beside one with `yucg-bars` → `yucg-table` → `yucg-footer` |
| **FAQ** | `yucg-header` → `yucg-page-hero` → `yucg-accordion` → `yucg-navy-band` (contact prompt) → `yucg-footer` |
| **Recruiting** | `yucg-header` → `yucg-hero` → `yucg-stat-row` → `yucg-feature` → `yucg-quote` → `yucg-accordion` (timeline / FAQ) → `yucg-navy-band` with `yucg-btn--light` → `yucg-footer` |

Tool-page two-column layout:

```css
.yucg-workspace { display: grid; grid-template-columns: minmax(0, 380px) minmax(0, 1fr); gap: clamp(32px, 5vw, 72px); align-items: start; }
.yucg-workspace > * { display: flex; flex-direction: column; gap: 32px; min-width: 0; }
@media (max-width: 900px) { .yucg-workspace { grid-template-columns: minmax(0, 1fr); } }
```
