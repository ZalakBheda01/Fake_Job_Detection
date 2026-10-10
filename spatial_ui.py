"""Shared spatial (glass + depth) styling for every page of the Fake Job Detector."""
import streamlit as st

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

:root {
  --ink: #f3f5ff;
  --ink-soft: rgba(243, 245, 255, 0.70);
  --glass: rgba(255, 255, 255, 0.09);
  --glass-strong: rgba(255, 255, 255, 0.15);
  --edge: rgba(255, 255, 255, 0.22);
  --edge-top: rgba(255, 255, 255, 0.45);
  --legit: #5eead4;
  --fraud: #ff8a7a;
  --accent: #8ea2ff;
}

html, body, [class*="css"], .stApp {
  font-family: 'Plus Jakarta Sans', -apple-system, 'Segoe UI', system-ui, sans-serif;
  color: var(--ink);
}
.stApp {
  background:
    radial-gradient(60rem 40rem at 12% -10%, rgba(110, 120, 255, 0.55), transparent 60%),
    radial-gradient(50rem 36rem at 95% 8%, rgba(45, 212, 191, 0.32), transparent 60%),
    radial-gradient(48rem 40rem at 70% 105%, rgba(255, 138, 122, 0.30), transparent 60%),
    linear-gradient(160deg, #0d1030 0%, #151a45 50%, #0b1130 100%);
  background-attachment: fixed;
}
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }
.block-container { padding-top: 2.5rem; padding-bottom: 4rem; max-width: 1180px; }
.stApp p, .stApp li, .stApp label, .stApp span { color: inherit; }

/* ---------- sidebar ---------- */
section[data-testid="stSidebar"] {
  background: rgba(20, 24, 66, 0.55);
  backdrop-filter: blur(28px) saturate(160%);
  -webkit-backdrop-filter: blur(28px) saturate(160%);
  border-right: 1px solid var(--edge);
}
section[data-testid="stSidebar"] * { color: var(--ink); }
section[data-testid="stSidebar"] a { border-radius: 14px; }
section[data-testid="stSidebar"] a:hover { background: var(--glass-strong); }
section[data-testid="stSidebar"] a[aria-current="page"] { background: var(--glass-strong); }

/* ---------- glass material ---------- */
.glass {
  position: relative;
  background: linear-gradient(145deg, var(--glass-strong), var(--glass));
  backdrop-filter: blur(26px) saturate(170%);
  -webkit-backdrop-filter: blur(26px) saturate(170%);
  border: 1px solid var(--edge);
  border-top-color: var(--edge-top);
  border-radius: 32px;
  box-shadow:
    0 1px 0 rgba(255, 255, 255, 0.25) inset,
    0 30px 60px -20px rgba(4, 6, 30, 0.65),
    0 8px 20px -8px rgba(4, 6, 30, 0.45);
}
.scene { perspective: 1400px; }

/* ---------- page header (sub-pages) ---------- */
.page-head { padding: 2rem 2.4rem 1.8rem; margin-bottom: 1.6rem; border-radius: 30px; }
.page-head h1 {
  font-size: clamp(1.9rem, 4vw, 2.7rem); font-weight: 800;
  letter-spacing: -0.03em; line-height: 1.1; margin: 0; color: var(--ink);
}
.page-head p { margin: 0.6rem 0 0; font-size: 1rem; line-height: 1.6; color: var(--ink-soft); max-width: 62ch; }

/* ---------- home hero ---------- */
.hero {
  padding: 3rem 3.2rem 2.8rem;
  transform: rotateX(2.5deg); transform-origin: 50% 100%;
  animation: settle 1.1s cubic-bezier(.2,.8,.2,1) both;
}
.hero h1 {
  font-size: clamp(2.4rem, 5.4vw, 4.1rem); font-weight: 800;
  letter-spacing: -0.035em; line-height: 1.02; margin: 0 0 0.9rem; color: var(--ink);
}
.hero .sub { font-size: 1.15rem; font-weight: 600; color: var(--accent); margin: 0 0 0.6rem; }
.hero p.lede { max-width: 56ch; font-size: 1.02rem; line-height: 1.65; color: var(--ink-soft); margin: 0; }
.hero .orb {
  position: absolute; right: 3rem; top: 50%;
  width: 190px; height: 190px; border-radius: 50%; transform: translateY(-50%);
  background:
    radial-gradient(circle at 32% 28%, rgba(255,255,255,0.85), rgba(255,255,255,0) 32%),
    radial-gradient(circle at 60% 65%, rgba(94,234,212,0.75), rgba(142,162,255,0.55) 55%, rgba(255,138,122,0.55) 100%);
  box-shadow: 0 40px 60px -20px rgba(4,6,30,0.7), inset 0 -12px 30px rgba(255,255,255,0.18);
  animation: hover 7s ease-in-out infinite;
}
@media (max-width: 860px) { .hero .orb { display: none; } .hero { padding: 2rem 1.6rem; } }

