"""Security-console styling: dark bento tiles, risk gauge, and widget theming."""
import streamlit as st

GAUGE_LEN = 251.33  # length of the half-circle arc (pi * 80)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@400;500;600;700;800&display=swap');

:root {
  --bg: #0a1017;
  --panel: #111a24;
  --panel-2: #16212e;
  --line: #223245;
  --ink: #e8eef6;
  --soft: #93a3b8;
  --info: #7aa7ff;
  --safe: #46d6b8;
  --risk: #ff5470;
}

html, body, [class*="css"], .stApp {
  font-family: 'Sora', -apple-system, 'Segoe UI', system-ui, sans-serif;
  color: var(--ink);
}
.stApp {
  background-color: var(--bg);
  background-image:
    linear-gradient(to right, rgba(255,255,255,0.028) 1px, transparent 1px),
    linear-gradient(to bottom, rgba(255,255,255,0.028) 1px, transparent 1px),
    radial-gradient(60rem 30rem at 50% -12%, rgba(122,167,255,0.14), transparent 65%);
  background-size: 44px 44px, 44px 44px, auto;
  background-attachment: fixed;
}
header[data-testid="stHeader"] { background: transparent; }
header[data-testid="stHeader"] *, [data-testid="stSidebarCollapseButton"] *, [data-testid="collapsedControl"] * { color: var(--ink) !important; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 2.6rem; padding-bottom: 4rem; max-width: 1200px; }

/* ---------- sidebar ---------- */
section[data-testid="stSidebar"] { background: var(--panel); border-right: 1px solid var(--line); }
section[data-testid="stSidebar"] * { color: var(--ink) !important; }
section[data-testid="stSidebar"] a { border-radius: 10px; }
section[data-testid="stSidebar"] a:hover { background: var(--panel-2); }
section[data-testid="stSidebar"] a[aria-current="page"] { background: var(--panel-2); box-shadow: inset 3px 0 0 var(--info); }

/* ---------- bento grid ---------- */
.bento { display: grid; grid-template-columns: repeat(12, 1fr); gap: 1.1rem; margin-bottom: 1.1rem; }
.t {
  grid-column: span 12; min-width: 0;
  background: var(--panel); border: 1px solid var(--line); border-radius: 18px;
  padding: 1.6rem 1.7rem;
}
.s3 { grid-column: span 3; } .s4 { grid-column: span 4; } .s5 { grid-column: span 5; }
.s6 { grid-column: span 6; } .s7 { grid-column: span 7; } .s8 { grid-column: span 8; }
@media (max-width: 1000px) { .s3 { grid-column: span 6; } .s4, .s5, .s6, .s7, .s8 { grid-column: span 12; } }
@media (max-width: 640px)  { .s3 { grid-column: span 12; } }

.t h3 { font-size: 1.08rem; font-weight: 700; letter-spacing: -0.01em; margin: 0 0 0.9rem; color: var(--ink); }
.t p { font-size: 0.95rem; line-height: 1.7; color: var(--soft); margin: 0 0 0.6rem; }
.t p:last-child { margin-bottom: 0; }
.t ul { margin: 0; padding-left: 1.15rem; }
.t li { font-size: 0.95rem; line-height: 1.75; color: var(--soft); }
.t b { color: var(--ink); font-weight: 700; }
.t code { font-size: 0.86em; padding: 0.1em 0.45em; border-radius: 6px; background: var(--panel-2); border: 1px solid var(--line); color: var(--ink); }

