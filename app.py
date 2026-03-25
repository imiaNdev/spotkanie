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
# STYLE
# ======================
st.markdown(f"""
<style>
.stApp {{
    background: {COLOR_APP_BG};
}}

section.main > div.block-container {{
    max-width: 1000px;
    padding: 2rem;
}}

.title {{
    font-size: 36px;
    font-weight: 900;
    color: white;
    text-align: center;
}}

.lead-box {{
    margin: 20px auto;
    padding: 18px;
    border-left: 5px solid {COLOR_ACCENT};
    background: rgba(0,0,0,0.4);
    border-radius: 14px;
    font-size: 17px;
    color: {COLOR_TEXT_PRIMARY};
    text-align: center;
}}

div[data-testid="stExpander"] {{
    background: {COLOR_SECTION_BG};
    border-radius: 16px;
    margin-bottom: 12px;
}}
</style>
""", unsafe_allow_html=True)

# ======================
# HEADER
# ======================
st.markdown("""
<div class="title">Przegląd obszarów i inicjatyw sprzedażowych</div>
<div class="lead-box">
Krótkie wprowadzenie w aktualne inicjatywy, blokery oraz sposób pracy na danych,
żeby łatwiej złapać bieżący kontekst sprzedaży.
</div>
""", unsafe_allow_html=True)

# ======================
# BUTTONY
# ======================
c1, c2 = st.columns(2)
with c1:
    if st.button("Rozwiń wszystkie sekcje"):
        st.session_state.expand_all = True
with c2:
    if st.button("Zwiń wszystkie sekcje"):
        st.session_state.expand_all = False

# ======================
# GŁÓWNE INICJATYWY
# ======================
with st.expander("🎯 Główne inicjatywy", expanded=st.session_state.expand_all):

    with st.expander("🟡 CC – jakość rozmów i zgodność skryptu (AI)"):
        st.markdown("""
- Status: [W TRAKCIE]

- Kierunek: wykorzystanie narzędzi AI do wsparcia analizy rozmów sprzedażowych

- Zakres:
  - poprawność realizacji skryptu prawnego w rozmowach sprzedażowych
  - jakość rozmowy i skuteczność sprzedażowa (do dalszego zdefiniowania metryk)

- Kolejny krok: wypracowanie modelu pracy, w którym analiza rozmów realizowana jest bezpośrednio w pionie sprzedaży
  (z wykorzystaniem narzędzi AI jako wsparcia), co pozwoli skrócić czas iteracji i ograniczyć zależności między zespołami
""")

    with st.expander("🟡 CC – odzysk sprzedaży po soft-odmowie"):
        st.markdown("""
- Status: [W TRAKCIE]

- INIT-6319

- Analiza możliwości wdrożenia mechanizmu powrotu klienta do oferty po soft-odmowie
  (np. e-mail + callback / lead)

- Status IT: analiza wstępna

- Potencjał: odzysk części sprzedaży z istniejących kontaktów
  (ok. 100–250 tys. zł rocznie)
""")

    with st.expander("🔵 POS – czas pracy agentów"):
        st.markdown("""
- Status: [FROZEN]

- INIT-6176

- Brak zgody po stronie IT – do ewentualnego planowania w PSO

- Wymaga zmian systemowych w Suflerze (logowanie/wylogowanie agentów)

- Potencjał: poprawa dostępności i zarządzania obsadą
  (ok. 57 tys. zł rocznie)
""")

    with st.expander("🟡 POS – raportowanie wizyt klientów (ruch, wynik, leady)"):
        st.markdown("""
- Status: [W TRAKCIE]

- INIT-6291

- Rozszerzenie raportowania do poziomu pojedynczej wizyty
  (1 klient = 1 kontakt = 1 wynik)

- Cel: pomiar rzeczywistego ruchu oraz konwersji wizyt na sprzedaż

- Potencjał: identyfikacja leadów i wzrost sprzedaży
  (ok. 180–400 tys. zł rocznie)
""")

    with st.expander("🟠 D2D – kontrola dystrybucji ulotek"):
        st.markdown("""
- Status: [OCZEKUJĄCE]

- Temat wstrzymany do momentu wyłonienia nowego dyrektora kanału D2D

- Cel: uzyskanie widoczności pokrycia dystrybucji oraz powiązanie jej z wynikiem sprzedażowym

- Potencjał: wzrost sprzedaży o ok. 20%
  (~200 tys. zł rocznie)

- Alternatywa:
  - zagregowany raport pokazujący per handlowiec liczbę ulotek
  - liczbę połączeń
  - wynik sprzedażowy

- Link:
  https://app.powerbi.com/links/qA-hshMZcv?ctid=7f5db18f-4f22-42c1-b4c8-e8c0d3435484&pbi_source=linkShare
""")

    with st.expander("🟠 D2D – odzysk kontaktów poprzez transfer na CC"):
        st.markdown("""
- Status: [OCZEKUJĄCE]

- Wymaga wpięcia numerów do systemu Avaya – obecnie relacja kosztów do potencjalnego zysku nie uzasadnia priorytetyzacji

- Alternatywa:
  - raport identyfikujący krótkie próby kontaktu (<X sek.)
  - weryfikacja ponownego kontaktu zakończonego dłuższą rozmową
""")

