"""Original flat illustrations for the industry pages, written as SVG files.

Each one is 400 x 240, with a soft gradient background, one main scene and a little motion
(flames, steam, sparkles) that stops for people who prefer reduced motion.
"""
import os

W, H = 400, 240
FONT = "Inter, -apple-system, 'Segoe UI', Arial, sans-serif"

BASE_STYLE = """
.tw{animation:tw 2.6s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.tw2{animation:tw 3.1s ease-in-out .8s infinite;transform-box:fill-box;transform-origin:center}
.fl{animation:fl 1.4s ease-in-out infinite;transform-box:fill-box;transform-origin:50% 100%}
.fl2{animation:fl 1.7s ease-in-out .3s infinite;transform-box:fill-box;transform-origin:50% 100%}
.st{animation:st 3.2s ease-in-out infinite}
.st2{animation:st 3.2s ease-in-out 1.1s infinite}
.fo{animation:fo 4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}
.fo2{animation:fo 4.6s ease-in-out 1.2s infinite;transform-box:fill-box;transform-origin:center}
.dr{animation:dr 2.4s ease-in infinite}
@keyframes tw{0%,100%{opacity:.25;transform:scale(.7)}50%{opacity:1;transform:scale(1)}}
@keyframes fl{0%,100%{transform:scaleY(1) rotate(-3deg)}50%{transform:scaleY(1.18) rotate(3deg)}}
@keyframes st{0%{opacity:0;transform:translateY(8px)}35%{opacity:.85}100%{opacity:0;transform:translateY(-16px)}}
@keyframes fo{0%,100%{transform:translateY(0)}50%{transform:translateY(-6px)}}
@keyframes dr{0%{opacity:0;transform:translateY(-4px)}20%{opacity:1}80%{opacity:1;transform:translateY(16px)}100%{opacity:0;transform:translateY(18px)}}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
"""


def spark(x, y, s=9, color="#FFFFFF", cls="tw"):
    """Four-point sparkle."""
    return (f'<path class="{cls}" d="M{x} {y - s} Q{x + s * .18} {y - s * .18} {x + s} {y} Q{x + s * .18} {y + s * .18} {x} {y + s} '
            f'Q{x - s * .18} {y + s * .18} {x - s} {y} Q{x - s * .18} {y - s * .18} {x} {y - s}Z" fill="{color}"/>')