/* ---------- headers ---------- */
.hero { padding: 2.6rem 2.8rem; display: flex; flex-direction: column; justify-content: center; }
.hero h1 {
  font-size: clamp(2.2rem, 4.6vw, 3.6rem) !important; font-weight: 800 !important;
  letter-spacing: -0.04em; line-height: 1.05 !important;
  margin: 1.1rem 0 0.7rem !important; padding: 0 !important; color: var(--ink) !important;
}
.hero .sub { font-size: 1.1rem; font-weight: 600; color: var(--info); margin: 0 0 0.7rem; }
.hero p.lede { max-width: 52ch; }
.pill {
  align-self: flex-start; display: inline-flex; align-items: center; gap: 0.6rem;
  padding: 0.4rem 0.9rem; border-radius: 999px; font-size: 0.85rem; font-weight: 600;
  background: var(--panel-2); border: 1px solid var(--line); color: var(--ink);
}
.pill i { width: 8px; height: 8px; border-radius: 50%; background: var(--safe); box-shadow: 0 0 0 4px rgba(70,214,184,0.2); }

.page-head h1 {
  font-size: clamp(1.8rem, 3.6vw, 2.5rem) !important; font-weight: 800 !important;
  letter-spacing: -0.035em; line-height: 1.1 !important; margin: 0 !important; padding: 0 !important; color: var(--ink) !important;
}
.page-head p { margin: 0.6rem 0 0; max-width: 62ch; }

/* ---------- metric tiles ---------- */
.m .label { font-size: 0.9rem; font-weight: 600; color: var(--soft); margin: 0 0 0.6rem; }
.m .value { font-size: 2.3rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; margin: 0; color: var(--ink); }
.m .value.sm { font-size: 1.45rem; line-height: 1.4; }
.m .sub { font-size: 0.88rem; color: var(--soft); margin: 0.45rem 0 0; }
.m.risk .value { color: var(--risk); } .m.safe .value { color: var(--safe); } .m.info .value { color: var(--info); }
.meter { height: 6px; border-radius: 999px; background: var(--panel-2); margin-top: 1.1rem; overflow: hidden; }
.meter > div { height: 100%; border-radius: 999px; background: var(--info); }
.m.risk .meter > div { background: var(--risk); } .m.safe .meter > div { background: var(--safe); }

/* ---------- gauge ---------- */
.gauge-box { text-align: center; }
.gauge { width: 100%; max-width: 300px; height: auto; display: block; margin: 0 auto; }
.gauge text { fill: var(--soft); font-size: 9px; font-family: 'Sora', sans-serif; }
.needle { transform-origin: 100px 100px; transform: rotate(var(--a)); animation: sweep 1.3s cubic-bezier(.2,.9,.2,1) both; }
.garc { animation: gfill 1.3s cubic-bezier(.2,.9,.2,1) both; }
.gauge-val { font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1; margin-top: -0.2rem; }
.gauge-val.risk { color: var(--risk); } .gauge-val.safe { color: var(--safe); } .gauge-val.info { color: var(--info); }
.gauge-cap { font-size: 0.9rem; color: var(--soft); margin-top: 0.45rem; }
@keyframes sweep { from { transform: rotate(-90deg); } }
@keyframes gfill { from { stroke-dashoffset: 251.33; } }

/* ---------- bars, chips, mini stats ---------- */
.hbar { margin: 0 0 1.2rem; }
.hbar .top { display: flex; justify-content: space-between; font-size: 0.92rem; margin-bottom: 0.5rem; color: var(--soft); }
.hbar .top b { color: var(--ink); }
.hbar .track { height: 12px; border-radius: 999px; background: var(--panel-2); overflow: hidden; }
.hbar .fill { height: 100%; border-radius: 999px; min-width: 5px; }
.fill.safe { background: var(--safe); } .fill.risk { background: var(--risk); } .fill.info { background: var(--info); }