/* ---------- note ---------- */
.note {
  display: flex; gap: 1rem; align-items: center;
  padding: 1.1rem 1.5rem; border-radius: 22px;
  background: linear-gradient(145deg, rgba(142,162,255,0.28), rgba(142,162,255,0.12));
}
.note.float { margin: -1.1rem 2.4rem 0 2.4rem; transform: translateZ(60px); z-index: 3; }
.note .dot {
  flex: none; width: 12px; height: 12px; border-radius: 50%;
  background: var(--accent); box-shadow: 0 0 0 6px rgba(142,162,255,0.25);
}
.note span { font-size: 0.98rem; line-height: 1.5; color: var(--ink); }
@media (max-width: 860px) { .note.float { margin: 1rem 0 0; } }

/* ---------- metrics ---------- */
.metrics { display: grid; grid-template-columns: repeat(3, 1fr); gap: 1.4rem; margin-top: 1.6rem; }
.metrics.cols-4 { grid-template-columns: repeat(4, 1fr); gap: 1.2rem; }
@media (max-width: 960px) { .metrics.cols-4 { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 760px) { .metrics, .metrics.cols-4 { grid-template-columns: 1fr; } }
.metric { padding: 1.6rem 1.7rem 1.5rem; border-radius: 28px; }
.metric .label { font-size: 0.95rem; font-weight: 600; color: var(--ink-soft); margin: 0 0 0.5rem; }
.metric .value { font-size: 2.3rem; font-weight: 800; letter-spacing: -0.03em; line-height: 1.1; margin: 0; }
.metric .value.sm { font-size: 1.55rem; line-height: 1.35; }
.metric .share { font-size: 0.9rem; color: var(--ink-soft); margin: 0.5rem 0 0; }
.metric.fraud .value { color: var(--fraud); }
.metric.legit .value { color: var(--legit); }
.metric .glow {
  position: absolute; inset: auto 1.4rem -1px 1.4rem; height: 2px; border-radius: 2px;
  background: linear-gradient(90deg, transparent, var(--accent), transparent); opacity: 0.8;
}
.metric.fraud .glow { background: linear-gradient(90deg, transparent, var(--fraud), transparent); }
.metric.legit .glow { background: linear-gradient(90deg, transparent, var(--legit), transparent); }

/* ---------- generic panes & grids ---------- */
.grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 1.4rem; margin-top: 1.6rem; }
@media (max-width: 860px) { .grid2 { grid-template-columns: 1fr; } }
.pane { padding: 1.7rem 1.9rem 1.8rem; border-radius: 28px; }
.pane h3 { font-size: 1.15rem; font-weight: 700; letter-spacing: -0.01em; margin: 0 0 0.9rem; color: var(--ink); }
.pane p { font-size: 0.98rem; line-height: 1.65; color: var(--ink-soft); margin: 0 0 0.6rem; }
.pane p:last-child { margin-bottom: 0; }
.pane ul { margin: 0; padding-left: 1.15rem; }
.pane li { font-size: 0.98rem; line-height: 1.7; color: var(--ink-soft); }
.pane li b, .pane p b { color: var(--ink); font-weight: 700; }
.pane code, .note code {
  font-size: 0.88em; padding: 0.1em 0.45em; border-radius: 8px;
  background: rgba(255,255,255,0.14); color: var(--ink);
}
.mini { display: grid; grid-template-columns: repeat(3, 1fr); gap: 0.8rem; margin: 0.4rem 0 1.1rem; }
.mini div { padding: 0.9rem 1rem; border-radius: 18px; background: rgba(255,255,255,0.08); border: 1px solid var(--edge); }
.mini b { display: block; font-size: 1.5rem; font-weight: 800; color: var(--ink); letter-spacing: -0.02em; }
.mini span { font-size: 0.85rem; color: var(--ink-soft); }

.chips { display: flex; flex-wrap: wrap; gap: 0.6rem; }
.chip {
  padding: 0.5rem 1rem; border-radius: 999px; font-size: 0.92rem; font-weight: 600;
  background: rgba(255,255,255,0.10); border: 1px solid var(--edge); color: var(--ink);
}