def svg(bg1, bg2, body, extra_style=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img">
<style>{BASE_STYLE}{extra_style}</style>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{bg1}"/><stop offset="1" stop-color="{bg2}"/></linearGradient>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#FFFFFF" stop-opacity=".75"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient></defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<circle cx="335" cy="38" r="88" fill="#FFFFFF" opacity=".28"/>
<circle cx="40" cy="225" r="70" fill="#FFFFFF" opacity=".22"/>
<ellipse cx="200" cy="132" rx="150" ry="100" fill="url(#glow)"/>
{body}
</svg>'''


ART = {}

# 1. Bakery: two-tier cake with candles, and a calendar page
ART["bakeries-and-cake-shops"] = svg("#FFE7E0", "#FFD3C7", f'''
<ellipse cx="205" cy="214" rx="104" ry="9" fill="#C9786B" opacity=".18"/>
<rect x="196" y="196" width="18" height="18" rx="3" fill="#F1D9D2"/>
<ellipse cx="205" cy="215" rx="44" ry="6" fill="#F1D9D2"/>
<ellipse cx="205" cy="196" rx="100" ry="10" fill="#FFFFFF"/>
<rect x="128" y="138" width="154" height="56" rx="12" fill="#FFF4E8"/>
<path d="M128 150 q0-12 12-12 h130 q12 0 12 12 v6 q-6 10-12 0 q-6-10-12 2 q-7 14-14 0 q-7-12-14 2 q-6 12-13 0 q-7-12-14 3 q-6 13-13 0 q-6-11-13 1 q-7 14-14 0 q-6-10-12 0 q-6 10-12 0 q-6-10-12 0Z" fill="#F57FA0"/>
<rect x="152" y="96" width="106" height="44" rx="10" fill="#FFF4E8"/>
<path d="M152 106 q0-10 10-10 h86 q10 0 10 10 v5 q-6 9-11 0 q-6-9-12 2 q-6 12-12 0 q-6-10-12 1 q-6 12-12 0 q-6-10-12 1 q-6 11-12 0 q-6-9-11 1 q-4 8-8 0Z" fill="#8B5A3C"/>
<g fill="#FFFFFF"><circle cx="150" cy="176" r="2.4"/><circle cx="176" cy="168" r="2.4"/><circle cx="212" cy="178" r="2.4"/><circle cx="246" cy="170" r="2.4"/><circle cx="266" cy="180" r="2.4"/></g>
<g><rect x="166" y="181" width="7" height="3" rx="1.5" fill="#FFD166" transform="rotate(30 169 182)"/><rect x="232" y="182" width="7" height="3" rx="1.5" fill="#7CC6FE" transform="rotate(-25 235 183)"/><rect x="196" y="170" width="7" height="3" rx="1.5" fill="#9AE6B4" transform="rotate(15 199 171)"/></g>
<g><rect x="181" y="68" width="7" height="30" rx="2" fill="#7CC6FE"/><rect x="202" y="62" width="7" height="36" rx="2" fill="#FFD166"/><rect x="223" y="68" width="7" height="30" rx="2" fill="#F57FA0"/>
<path d="M181 76 l7-4 M181 86 l7-4 M202 72 l7-4 M202 82 l7-4 M202 92 l7-4 M223 76 l7-4 M223 86 l7-4" stroke="#FFFFFF" stroke-width="2" opacity=".7"/></g>
<g class="fl"><path d="M184.5 66 c-5-6-3-12 0-16 c3 4 5 10 0 16Z" fill="#FFB020"/><path d="M184.5 64 c-2-3-1-6 0-8 c1 2 2 5 0 8Z" fill="#FFF3C4"/></g>
<g class="fl2"><path d="M205.5 60 c-5-6-3-12 0-16 c3 4 5 10 0 16Z" fill="#FFB020"/><path d="M205.5 58 c-2-3-1-6 0-8 c1 2 2 5 0 8Z" fill="#FFF3C4"/></g>
<g class="fl"><path d="M226.5 66 c-5-6-3-12 0-16 c3 4 5 10 0 16Z" fill="#FFB020"/><path d="M226.5 64 c-2-3-1-6 0-8 c1 2 2 5 0 8Z" fill="#FFF3C4"/></g>
<g class="fo"><g transform="rotate(-9 78 102)"><rect x="42" y="62" width="74" height="82" rx="12" fill="#FFFFFF"/><rect x="42" y="62" width="74" height="24" rx="12" fill="#2A78D6"/><rect x="42" y="76" width="74" height="10" fill="#2A78D6"/>
<text x="79" y="80" text-anchor="middle" font-family="{FONT}" font-size="12" font-weight="700" fill="#FFFFFF" letter-spacing="1.5">MAR</text>
<text x="79" y="124" text-anchor="middle" font-family="{FONT}" font-size="34" font-weight="800" fill="#0F2A4A">14</text>
<circle cx="79" cy="113" r="22" fill="none" stroke="#F57FA0" stroke-width="3" stroke-dasharray="4 4" opacity=".9"/></g></g>
{spark(318, 78, 10)}{spark(345, 118, 6, cls="tw2")}{spark(112, 190, 7, "#FFFFFF", "tw2")}
''')

# 2. Gifts: wrapped gift with bow, tulip bouquet, floating hearts
HEART = "M0 4 C0 -1 7 -2 8 3 C9 -2 16 -1 16 4 C16 10 8 14 8 16 C8 14 0 10 0 4Z"
ART["gifts-flowers-and-hampers"] = svg("#EFE6FF", "#FFDDE8", f'''
<ellipse cx="200" cy="214" rx="120" ry="9" fill="#7B5CC9" opacity=".14"/>
<rect x="118" y="124" width="112" height="88" rx="8" fill="#8E7CF0"/>
<rect x="118" y="124" width="112" height="88" rx="8" fill="url(#bg)" opacity=".08"/>
<rect x="110" y="106" width="128" height="26" rx="7" fill="#A596F7"/>
<rect x="166" y="106" width="16" height="106" fill="#FFD166"/>
<rect x="110" y="114" width="128" height="10" fill="#FFD166" opacity=".0"/>
<path d="M174 106 C150 80 128 94 150 106Z" fill="#FFC23D"/><path d="M174 106 C198 80 220 94 198 106Z" fill="#FFC23D"/>
<circle cx="174" cy="105" r="7" fill="#FFB020"/>
<path d="M176 110 q10 18 2 34" stroke="#FFFFFF" stroke-width="1.5" fill="none" opacity=".8"/>
<g transform="translate(168 140) rotate(8)"><rect x="0" y="0" width="34" height="22" rx="4" fill="#FFFFFF"/><path transform="translate(9 3) scale(.95)" d="{HEART}" fill="#F25C82"/></g>
<g stroke="#2E9E63" stroke-width="4" stroke-linecap="round" fill="none"><path d="M296 200 C292 170 282 140 270 112"/><path d="M300 200 C302 168 304 140 306 100"/><path d="M304 200 C312 170 324 146 338 124"/></g>
<path d="M286 168 C268 160 262 146 266 136 C278 142 286 152 286 168Z" fill="#3CB371"/><path d="M312 170 C332 164 340 150 336 140 C324 146 314 156 312 170Z" fill="#3CB371"/>
<g class="fo"><path d="M256 112 C256 94 266 86 270 84 C274 86 284 94 284 112 C284 120 278 124 270 124 C262 124 256 120 256 112Z" fill="#F25C82"/><path d="M262 98 L270 108 L278 98" stroke="#FFFFFF" stroke-width="2" fill="none" opacity=".45"/></g>
<g class="fo2"><path d="M292 100 C292 82 302 74 306 72 C310 74 320 82 320 100 C320 108 314 112 306 112 C298 112 292 108 292 100Z" fill="#FF9F43"/><path d="M298 86 L306 96 L314 86" stroke="#FFFFFF" stroke-width="2" fill="none" opacity=".45"/></g>
<g class="fo"><path d="M324 124 C324 106 334 98 338 96 C342 98 352 106 352 124 C352 132 346 136 338 136 C330 136 324 132 324 124Z" fill="#E84A7F"/></g>
<path d="M278 192 L330 192 L318 214 L290 214Z" fill="#FFFFFF" opacity=".95"/><path d="M276 190 L332 190" stroke="#F2B8CB" stroke-width="5" stroke-linecap="round"/>
<g class="fo"><path transform="translate(70 70) scale(1.1)" d="{HEART}" fill="#F25C82"/></g>
<g class="fo2"><path transform="translate(96 46) scale(.7)" d="{HEART}" fill="#FF9FB8"/></g>
{spark(352, 60, 9)}{spark(60, 150, 7, cls="tw2")}
''')

# 3. Grocery: paper bag with greens, baguette and fruit, a weekly loop badge
ART["online-grocery"] = svg("#DDF5E8", "#C8EDDA", f'''
<ellipse cx="208" cy="216" rx="110" ry="8" fill="#1F7A4D" opacity=".14"/>
<g transform="rotate(-14 214 86)"><rect x="200" y="40" width="26" height="96" rx="13" fill="#E9B36A"/><path d="M206 56 l14 8 M206 74 l14 8 M206 92 l14 8" stroke="#C98B3E" stroke-width="3" stroke-linecap="round"/></g>
<g><ellipse cx="168" cy="94" rx="18" ry="26" fill="#2E9E63" transform="rotate(-20 168 94)"/><ellipse cx="186" cy="86" rx="16" ry="28" fill="#3CB371" transform="rotate(8 186 86)"/><path d="M168 118 L176 70 M186 112 L186 62" stroke="#1F7A4D" stroke-width="2" opacity=".5"/></g>
<g transform="rotate(24 250 92)"><path d="M244 66 L256 66 L250 124Z" fill="#FF8C42"/><path d="M250 66 l-8-14 M250 66 l0-16 M250 66 l8-14" stroke="#3CB371" stroke-width="4" stroke-linecap="round"/></g>
<path d="M138 108 L278 108 L266 210 L150 210Z" fill="#D9A86C"/>
<path d="M138 108 L278 108 L276 124 L140 124Z" fill="#C8945A"/>
<path d="M190 150 q18 -14 36 0" stroke="#B57E45" stroke-width="3" fill="none" stroke-linecap="round" opacity=".6"/>
<circle cx="298" cy="196" r="20" fill="#E5484D"/><path d="M298 178 q4-10 12-10" stroke="#3B7D3B" stroke-width="3" fill="none" stroke-linecap="round"/><ellipse cx="291" cy="190" rx="5" ry="7" fill="#FFFFFF" opacity=".35"/>
<circle cx="120" cy="200" r="15" fill="#FFB020"/><circle cx="116" cy="196" r="4" fill="#FFFFFF" opacity=".35"/>
<g class="fo"><circle cx="78" cy="78" r="34" fill="#FFFFFF"/><path d="M62 78 a16 16 0 1 1 6 12.5" stroke="#2A78D6" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M60 88 l8 4 l2-9" stroke="#2A78D6" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<text x="78" y="83" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="800" fill="#0F2A4A">7d</text></g>
{spark(336, 70, 10)}{spark(358, 120, 6, cls="tw2")}
''')

# 4. Beauty: amber serum with dropper, cream jar, tube, falling drop, refill badge
ART["beauty-and-skincare"] = svg("#FDE8EF", "#EFE4FF", f'''
<ellipse cx="205" cy="214" rx="118" ry="8" fill="#9A4C7A" opacity=".14"/>
<g transform="rotate(-12 124 168)"><rect x="104" y="112" width="40" height="96" rx="8" fill="#BFE3F7"/><rect x="104" y="112" width="40" height="18" rx="4" fill="#8CCBEE"/><rect x="112" y="98" width="24" height="16" rx="3" fill="#5BA8D8"/><rect x="112" y="146" width="24" height="30" rx="4" fill="#FFFFFF" opacity=".85"/></g>
<rect x="174" y="102" width="62" height="106" rx="16" fill="#F2A65A"/>
<rect x="180" y="110" width="10" height="84" rx="5" fill="#FFFFFF" opacity=".35"/>
<rect x="186" y="136" width="38" height="44" rx="6" fill="#FFF8F0"/>
<path d="M194 150 h22 M194 160 h16 M194 170 h20" stroke="#E6B98E" stroke-width="3" stroke-linecap="round"/>
<rect x="190" y="76" width="30" height="28" rx="6" fill="#3D3D5C"/>
<ellipse cx="205" cy="68" rx="13" ry="15" fill="#3D3D5C"/>
<ellipse cx="200" cy="64" rx="3" ry="5" fill="#FFFFFF" opacity=".3"/>
<path class="dr" d="M150 70 c-5 7-7 11-7 14 a7 7 0 0 0 14 0 c0-3-2-7-7-14Z" fill="#F2A65A"/>
<rect x="252" y="150" width="78" height="58" rx="14" fill="#FFFFFF"/>
<rect x="248" y="138" width="86" height="20" rx="8" fill="#F57FA0"/>
<rect x="266" y="168" width="50" height="22" rx="5" fill="#FDE8EF"/>
<g class="fo"><circle cx="316" cy="76" r="30" fill="#FFFFFF"/><path d="M302 76 a14 14 0 1 1 4 10" stroke="#9B5DE5" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M300 84 l6 4 l2-8" stroke="#9B5DE5" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></g>
{spark(80, 72, 10)}{spark(64, 112, 6, cls="tw2")}{spark(356, 150, 7, cls="tw2")}
''')

# 5. Fashion: clothing rail with three garments, crescent moon, shopping bag
ART["fashion-and-clothing"] = svg("#FFF2DC", "#FFE0C2", f'''
<ellipse cx="200" cy="216" rx="130" ry="8" fill="#9A5B2A" opacity=".14"/>
<path d="M92 54 H308" stroke="#5B4636" stroke-width="6" stroke-linecap="round"/>
<path d="M100 54 V210 M300 54 V210" stroke="#5B4636" stroke-width="6" stroke-linecap="round"/>
<path d="M84 212 h32 M284 212 h32" stroke="#5B4636" stroke-width="6" stroke-linecap="round"/>
<g fill="none" stroke="#7A6352" stroke-width="3" stroke-linecap="round"><path d="M150 54 q0 8 -6 10 l-22 12 h56 l-22-12"/><path d="M206 54 q0 8 -6 10 l-22 12 h56 l-22-12"/><path d="M262 54 q0 8 -6 10 l-22 12 h56 l-22-12"/></g>
<path d="M132 76 h36 l8 26 l12 92 h-76 l12-92Z" fill="#1F8A8A"/><path d="M138 100 h24" stroke="#FFFFFF" stroke-width="3" opacity=".5"/><path d="M150 108 v80" stroke="#176E6E" stroke-width="2" opacity=".5"/>
<path d="M182 76 h48 l14 22 l-10 8 l-6-8 v58 h-48 v-58 l-6 8 l-10-8Z" fill="#F29E4C"/><path d="M206 80 v76" stroke="#D9822F" stroke-width="2"/><circle cx="206" cy="98" r="2" fill="#FFFFFF"/><circle cx="206" cy="114" r="2" fill="#FFFFFF"/><circle cx="206" cy="130" r="2" fill="#FFFFFF"/>
<path d="M244 76 h36 l6 22 l4 108 h-56 l4-108Z" fill="#7B4FD1"/><path d="M248 96 h28" stroke="#FFD166" stroke-width="4"/><path d="M252 160 l8 8 l8-8 l8 8" stroke="#FFD166" stroke-width="2" fill="none" opacity=".8"/>
<g class="fo"><path d="M346 34 a24 24 0 1 0 18 40 a19 19 0 1 1 -18 -40Z" fill="#FFC24A"/>{spark(372, 46, 7, "#FFC24A")}</g>
<g transform="translate(318 140)"><path d="M10 18 q0-18 16-18 q16 0 16 18" stroke="#B83E5C" stroke-width="4" fill="none"/><rect x="0" y="16" width="52" height="58" rx="6" fill="#E85D75"/><rect x="0" y="16" width="52" height="12" rx="6" fill="#D44B64"/></g>
{spark(56, 100, 9)}{spark(40, 160, 6, cls="tw2")}
''')

# 6. Pet: food bag with paw label, bowl of kibble, bone treat, paw trail
PAW = '<ellipse cx="0" cy="6" rx="7" ry="6"/><circle cx="-8" cy="-3" r="3.2"/><circle cx="-3" cy="-8" r="3.2"/><circle cx="3" cy="-8" r="3.2"/><circle cx="8" cy="-3" r="3.2"/>'
ART["pet-food-and-supplies"] = svg("#FFF6D2", "#FFE5A8", f'''
<ellipse cx="210" cy="216" rx="120" ry="8" fill="#8A6A10" opacity=".16"/>
<path d="M124 72 l8-12 l8 12 l8-12 l8 12 l8-12 l8 12 l8-12 l8 12 l8-12 l8 12 l8-12 l8 12 V206 a8 8 0 0 1 -8 8 H132 a8 8 0 0 1 -8-8Z" fill="#3F78E6"/>
<rect x="124" y="72" width="104" height="18" fill="#2F63C8"/>
<circle cx="176" cy="142" r="32" fill="#FFFFFF"/>
<g transform="translate(176 142) scale(1.6)" fill="#3F78E6">{PAW}</g>
<rect x="146" y="186" width="60" height="10" rx="5" fill="#FFFFFF" opacity=".55"/>
<path d="M240 186 h96 l-8 26 h-80Z" fill="#E85D75"/><ellipse cx="288" cy="186" rx="48" ry="9" fill="#F07A8E"/>
<g fill="#A0612C"><circle cx="268" cy="182" r="6"/><circle cx="282" cy="179" r="6"/><circle cx="296" cy="181" r="6"/><circle cx="309" cy="183" r="5.5"/><circle cx="275" cy="186" r="5"/><circle cx="290" cy="187" r="5"/><circle cx="303" cy="188" r="5"/></g>
<g class="fo"><g transform="rotate(-20 300 110)"><rect x="276" y="104" width="48" height="12" rx="6" fill="#FFFFFF"/><circle cx="276" cy="104" r="8" fill="#FFFFFF"/><circle cx="276" cy="116" r="8" fill="#FFFFFF"/><circle cx="324" cy="104" r="8" fill="#FFFFFF"/><circle cx="324" cy="116" r="8" fill="#FFFFFF"/></g></g>
<g fill="#D9A520" opacity=".45"><g transform="translate(60 196) rotate(-20) scale(.8)">{PAW}</g><g transform="translate(84 168) rotate(-10) scale(.8)">{PAW}</g><g transform="translate(70 134) rotate(-25) scale(.8)">{PAW}</g></g>
{spark(352, 60, 10)}{spark(88, 70, 7, cls="tw2")}
''')

# 7. Restaurants: noodle bowl with chopsticks and steam, takeaway bag, location pin
ART["restaurants-and-cloud-kitchens"] = svg("#FFE6D6", "#FFD0B8", f'''
<ellipse cx="208" cy="216" rx="122" ry="8" fill="#A0461E" opacity=".15"/>
<g stroke="#FFFFFF" stroke-width="4" fill="none" stroke-linecap="round" opacity=".9"><path class="st" d="M188 92 q-8-10 0-20 q8-10 0-20"/><path class="st2" d="M214 88 q-8-10 0-20 q8-10 0-20"/><path class="st" d="M240 92 q-8-10 0-20 q8-10 0-20"/></g>
<path d="M248 70 L300 120" stroke="#8B5A3C" stroke-width="5" stroke-linecap="round"/><path d="M262 64 L306 122" stroke="#A86B45" stroke-width="5" stroke-linecap="round"/>
<path d="M150 124 h128 a64 64 0 0 1 -128 0Z" fill="#FFFFFF"/>
<path d="M156 140 h116" stroke="#2A78D6" stroke-width="4" stroke-dasharray="8 6"/>
<ellipse cx="214" cy="124" rx="64" ry="12" fill="#F7C873"/>
<path d="M164 122 q8 -8 16 0 t16 0 t16 0 t16 0 t16 0 t16 0" stroke="#E8A93E" stroke-width="3" fill="none"/>
<circle cx="190" cy="120" r="7" fill="#3CB371"/><circle cx="238" cy="119" r="6" fill="#E5484D"/><ellipse cx="214" cy="117" rx="9" ry="5" fill="#FFFFFF"/><ellipse cx="214" cy="117" rx="4" ry="3" fill="#FFB020"/>
<rect x="196" y="186" width="36" height="14" rx="4" fill="#FFFFFF"/>
<path d="M66 110 L118 110 L124 210 L60 210Z" fill="#D9A86C"/><path d="M66 110 L118 110 L116 124 L68 124Z" fill="#C8945A"/>
<circle cx="92" cy="164" r="17" fill="#FFFFFF"/><path d="M84 164 h16 M92 156 v16" stroke="#E85D75" stroke-width="4" stroke-linecap="round" opacity="0"/>
<text x="92" y="169" text-anchor="middle" font-family="{FONT}" font-size="13" font-weight="800" fill="#E85D75">8pm</text>
<g class="fo"><path d="M336 30 a24 24 0 0 1 24 24 c0 18 -24 42 -24 42 s-24 -24 -24 -42 a24 24 0 0 1 24 -24Z" fill="#E85D75"/><circle cx="336" cy="54" r="9" fill="#FFFFFF"/></g>
{spark(316, 150, 9)}{spark(352, 182, 6, cls="tw2")}
''')

# 8. Coffee and tea: latte with heart, steam, coffee bag, beans and a tea leaf
BEAN = '<ellipse cx="0" cy="0" rx="7" ry="10"/><path d="M0 -9 q-4 9 0 18" stroke="#3B2416" stroke-width="1.6" fill="none"/>'
ART["coffee-tea-and-specialty-food"] = svg("#F6EEE4", "#EAD7C2", f'''
<ellipse cx="200" cy="216" rx="124" ry="8" fill="#6B4226" opacity=".16"/>
<g stroke="#FFFFFF" stroke-width="4" fill="none" stroke-linecap="round"><path class="st" d="M160 84 q-8-10 0-20 q8-10 0-20"/><path class="st2" d="M186 80 q-8-10 0-20 q8-10 0-20"/></g>
<ellipse cx="172" cy="204" rx="78" ry="12" fill="#FFFFFF"/>
<path d="M112 110 h120 l-10 78 a16 16 0 0 1 -16 14 h-68 a16 16 0 0 1 -16 -14Z" fill="#FFFFFF"/>
<path d="M230 126 a24 24 0 0 1 0 48" stroke="#FFFFFF" stroke-width="10" fill="none"/>
<ellipse cx="172" cy="112" rx="58" ry="12" fill="#C69C6D"/>
<path d="M172 120 C160 112 158 104 166 103 C170 102 172 106 172 108 C172 106 174 102 178 103 C186 104 184 112 172 120Z" fill="#F6E6D3"/>
<path d="M118 140 h108" stroke="#2A78D6" stroke-width="5" opacity=".9"/>
<path d="M270 70 l60 0 l8 140 l-76 0Z" fill="#3B2A20"/>
<path d="M270 70 l60 0 l2 14 l-64 0Z" fill="#2A1D16"/>
<rect x="280" y="112" width="46" height="54" rx="6" fill="#F2A65A"/>
<g transform="translate(303 132)" fill="#3B2A20">{BEAN}</g>
<path d="M286 152 h34" stroke="#3B2A20" stroke-width="3" stroke-linecap="round" opacity=".7"/>
<g fill="#6B4226"><g transform="translate(96 200) rotate(30)">{BEAN}</g><g transform="translate(250 212) rotate(-40)">{BEAN}</g><g transform="translate(70 180) rotate(60) scale(.8)">{BEAN}</g></g>
<g class="fo"><path d="M70 72 C70 48 96 38 112 40 C112 64 92 80 70 72Z" fill="#3CB371"/><path d="M72 70 C82 60 94 52 108 44" stroke="#1F7A4D" stroke-width="2" fill="none"/></g>
{spark(356, 52, 9)}{spark(48, 120, 6, cls="tw2")}
''')

# 9. Baby and kids: bottle, ABC blocks, balloon, clouds
ART["baby-and-kids"] = svg("#E1F0FD", "#E6E6FA", f'''
<ellipse cx="206" cy="216" rx="124" ry="8" fill="#3A5A8C" opacity=".14"/>
<g fill="#FFFFFF" opacity=".9"><ellipse cx="74" cy="64" rx="30" ry="14"/><ellipse cx="96" cy="56" rx="22" ry="16"/><ellipse cx="300" cy="44" rx="26" ry="11"/><ellipse cx="318" cy="38" rx="18" ry="13"/></g>
<path d="M150 64 q6-20 12 0Z" fill="#FFCC80"/>
<rect x="140" y="64" width="34" height="18" rx="5" fill="#FFB74D"/>
<rect x="134" y="80" width="46" height="128" rx="16" fill="#FFFFFF"/>
<rect x="134" y="132" width="46" height="76" rx="0" fill="#FFF3E0"/><rect x="134" y="184" width="46" height="24" rx="12" fill="#FFF3E0"/>
<path d="M140 104 h12 M140 120 h8 M140 136 h12 M140 152 h8 M140 168 h12" stroke="#90A4D4" stroke-width="2.5" stroke-linecap="round"/>
<rect x="210" y="160" width="48" height="48" rx="8" fill="#FF8A80"/><text x="234" y="194" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="800" fill="#FFFFFF">A</text>
<rect x="262" y="160" width="48" height="48" rx="8" fill="#64B5F6"/><text x="286" y="194" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="800" fill="#FFFFFF">B</text>
<g transform="rotate(-6 260 136)"><rect x="236" y="110" width="48" height="48" rx="8" fill="#81C784"/><text x="260" y="144" text-anchor="middle" font-family="{FONT}" font-size="28" font-weight="800" fill="#FFFFFF">C</text></g>
<g class="fo"><ellipse cx="344" cy="104" rx="24" ry="29" fill="#FFD166"/><ellipse cx="336" cy="94" rx="6" ry="9" fill="#FFFFFF" opacity=".45"/><path d="M340 132 l8 0 l-4 6Z" fill="#F0B83C"/><path d="M344 138 q-10 20 4 40 q10 16 -2 32" stroke="#8C9EC9" stroke-width="2" fill="none"/></g>
{spark(108, 132, 9)}{spark(92, 176, 6, cls="tw2")}{spark(210, 70, 7, cls="tw2")}
''')

# 10. Corporate and B2B: office tower, people linked to it, gift hamper
PERSON = '<circle cx="0" cy="0" r="17" fill="#FFFFFF"/><circle cx="0" cy="-4" r="6" fill="{c}"/><path d="M-10 11 a10 9 0 0 1 20 0" fill="{c}"/>'
ART["corporate-gifting-and-b2b"] = svg("#E3ECFB", "#ECE7FE", f'''
<ellipse cx="200" cy="216" rx="130" ry="8" fill="#1D3B66" opacity=".14"/>
<g stroke="#9DB7E6" stroke-width="2.5" stroke-dasharray="5 5" fill="none"><path d="M76 74 L156 110"/><path d="M60 150 L156 150"/><path d="M84 202 L156 186"/><path d="M332 56 L248 96"/><path d="M350 128 L248 132"/></g>
<rect x="156" y="52" width="92" height="160" rx="8" fill="#1D3B66"/>
<rect x="156" y="52" width="92" height="16" rx="8" fill="#2A4E85"/>
<g fill="#4D7CC7">
<rect x="170" y="80" width="16" height="14" rx="2"/><rect x="194" y="80" width="16" height="14" rx="2" fill="#FFD166"/><rect x="218" y="80" width="16" height="14" rx="2"/>
<rect x="170" y="104" width="16" height="14" rx="2" fill="#FFD166"/><rect x="194" y="104" width="16" height="14" rx="2"/><rect x="218" y="104" width="16" height="14" rx="2"/>
<rect x="170" y="128" width="16" height="14" rx="2"/><rect x="194" y="128" width="16" height="14" rx="2"/><rect x="218" y="128" width="16" height="14" rx="2" fill="#FFD166"/>
<rect x="170" y="152" width="16" height="14" rx="2"/><rect x="194" y="152" width="16" height="14" rx="2" fill="#FFD166"/><rect x="218" y="152" width="16" height="14" rx="2"/></g>
<rect x="190" y="182" width="24" height="30" rx="3" fill="#FFFFFF" opacity=".85"/>
<g class="fo"><g transform="translate(68 70)">{PERSON.format(c="#F57FA0")}</g></g>
<g class="fo2"><g transform="translate(48 150)">{PERSON.format(c="#3CB371")}</g></g>
<g class="fo"><g transform="translate(76 204)">{PERSON.format(c="#FF9F43")}</g></g>
<g class="fo2"><g transform="translate(338 52)">{PERSON.format(c="#9B5DE5")}</g></g>
<g class="fo"><g transform="translate(356 128)">{PERSON.format(c="#2A78D6")}</g></g>
<path d="M266 176 h76 l-8 36 h-60Z" fill="#C8945A"/>
<path d="M270 186 h68 M272 196 h64 M274 206 h60" stroke="#A9773F" stroke-width="2"/>
<path d="M272 176 q32 -40 64 0" stroke="#A9773F" stroke-width="4" fill="none"/>
<rect x="284" y="148" width="12" height="30" rx="3" fill="#7B4FD1"/><rect x="286" y="142" width="8" height="8" rx="2" fill="#5E3BAE"/>
<circle cx="314" cy="168" r="11" fill="#E5484D"/><rect x="322" y="156" width="14" height="22" rx="3" fill="#FFD166"/>
{spark(130, 36, 8)}{spark(296, 110, 6, cls="tw2")}
''')


# Little Loyalbase pop-ups shown over each picture: (title, detail, dot colour)
CHIPS = {
    "bakeries-and-cake-shops": ("Birthday in 12 days", "Anna P. · ordered 14 Mar last year", "#F57FA0"),
    "gifts-flowers-and-hampers": ("Last Valentine's buyer", "Daniel R. · not back since · $85", "#8E7CF0"),
    "online-grocery": ("Missed the weekly shop", "Fatima R. · 34 days, usually 7", "#E5A100"),
    "beauty-and-skincare": ("Refill due", "Vitamin C serum · every 9 weeks", "#9B5DE5"),
    "fashion-and-clothing": ("Eid regular, 3 years", "Aisha N. · send the new collection", "#1F8A8A"),
    "pet-food-and-supplies": ("Due in 2 days", "Omar K. · Adult dry food 10kg", "#3F78E6"),
    "restaurants-and-cloud-kitchens": ("Friday regular went quiet", "Kasun P. · last order 4 weeks ago", "#E85D75"),
    "coffee-tea-and-specialty-food": ("Tasting set, no full bag", "44% of these came back", "#A0612C"),
    "baby-and-kids": ("Next size up?", "Sofia L. · last nappies 52 days ago", "#64B5F6"),
    "corporate-gifting-and-b2b": ("5 people, 1 company", "Ordered 40 hampers last December", "#1D3B66"),
}

ALT = {
    "bakeries-and-cake-shops": "Illustration of a birthday cake with candles next to a calendar page marked 14 March",
    "gifts-flowers-and-hampers": "Illustration of a wrapped gift with a bow beside a bouquet of tulips",
    "online-grocery": "Illustration of a grocery bag with greens, bread and fruit, and a weekly repeat badge",
    "beauty-and-skincare": "Illustration of a skincare serum bottle with dropper, a cream jar and a tube",
    "fashion-and-clothing": "Illustration of a clothing rail with three garments, a shopping bag and a crescent moon",
    "pet-food-and-supplies": "Illustration of a bag of pet food with a paw print, a bowl of kibble and a bone treat",
    "restaurants-and-cloud-kitchens": "Illustration of a steaming noodle bowl with chopsticks, a takeaway bag and a map pin",
    "coffee-tea-and-specialty-food": "Illustration of a latte with heart art beside a bag of coffee beans and a tea leaf",
    "baby-and-kids": "Illustration of a baby bottle, A B C blocks and a balloon",
    "corporate-gifting-and-b2b": "Illustration of an office building linked to five people, with a gift hamper",
}


def write_all(root):
    out = os.path.join(root, "assets", "ind")
    os.makedirs(out, exist_ok=True)
    for slug, s in ART.items():
        with open(os.path.join(out, f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(s.strip() + "\n")
    return out


def figure(slug, cls="sx-art", eager=False):
    """Picture plus its Loyalbase pop-up, for cards and page headers."""
    title, detail, dot = CHIPS[slug]
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<div class="{cls}"><img src="/assets/ind/{slug}.svg" width="400" height="240" alt="{ALT[slug]}" {loading} decoding="async">'
            f'<div class="sx-chip" aria-hidden="true"><i style="background: {dot}"></i><span><b>{title}</b><small>{detail}</small></span></div></div>')


if __name__ == "__main__":
    print(write_all(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
