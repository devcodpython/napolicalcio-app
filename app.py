# app.py
"""
PUNTO DI INGRESSO WEB (Streamlit): La cabina di regia per tuo padre.
Versione: 3.0 (Motore di Variabilità Dinamica per le Partite)
"""
import streamlit as st
import random
from data_provider import DataProvider
from logic_engine import AdvancedAnalysisEngine

# 1. Configurazione della Pagina Web
st.set_page_config(page_title="NapoliCalcio", page_icon="⚽", layout="wide")

# 2. INIEZIONE CSS: Ricostruiamo la veste grafica e NASCONDIAMO IL BOLLINO
st.markdown("""
    <style>
    /* KILLER DEI MENU E DEI BOLLINI STREAMLIT */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .viewerBadge_container__1JCJq {display: none !important;}
    .viewerBadge_link__1S137 {display: none !important;}
    [data-testid="stCreatorBadge"] {display: none !important;}
    iframe[title="Streamlit Badge"] {display: none !important;}
    
    /* LA NOSTRA GRAFICA AZZURRA */
    .stApp { background-color: #0087D1 !important; }
    [data-testid="stSidebar"] { background-color: #003c82 !important; display: none; }
    h1, h2, h3, h4, h5, h6, .stMarkdown p, label { color: #FFFFFF !important; }
    [data-testid="stMetricValue"] { color: #FFFFFF !important; }
    [data-testid="stMetricLabel"] p { color: #E0E0E0 !important; font-weight: bold; }
    [data-testid="stExpander"] { background-color: #FFFFFF !important; border-radius: 10px !important; border: none !important; margin-bottom: 10px; }
    [data-testid="stExpander"] summary p { color: #0087D1 !important; font-weight: bold !important; font-size: 1.1rem !important; }
    .stAlert { background-color: rgba(255, 255, 255, 0.95) !important; border-radius: 10px !important; border: none !important; }
    .stAlert p { color: #003c82 !important; }
    </style>
""", unsafe_allow_html=True)

# 3. IL LOGO VETTORIALE
logo_svg = """
<div style="display: flex; justify-content: center; margin-bottom: 10px; margin-top: 20px;">
    <svg width="160" height="160" viewBox="0 0 160 160" xmlns="http://www.w3.org/2000/svg">
        <circle cx="80" cy="80" r="75" fill="#0087D1" />
        <circle cx="80" cy="80" r="72" fill="none" stroke="white" stroke-width="2.5" />
        <circle cx="80" cy="80" r="62" fill="none" stroke="white" stroke-width="2.5" />
        <path d="M 50 110 L 50 50 L 110 110 L 110 50" fill="none" stroke="white" stroke-width="14" stroke-linecap="square" stroke-linejoin="miter" />
    </svg>
</div>
"""
st.markdown(logo_svg, unsafe_allow_html=True)

# --- INIZIO LOGICA DELL'APP ---
@st.cache_data
def load_matches():
    return DataProvider.get_last_matches()

matches = load_matches()

st.markdown("<h2 style='text-align: center;'>Analisi Tattica Napoli</h2>", unsafe_allow_html=True)

# --- MENU CENTRALE ---
if not matches:
    st.error("Nessuna partita trovata.")