/* ---------- donut + ring ---------- */
.dial-wrap { display: flex; align-items: center; gap: 1.8rem; flex-wrap: wrap; }
.dial {
  --p: 50; --c1: var(--legit); --c2: var(--fraud);
  width: 180px; height: 180px; border-radius: 50%; flex: none;
  display: grid; place-items: center;
  background: conic-gradient(var(--c2) calc(var(--p) * 1%), var(--c1) 0);
  box-shadow: 0 24px 40px -18px rgba(4,6,30,0.7);
}
.dial.ring { background: conic-gradient(var(--c1) calc(var(--p) * 1%), rgba(255,255,255,0.12) 0); }
.dial > div {
  width: 76%; height: 76%; border-radius: 50%;
  display: grid; place-items: center; text-align: center;
  background: #161b4a; border: 1px solid var(--edge);
  box-shadow: inset 0 6px 14px rgba(255,255,255,0.08);
}
.dial b { font-size: 1.7rem; font-weight: 800; letter-spacing: -0.02em; display: block; line-height: 1.1; }
.dial span { font-size: 0.8rem; color: var(--ink-soft); }
.legend-list { display: grid; gap: 0.9rem; flex: 1; min-width: 190px; }
.legend-list .row { display: flex; align-items: center; gap: 0.7rem; font-size: 0.96rem; color: var(--ink-soft); }
.legend-list .sw { width: 12px; height: 12px; border-radius: 50%; flex: none; }
.legend-list b { margin-left: auto; color: var(--ink); font-weight: 700; }