.chips { display: flex; flex-wrap: wrap; gap: 0.55rem; }
.chip { padding: 0.45rem 0.95rem; border-radius: 999px; font-size: 0.88rem; font-weight: 600; background: var(--panel-2); border: 1px solid var(--line); color: var(--ink); }
.chip.risk { border-color: rgba(255,84,112,0.55); color: #ff9aab; background: rgba(255,84,112,0.08); }
.chip.safe { border-color: rgba(70,214,184,0.55); color: var(--safe); background: rgba(70,214,184,0.08); }

.mini { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin: 0 0 1.1rem; }
.mini div { padding: 0.9rem 1rem; border-radius: 12px; background: var(--panel-2); border: 1px solid var(--line); }
.mini b { display: block; font-size: 1.5rem; font-weight: 800; letter-spacing: -0.02em; }
.mini span { font-size: 0.84rem; color: var(--soft); }

/* ---------- workflow: one straight line ---------- */
.flow { position: relative; display: grid; grid-template-columns: repeat(8, 1fr); gap: 0.6rem; }
.flow::before { content: ""; position: absolute; top: 15px; left: 6.25%; right: 6.25%; height: 2px; background: var(--line); }
.step { position: relative; text-align: center; padding: 0 0.3rem; }
.step .n {
  position: relative; width: 32px; height: 32px; margin: 0 auto 0.8rem; border-radius: 50%;
  display: grid; place-items: center; font-size: 0.82rem; font-weight: 700;
  background: var(--panel); border: 2px solid var(--line); color: var(--soft);
}
.step .name { font-size: 0.86rem; font-weight: 600; line-height: 1.35; color: var(--ink); }
.step.last .n { background: var(--safe); border-color: var(--safe); color: #06231d; }
@media (max-width: 1000px) {
  .flow { grid-template-columns: repeat(4, 1fr); row-gap: 1.6rem; }
  .flow::before { display: none; }
}
@media (max-width: 560px) { .flow { grid-template-columns: repeat(2, 1fr); } }

/* ---------- verdict ---------- */
.verdict h2 { font-size: 1.7rem; font-weight: 800; letter-spacing: -0.025em; margin: 0 0 1rem; line-height: 1.2; }
.verdict.risk h2 { color: var(--risk); } .verdict.safe h2 { color: var(--safe); }
.verdict .stats { display: grid; grid-template-columns: 1fr 1fr; gap: 0.8rem; margin-bottom: 1.2rem; }
.verdict .stats div { padding: 0.9rem 1rem; border-radius: 12px; background: var(--panel-2); border: 1px solid var(--line); }
.verdict .stats b { display: block; font-size: 1.4rem; font-weight: 800; }
.verdict .stats span { font-size: 0.84rem; color: var(--soft); }
.verdict h4 { font-size: 0.95rem; font-weight: 700; margin: 0 0 0.7rem; color: var(--ink); }
.verdict .fine { font-size: 0.84rem; margin-top: 1rem; }

/* ---------- native widgets ---------- */
[data-testid="stForm"] { background: var(--panel); border: 1px solid var(--line); border-radius: 18px; padding: 1.7rem 1.8rem 1.9rem; }
[data-testid="stWidgetLabel"] p, .stApp label p { color: var(--soft) !important; font-weight: 600; font-size: 0.9rem; }
[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"], [data-baseweb="select"] > div {
  background: #0d151e !important; border: 1px solid var(--line) !important; border-radius: 12px !important;
}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within, [data-baseweb="select"]:focus-within > div {
  border-color: var(--info) !important; box-shadow: 0 0 0 3px rgba(122,167,255,0.25) !important;
}
.stApp input, .stApp textarea, [data-baseweb="select"] * { color: var(--ink) !important; -webkit-text-fill-color: var(--ink); }
.stApp input::placeholder, .stApp textarea::placeholder { color: rgba(147,163,184,0.6) !important; -webkit-text-fill-color: rgba(147,163,184,0.6); }
[data-baseweb="popover"] > div, ul[role="listbox"] { background: var(--panel-2) !important; border: 1px solid var(--line); border-radius: 12px !important; }
ul[role="listbox"] li { color: var(--ink) !important; }
ul[role="listbox"] li:hover, ul[role="listbox"] li[aria-selected="true"] { background: rgba(122,167,255,0.22) !important; }
[data-testid="stFormSubmitButton"] > button, .stButton > button {
  background: var(--info); color: #07111f !important; border: none; border-radius: 12px;
  padding: 0.8rem 1.6rem; font-weight: 700; font-size: 1rem;
}
[data-testid="stFormSubmitButton"] > button p, .stButton > button p { color: #07111f !important; font-weight: 700; }
[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover { background: #9ab9ff; color: #07111f; }
[data-testid="stAlert"] { background: var(--panel); border: 1px solid var(--line); border-radius: 14px; color: var(--ink); }

@media (prefers-reduced-motion: reduce) { .needle, .garc { animation: none; } }
</style>
"""


def inject() -> None:
    st.markdown(CSS, unsafe_allow_html=True)


def html(*parts: str) -> str:
    """Join HTML flush-left so Markdown never treats it as a code block."""
    return "".join(p.strip() for p in parts)


def render(*parts: str) -> None:
    st.markdown(html(*parts), unsafe_allow_html=True)


def bento(*tiles: str) -> str:
    return f'<div class="bento">{"".join(tiles)}</div>'


def tile(inner: str, span: str = "", extra: str = "") -> str:
    return f'<div class="t {span} {extra}">{inner}</div>'


def page_header(title: str, subtitle: str = "") -> None:
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    render(bento(tile(f"<h1>{title}</h1>{sub}", "", "page-head")))


def metric(label, value, sub="", tone="", span="s3", pct=None, small=False) -> str:
    meter = f'<div class="meter"><div style="width:{max(pct, 2):.2f}%"></div></div>' if pct is not None else ""
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    size = " sm" if small else ""
    return tile(
        f'<p class="label">{label}</p><p class="value{size}">{value}</p>{sub_html}{meter}',
        span, f"m {tone}",
    )


def chips(items, tone="") -> str:
    return '<div class="chips">' + "".join(f'<span class="chip {tone}">{i}</span>' for i in items) + "</div>"


def hbar(label, shown, pct, tone) -> str:
    return (
        f'<div class="hbar"><div class="top"><span>{label}</span><b>{shown}</b></div>'
        f'<div class="track"><div class="fill {tone}" style="width:{max(pct, 0):.2f}%"></div></div></div>'
    )


def gauge(value: float, tone: str = "info", big: str = "", caption: str = "") -> str:
    """Half-circle gauge, 0-100. tone: info | safe | risk."""
    v = max(0.0, min(100.0, value))
    offset = GAUGE_LEN * (1 - v / 100)
    angle = -90 + v * 1.8
    big_html = f'<div class="gauge-val {tone}">{big}</div>' if big else ""
    cap_html = f'<div class="gauge-cap">{caption}</div>' if caption else ""
    return html(
        '<div class="gauge-box">',
        f'<svg class="gauge" viewBox="0 0 200 118" role="img" aria-label="Gauge showing {v:.1f} percent">',
        '<path d="M20 100 A80 80 0 0 1 180 100" fill="none" stroke="var(--line)" stroke-width="14" stroke-linecap="round"/>',
        f'<path class="garc" d="M20 100 A80 80 0 0 1 180 100" fill="none" stroke="var(--{tone})" stroke-width="14" '
        f'stroke-linecap="round" stroke-dasharray="{GAUGE_LEN}" style="stroke-dashoffset:{offset:.2f}"/>',
        f'<g class="needle" style="--a:{angle:.1f}deg">',
        '<line x1="100" y1="100" x2="100" y2="36" stroke="var(--ink)" stroke-width="3" stroke-linecap="round"/>',
        '<circle cx="100" cy="100" r="7" fill="var(--panel)" stroke="var(--ink)" stroke-width="3"/></g>',
        '<text x="20" y="116" text-anchor="middle">0</text>',
        '<text x="100" y="9" text-anchor="middle">50</text>',
        '<text x="180" y="116" text-anchor="middle">100</text>',
        "</svg>",
        big_html, cap_html, "</div>",
    )
