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

    .subnote {{
        font-size: 15px;
        color: #C9CDD2;
        margin-top: -4px;
        margin-bottom: 10px;
        line-height: 1.5;
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

    with st.expander("🟡 CC – jakość rozmów i zgodność skryptu (AI)"):
        st.markdown("""
**Status:** 🟡 w trakcie  

**Kierunek:** wykorzystanie narzędzi AI do wsparcia analizy rozmów sprzedażowych  

**Zakres:**  
• poprawność realizacji skryptu prawnego w rozmowach sprzedażowych  
• jakość rozmowy i skuteczność sprzedażowa (do dalszego zdefiniowania metryk)  

**Kolejny krok:** wypracowanie modelu pracy, w którym analiza rozmów realizowana jest bezpośrednio w pionie sprzedaży (z wykorzystaniem narzędzi AI jako wsparcia), co pozwoli skrócić czas iteracji i ograniczyć zależności między zespołami  
""")

    with st.expander("🟡 CC – odzysk sprzedaży po soft-odmowie"):
        st.markdown("""
**Status:** 🟡 w trakcie  
**INIT:** 6319  

**Opis:** analiza możliwości wdrożenia mechanizmu powrotu klienta do oferty po soft-odmowie (np. e-mail + callback / lead)  

**Status IT:** analiza wstępna  

**Potencjał:** odzysk części sprzedaży z istniejących kontaktów (ok. 100–250 tys. zł rocznie)  
""")

    with st.expander("🟠 D2D – kontrola dystrybucji ulotek"):
        st.markdown("""
**Status:** 🟠 oczekujące  

**Opis:** temat wstrzymany do momentu wyłonienia nowego dyrektora kanału D2D  

**Cel:** uzyskanie widoczności pokrycia dystrybucji oraz powiązanie jej z wynikiem sprzedażowym  

**Potencjał:** wzrost sprzedaży o ok. 20% (~200 tys. zł rocznie)  

**Alternatywa:** zagregowany raport pokazujący per handlowiec liczbę ulotek, liczbę połączeń oraz wynik sprzedażowy  
https://app.powerbi.com/links/qA-hshMZcv?ctid=7f5db18f-4f22-42c1-b4c8-e8c0d3435484&pbi_source=linkShare  
""")

    with st.expander("🔵 POS – czas pracy agentów"):
        st.markdown("""
**Status:** 🔵 FROZEN  
**INIT:** 6176  

**Opis:** brak zgody po stronie IT – do ewentualnego planowania w PSO  

**Wymaga:** zmian systemowych w Suflerze (logowanie / wylogowanie agentów)  

**Potencjał:** poprawa dostępności i zarządzania obsadą (ok. 57 tys. zł rocznie)  
""")

    with st.expander("🟡 POS – raportowanie wizyt klientów"):
        st.markdown("""
**Status:** 🟡 w trakcie  
**INIT:** 6291  

**Opis:** rozszerzenie raportowania do poziomu pojedynczej wizyty (1 klient = 1 kontakt = 1 wynik)  

**Cel:** pomiar rzeczywistego ruchu oraz konwersji wizyt na sprzedaż  

**Potencjał:** identyfikacja leadów i wzrost sprzedaży (ok. 180–400 tys. zł rocznie)  
""")

    with st.expander("🟠 D2D – odzysk kontaktów poprzez transfer na CC"):
        st.markdown("""
**Status:** 🟠 oczekujące  

**Opis:** wymaga wpięcia numerów do systemu Avaya – obecnie relacja kosztów do potencjalnego zysku nie uzasadnia priorytetyzacji  

**Alternatywa:** raport identyfikujący krótkie próby kontaktu (<X sek.) oraz weryfikujący ponowny kontakt zakończony dłuższą rozmową  
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

- Czy obecny sposób przygotowania prezentacji dla EXCOM i materiałów na BR jest optymalny, czy widzisz przestrzeń do usprawnień?  

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