else:
    match_dict = {f"{m['comp']} | {m['opponent']} ({m['score']})": m for m in matches}
    
    selected_match_label = st.selectbox("⚽ Seleziona la Partita:", list(match_dict.keys()), index=0)
    selected_match = match_dict[selected_match_label]

    # --- SIMULAZIONE LOGICA DATI DINAMICA ---
    # Usiamo il nome della partita come "seme" per generare dati sempre diversi ma fissi per QUELLA specifica partita!
    random.seed(selected_match_label)
    
    win = "-" in selected_match['score'] and int(selected_match['score'].split("-")[0]) > int(selected_match['score'].split("-")[1])
    
    # Statistiche di squadra dinamiche e uniche per ogni partita
    team_stats = {
        'opp_passes': random.randint(250, 500), 
        'def_actions': random.randint(30, 65), 
        'att_left': random.randint(25, 45), 
        'att_center': random.randint(20, 40), 
        'att_right': random.randint(25, 45),
        'passes_final_third': random.randint(110, 240), 
        'total_passes': random.randint(450, 650)
    }
    coach_data = AdvancedAnalysisEngine.analyze_coach_strategy(team_stats)
    
    # LISTA GIOCATORI CON DATI VARIABILI (Ogni partita avranno statistiche diverse)
    players_mock_stats = [
        ("Meret", {'role': 'GK', 'saves': random.randint(1, 5), 'clean_sheet': win}),
        ("Di Lorenzo", {'role': 'DEF', 'prog_passes': random.randint(3, 9), 'passes_box': random.randint(0, 3), 'dribbles': random.randint(0, 2)}),
        ("Rrahmani", {'role': 'DEF', 'prog_passes': random.randint(1, 5), 'passes_box': 0, 'dribbles': 0}),
        ("Buongiorno", {'role': 'DEF', 'prog_passes': random.randint(4, 10), 'passes_box': 0, 'dribbles': random.randint(0, 1)}),
        ("Olivera", {'role': 'DEF', 'prog_passes': random.randint(3, 7), 'passes_box': random.randint(0, 2), 'dribbles': random.randint(0, 3)}),
        ("Lobotka", {'role': 'MID', 'prog_passes': random.randint(10, 22), 'passes_box': random.randint(0, 2), 'dribbles': random.randint(1, 3)}),
        ("Anguissa", {'role': 'MID', 'prog_passes': random.randint(5, 12), 'passes_box': random.randint(1, 3), 'dribbles': random.randint(1, 4)}),
        ("McTominay", {'role': 'MID', 'prog_passes': random.randint(4, 9), 'passes_box': random.randint(2, 6), 'dribbles': random.randint(1, 3)}),
        ("Politano", {'role': 'ATT', 'prog_passes': random.randint(2, 6), 'passes_box': random.randint(3, 8), 'dribbles': random.randint(2, 6)}),
        ("Kvaratskhelia", {'role': 'ATT', 'prog_passes': random.randint(4, 11), 'passes_box': random.randint(5, 10), 'dribbles': random.randint(5, 11)}),
        ("Lukaku", {'role': 'ATT', 'prog_passes': random.randint(1, 4), 'passes_box': random.randint(6, 12), 'dribbles': random.randint(0, 2)}),
    ]
    
    players_data = [
        AdvancedAnalysisEngine.analyze_player_advanced(name, stats) 
        for name, stats in players_mock_stats
    ]

    # --- DASHBOARD CENTRALE WEB ---
    st.markdown("---")
    st.header("TACTICAL BOARD: STRATEGIA MISTER")
    
    col1, col2, col3 = st.columns(3)
    col1.metric(label="PPDA (Pressing)", value=coach_data['ppda'])
    col2.metric(label="Asimmetria", value="Info") 
    col3.metric(label="Dominio (IDT)", value=f"{coach_data['idt']}%")
    
    st.caption(f"**Asimmetria Manovra:** {coach_data['asymmetry']}")

    st.info(coach_data['report_possesso'])
    st.warning(coach_data['report_non_possesso'])
    st.success(coach_data['chiave_tattica'])

    st.markdown("---")
    st.header("👕 LE PAGELLE TATTICHE")
    
    for player in players_data:
        # Se è il portiere, mostra Parate invece di xT/LBA
        if player.get('is_gk'):
            with st.expander(f"🧤 {player['name']} | Parate: {player.get('saves', 0)}"):
                st.markdown(f"<div style='color: #222222 !important; font-size: 1rem; line-height: 1.5;'>{player['profile']}</div>", unsafe_allow_html=True)
        else:
            with st.expander(f"⚽ {player['name']} | xT: {player['xt']} | LBA: {player['lba']}"):
                st.markdown(f"<div style='color: #222222 !important; font-size: 1rem; line-height: 1.5;'>{player['profile']}</div>", unsafe_allow_html=True)