.hbar { margin: 0 0 1.2rem; }
.hbar .top { display: flex; justify-content: space-between; font-size: 0.95rem; margin-bottom: 0.5rem; color: var(--ink-soft); }
.hbar .top b { color: var(--ink); }
.hbar .track { height: 16px; border-radius: 999px; background: rgba(255,255,255,0.08); box-shadow: inset 0 2px 4px rgba(4,6,30,0.4); overflow: hidden; }
.hbar .fill { height: 100%; border-radius: 999px; }
.hbar .fill.legit { background: linear-gradient(90deg, #2dd4bf, var(--legit)); }
.hbar .fill.fraud { background: linear-gradient(90deg, var(--fraud), #ff6b5a); min-width: 6px; }

/* ---------- workflow (home) ---------- */
.section-title { font-size: 1.5rem; font-weight: 700; letter-spacing: -0.02em; margin: 3rem 0 1.3rem; }
.flow { display: grid; grid-template-columns: repeat(8, 1fr); gap: 0.9rem; align-items: stretch; }
@media (max-width: 1100px) { .flow { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 600px)  { .flow { grid-template-columns: repeat(2, 1fr); } }
.step {
  padding: 1rem 0.9rem 1.1rem; border-radius: 22px; min-height: 120px;
  display: flex; flex-direction: column; justify-content: space-between; gap: 1rem;
  font-size: 0.92rem; font-weight: 600; line-height: 1.3;
  transition: transform .3s cubic-bezier(.2,.8,.2,1), background .3s;
}
.step .n {
  width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center;
  font-size: 0.8rem; font-weight: 700; background: rgba(255,255,255,0.16); border: 1px solid var(--edge);
}
.step:hover { transform: translateY(-5px); background: var(--glass-strong); }
.step.last { background: linear-gradient(145deg, rgba(94,234,212,0.32), rgba(142,162,255,0.16)); border-color: rgba(94,234,212,0.5); }
.step.last .n { background: var(--legit); color: #0d1030; border-color: transparent; }

/* ---------- prediction result ---------- */
.result { display: flex; align-items: center; gap: 1.4rem; padding: 1.6rem 2rem; border-radius: 28px; margin-top: 1.4rem; flex-wrap: wrap; }
.result .icon {
  flex: none; width: 64px; height: 64px; border-radius: 50%; display: grid; place-items: center; font-size: 1.8rem;
  background: rgba(255,255,255,0.14); border: 1px solid var(--edge);
}
.result h2 { font-size: 1.6rem; font-weight: 800; letter-spacing: -0.02em; margin: 0; color: var(--ink); }
.result .txt { flex: 1; min-width: 200px; }
.result .conf { min-width: 220px; flex: 1; max-width: 340px; }
.result.fraud { border-color: rgba(255,138,122,0.7); background: linear-gradient(145deg, rgba(255,138,122,0.30), rgba(255,138,122,0.10)); }
.result.legit { border-color: rgba(94,234,212,0.7); background: linear-gradient(145deg, rgba(94,234,212,0.28), rgba(94,234,212,0.08)); }

/* ---------- native Streamlit widgets ---------- */
[data-testid="stForm"] {
  background: linear-gradient(145deg, var(--glass-strong), var(--glass));
  backdrop-filter: blur(26px) saturate(170%);
  -webkit-backdrop-filter: blur(26px) saturate(170%);
  border: 1px solid var(--edge); border-top-color: var(--edge-top);
  border-radius: 32px; padding: 1.8rem 2rem 2rem;
  box-shadow: 0 1px 0 rgba(255,255,255,0.25) inset, 0 30px 60px -20px rgba(4,6,30,0.65);
}
[data-testid="stWidgetLabel"] p, .stApp label p { color: var(--ink-soft) !important; font-weight: 600; font-size: 0.92rem; }
[data-baseweb="input"], [data-baseweb="base-input"], [data-baseweb="textarea"], [data-baseweb="select"] > div {
  background: rgba(255,255,255,0.08) !important;
  border: 1px solid var(--edge) !important; border-radius: 16px !important;
}
[data-baseweb="input"]:focus-within, [data-baseweb="textarea"]:focus-within, [data-baseweb="select"]:focus-within > div {
  border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(142,162,255,0.28) !important;
}
.stApp input, .stApp textarea, [data-baseweb="select"] * { color: var(--ink) !important; -webkit-text-fill-color: var(--ink); }
.stApp input::placeholder, .stApp textarea::placeholder { color: rgba(243,245,255,0.40) !important; -webkit-text-fill-color: rgba(243,245,255,0.40); }
[data-baseweb="popover"] > div, ul[role="listbox"] { background: #1a1f55 !important; border-radius: 16px !important; border: 1px solid var(--edge); }
ul[role="listbox"] li { color: var(--ink) !important; }
ul[role="listbox"] li:hover, ul[role="listbox"] li[aria-selected="true"] { background: rgba(142,162,255,0.28) !important; }

[data-testid="stFormSubmitButton"] > button, .stButton > button {
  background: linear-gradient(135deg, #8ea2ff, #5eead4); color: #0d1030 !important;
  border: none; border-radius: 999px; padding: 0.75rem 1.6rem; font-weight: 700; font-size: 1rem;
  box-shadow: 0 14px 28px -12px rgba(94,234,212,0.7);
  transition: transform .25s cubic-bezier(.2,.8,.2,1), box-shadow .25s;
}
[data-testid="stFormSubmitButton"] > button p, .stButton > button p { color: #0d1030 !important; font-weight: 700; }
[data-testid="stFormSubmitButton"] > button:hover, .stButton > button:hover {
  transform: translateY(-2px); box-shadow: 0 20px 34px -12px rgba(94,234,212,0.8); color: #0d1030;
}
[data-testid="stAlert"] {
  background: linear-gradient(145deg, rgba(255,255,255,0.14), rgba(255,255,255,0.07));
  border: 1px solid var(--edge); border-radius: 22px; color: var(--ink);
}

/* ---------- motion ---------- */
@keyframes settle {
  from { opacity: 0; transform: translateY(24px) rotateX(9deg); }
  to   { opacity: 1; transform: rotateX(2.5deg); }
}
@keyframes hover { 0%, 100% { transform: translateY(-50%); } 50% { transform: translateY(calc(-50% - 12px)); } }
@media (prefers-reduced-motion: reduce) {
  .hero, .hero .orb { animation: none; }
  .step, [data-testid="stFormSubmitButton"] > button { transition: none; }
}
</style>
"""


def inject() -> None:
    """Call once at the top of every page."""
    st.markdown(CSS, unsafe_allow_html=True)


def html(*lines: str) -> str:
    """Join HTML lines flush-left so Markdown never treats them as a code block."""
    return "".join(line.strip() for line in lines)


def render(*lines: str) -> None:
    st.markdown(html(*lines), unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "") -> None:
    sub = f"<p>{subtitle}</p>" if subtitle else ""
    render(f'<div class="glass page-head"><h1>{title}</h1>{sub}</div>')


def metric(label: str, value: str, share: str = "", tone: str = "", small: bool = False) -> str:
    share_html = f'<p class="share">{share}</p>' if share else ""
    size = " sm" if small else ""
    return html(
        f'<div class="glass metric {tone}">',
        f'<p class="label">{label}</p>',
        f'<p class="value{size}">{value}</p>',
        share_html,
        '<div class="glow"></div></div>',
    )


def metric_row(cards: list[str], cols: int = 3) -> None:
    cls = "metrics cols-4" if cols == 4 else "metrics"
    render(f'<div class="{cls}">{"".join(cards)}</div>')


def note(text: str, floating: bool = False) -> str:
    cls = "glass note float" if floating else "glass note"
    return f'<div class="{cls}"><div class="dot"></div><span>{text}</span></div>'
