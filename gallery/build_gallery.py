import re, base64, urllib.parse, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
md = open(os.path.join(ROOT, 'design.md')).read()
lib = md[md.index('## 11. Component Library'):]
css = '\n'.join(re.findall(r'```css\n(.*?)```', lib, re.S))
js = '\n'.join(re.findall(r'```js\n(.*?)```', lib, re.S))
logo = 'data:image/png;base64,' + base64.b64encode(open(os.path.join(ROOT, 'assets', 'logo-light.png'),'rb').read()).decode()
def mark(name, italic=False):
    w = 18 * len(name) + 20
    it = 'font-style="italic"' if italic else ''
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 48"><text x="{w/2}" y="34" text-anchor="middle" font-family="Georgia,serif" font-size="30" font-weight="700" {it} fill="#A0A09F">{name}</text></svg>'
    return 'data:image/svg+xml,' + urllib.parse.quote(svg)
names = ['Halcyon','Meridian','Bellweather','Arbor &amp; Co.','Kestrel','Lumen Health','Northfield','Quarry']
logos = lambda ns: ''.join(f'<li><img src="{mark(n, i%3==1)}" alt="{n} (placeholder)"></li>' for i, n in enumerate(ns))
def thumb(t):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 129 129"><rect width="129" height="129" fill="#fff"/><text x="64.5" y="76" text-anchor="middle" font-family="Georgia,serif" font-size="30" font-weight="700" fill="#1C366A">{t}</text></svg>'
    return 'data:image/svg+xml,' + urllib.parse.quote(svg)
press = ''.join(f'<li><a href="#yucg-press"><img src="{thumb(i)}" alt=""><span>{n}</span></a></li>' for i, n in [('BI','Business Insider'),('E','The Economist'),('YDN','Yale Daily News')])
s = open(os.path.join(HERE,'gallery-src.html')).read()
s = s.replace('{{LIB_CSS}}', css).replace('{{LIB_JS}}', js).replace('{{LOGO}}', logo).replace('{{LOGOS8}}', logos(names)).replace('{{LOGOS4}}', logos(names[:4])).replace('{{PRESS}}', press)
open(os.path.join(HERE,'yucg-components.html'), 'w').write(s)
print(len(css), len(js), len(s))
