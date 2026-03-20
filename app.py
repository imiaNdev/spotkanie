import streamlit as st

# ======================
# KONFIGURACJA STRONY
# ======================
st.set_page_config(
    page_title="Przegląd obszarów i inicjatyw sprzedażowych",
    layout="centered",
)

# ======================
# SESSION STATE
# ======================
if "expand_all" not in st.session_state:
    st.session_state.expand_all = False

# ======================
# DESIGN SYSTEM
# ======================
COLOR_APP_BG = "#0E1117"
COLOR_SECTION_BG = "#163329"
COLOR_ACCENT = "#A37752"
COLOR_TEXT_PRIMARY = "#E8E8E8"
COLOR_TEXT_SECONDARY = "#B0B3B8"

# ======================
# STYLE (CSS)
# ======================
st.markdown(
    f"""
    <style>
    .stApp {{
        background: {COLOR_APP_BG};
    }}

    section.main > div.block-container {{
        max-width: 1000px;
        padding-left: 2rem;
        padding-right: 2rem;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }}

    .header-wrap {{
        max-width: 1000px;
        margin: 0 auto;
        text-align: center;
        padding-top: 10px;
    }}

    .title {{
        font-size: clamp(30px, 3.5vw, 44px);
        font-weight: 900;
        color: #FFFFFF;
        line-height: 1.1;
        margin: 0 0 12px 0;
    }}

    .lead-box {{
        margin: 18px auto 28px auto;
        padding: 18px 22px;
        border-left: 5px solid {COLOR_ACCENT};
        background: linear-gradient(135deg, rgba(0,0,0,0.45), rgba(0,0,0,0.25));
        border-radius: 14px;
        font-size: 18px;
        color: {COLOR_TEXT_PRIMARY};
        line-height: 1.65;
        max-width: 880px;
        font-weight: 500;
    }}

    .stButton > button {{
        border-radius: 12px;
        padding: 0.45rem 1.2rem;
        font-weight: 600;
        background-color: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.18);
        color: {COLOR_TEXT_PRIMARY};
        width: 100%;
    }}

    div[data-testid="stExpander"] {{
        background: {COLOR_SECTION_BG};
        border-radius: 18px;
        border: 1px solid rgba(255,255,255,0.12);
        margin-bottom: 14px;
        overflow: hidden;
    }}

    div[data-testid="stExpander"] > details > summary {{
        padding: 12px 16px;
        background: rgba(0,0,0,0.25);
    }}

    div[data-testid="stExpander"] > details > summary p {{
        color: {COLOR_ACCENT} !important;
        font-size: 20px !important;
        font-weight: 850 !important;
        margin: 0 !important;
    }}

    div[data-testid="stExpander"] > details > div {{
        padding: 16px 20px 20px 20px;
        background: {COLOR_SECTION_BG};
        color: {COLOR_TEXT_PRIMARY};
    }}

    div[data-testid="stExpander"] li {{
        font-size: 17px;
        margin-bottom: 8px;
        line-height: 1.45;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ======================
# HEADER
# ======================
st.markdown("""
<div class="header-wrap">
  <div class="title">
    Przegląd obszarów i inicjatyw sprzedażowych
  </div>
  <div class="lead-box">
    Krótkie wprowadzenie w aktualne inicjatywy, blokery oraz sposób pracy na danych,
    żeby łatwiej złapać bieżący kontekst sprzedaży.
  </div>
</div>
""", unsafe_allow_html=True)

# ======================
# CONTROLS
# ======================
c1, c2 = st.columns(2)
with c1:
    if st.button("Rozwiń wszystkie sekcje"):
        st.session_state.expand_all = True
with c2:
    if st.button("Zwiń wszystkie sekcje"):
        st.session_state.expand_all = False

# ======================
# SEKCJE
# ======================
with st.expander("🎯 Główne inicjatywy", expanded=st.session_state.expand_all):
    st.markdown("""
- CC – odzysk sprzedaży po soft-odmowie  
- CC – jakość rozmów i zgodność skryptu (w tym AI)  
- D2D – kontrola dystrybucji ulotek  
- D2D – odzysk kontaktów poprzez transfer na CC  
- POS – czas pracy agentów, ruch klientów, wynik rozmów oraz zbieranie leadów przy braku sprzedaży  
""")

with st.expander("🚧 Kluczowe blokery", expanded=st.session_state.expand_all):
    st.markdown("""
- Potencjał inicjatyw jest widoczny, natomiast część z nich wymaga zaangażowania obszarów wspierających poza sprzedażą  
- Ograniczona dostępność zasobów technicznych wpływa dziś na tempo uruchamiania wybranych tematów  
- Projekty oparte o zmiany systemowe i integracje mają dłuższy czas wejścia niż inicjatywy operacyjne  
- Największym wyzwaniem są zależności międzyzespołowe, a nie brak kierunków działań  
""")

with st.expander("📊 Dane i narzędzia", expanded=st.session_state.expand_all):
    st.markdown("""
- Centrum raportowe Power BI (CT, CUK, POS, D2D):  
https://app.powerbi.com/links/yotwd4YNRw?ctid=7f5db18f-4f22-42c1-b4c8-e8c0d3435484&pbi_source=linkShare  

- W ostatnim czasie raporty Power BI zastąpiły wcześniejszą pracę na Excelach  

- Widok zarządczy (Streamlit – w budowie):  
ruch → deklaracje sprzedaży → realizacje → cele i KPI  

- Czy obecny sposób przygotowania prezentacji na EXECOM i materiałów na BR jest optymalny,
czy widzisz przestrzeń do usprawnień?  

- Kierunek: jeden spójny widok do pracy operacyjnej i zarządczej  
""")

with st.expander("⚙️ CX – obszary do automatyzacji", expanded=st.session_state.expand_all):
    st.markdown("""
- Czy są dziś procesy w obszarze CX, które wymagają ręcznej pracy i mogą być zautomatyzowane?  

- Czy są miejsca, gdzie tracony jest czas operacyjny (np. raportowanie, przekazywanie informacji, obsługa klienta)?  

- Czy obecny sposób prezentacji wyników (CX / sprzedaż) jest wystarczający do podejmowania decyzji?  
""")

with st.expander("🔭 Kierunek i next step", expanded=st.session_state.expand_all):
    st.markdown("""
- Chcę dalej rozwijać się w kierunku łączenia danych, procesów i decyzji sprzedażowych  

- Widzę przestrzeń do uporządkowania obszaru i budowy spójnego podejścia do pracy na danych  

- Zależy mi na większym zaangażowaniu w tematy przekładające się bezpośrednio na wynik i efektywność  

- Jestem otwarty na rozmowę o dalszym kierunku współpracy i zakresie odpowiedzialności  
""")