# ======================
# BLOKERY
# ======================
with st.expander("🚧 Kluczowe blokery", expanded=st.session_state.expand_all):
    st.markdown("""
- Potencjał inicjatyw jest widoczny, natomiast część z nich wymaga zaangażowania obszarów wspierających poza sprzedażą

- Ograniczona dostępność zasobów technicznych wpływa dziś na tempo uruchamiania wybranych tematów

- Projekty oparte o zmiany systemowe i integracje mają dłuższy czas wejścia niż inicjatywy operacyjne

- Największym wyzwaniem są zależności międzyzespołowe, a nie brak kierunków działań
""")

# ======================
# DANE I NARZĘDZIA
# ======================
with st.expander("📊 Dane i narzędzia", expanded=st.session_state.expand_all):
    st.markdown("""
**Centrum raportowe Power BI (CT, CUK, POS, D2D):**  
https://app.powerbi.com/links/yotwd4YNRw?ctid=7f5db18f-4f22-42c1-b4c8-e8c0d3435484&pbi_source=linkShare

- W ostatnim czasie raporty Power BI zastąpiły wcześniejszą pracę na Excelach

**Widok zarządczy (Streamlit – w budowie):**
- ruch → deklaracje sprzedaży → realizacje → cele i KPI

**Sposób prezentacji postępów (Task Force / EXCOM / BR):**
- Czy obecny sposób przygotowania materiałów jest optymalny?
- Czy widzisz przestrzeń do usprawnień?

**Kierunek:**
- jeden spójny widok do pracy operacyjnej i zarządczej
""")

    with st.expander("📊 Widok narzędzia operacyjnego", expanded=False):
        st.markdown("""
### Widok operacyjny – szybka ocena realizacji vs plan (ARPU, HC)

- Dyrektor wchodzi w jedno narzędzie i od razu widzi sytuację makro
- realizację vs plan (ARPU, HC)
- trend dzienny
- obszary wymagające reakcji

**Flow procesu sprzedażowego:**
- ruch → deklaracje → realizacja → cel

- Narzędzie odpowiada na pytanie: czy dowozimy i gdzie jest problem

- Power BI = warstwa analityczna (szczegóły)
- Streamlit = warstwa decyzyjna (szybki widok)
""")

        st.image("dashboard.png", use_container_width=True)

# ======================
# CX
# ======================
with st.expander("⚙️ CX – obszary do automatyzacji", expanded=st.session_state.expand_all):
    st.markdown("""
Czy są dziś procesy w obszarze CX, które wymagają ręcznej pracy i mogą być zautomatyzowane?

Czy są miejsca, gdzie tracony jest czas operacyjny (np. raportowanie, przekazywanie informacji, obsługa klienta)?

Czy obecny sposób prezentacji wyników (CX / sprzedaż) jest wystarczający do podejmowania decyzji?
""")

# ======================
# KIERUNEK
# ======================
with st.expander("🔭 Kierunek i next step", expanded=st.session_state.expand_all):
    st.markdown("""
- Widzę swoją rolę jako połączenie analityki, rozwoju narzędzi oraz prowadzenia inicjatyw wspierających efektywność sprzedaży

- Naturalnym kierunkiem jest dalsze uporządkowanie obszaru i budowa spójnego podejścia do pracy na danych

- Chciałbym doprecyzować docelowy zakres tej roli oraz sposób jej osadzenia w organizacji

- W kolejnym kroku chciałbym również porozmawiać o tym, jak ten zakres powinien przekładać się na poziom odpowiedzialności i wynagrodzenia
""")