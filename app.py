# app.py
"""
PUNTO DI INGRESSO WEB (Streamlit): La cabina di regia per tuo padre.
Versione: 2.0 (Menu Centrale, Ultima Partita Automatica, Rosa Aggiornata)
"""
import streamlit as st
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

# --- MENU CENTRALE (Risolve Problema 1 e 2) ---
if not matches:
    st.error("Nessuna partita trovata.")
else:
    match_dict = {f"{m['comp']} | {m['opponent']} ({m['score']})": m for m in matches}
    
    # Menu a tendina gigante al centro (index=0 seleziona l'ultima in automatico)
    selected_match_label = st.selectbox("⚽ Seleziona la Partita:", list(match_dict.keys()), index=0)
    selected_match = match_dict[selected_match_label]

    # --- SIMULAZIONE LOGICA DATI ---
    win = "-" in selected_match['score'] and int(selected_match['score'].split("-")[0]) > int(selected_match['score'].split("-")[1])
    
    team_stats = {
        'opp_passes': 300 if win else 450, 
        'def_actions': 55 if win else 30, 
        'att_left': 45 if win else 30, 
        'att_center': 25 if win else 40, 
        'att_right': 30 if win else 30,
        'passes_final_third': 220 if win else 110, 
        'total_passes': 550
    }
    coach_data = AdvancedAnalysisEngine.analyze_coach_strategy(team_stats)
    
    # LISTA GIOCATORI AGGIORNATA (Rosa Attuale + Ruoli)
    players_mock_stats = [
        ("Meret", {'role': 'GK', 'saves': 4 if win else 2, 'clean_sheet': win}),
        ("Di Lorenzo", {'role': 'DEF', 'prog_passes': 6 if win else 3, 'passes_box': 2, 'dribbles': 1}),
        ("Rrahmani", {'role': 'DEF', 'prog_passes': 3, 'passes_box': 0, 'dribbles': 0}),
        ("Buongiorno", {'role': 'DEF', 'prog_passes': 8, 'passes_box': 0, 'dribbles': 1}),
        ("Olivera", {'role': 'DEF', 'prog_passes': 5, 'passes_box': 1, 'dribbles': 2}),
        ("Lobotka", {'role': 'MID', 'prog_passes': 15, 'passes_box': 1, 'dribbles': 2}),
        ("Anguissa", {'role': 'MID', 'prog_passes': 7, 'passes_box': 2, 'dribbles': 3}),
        ("McTominay", {'role': 'MID', 'prog_passes': 5, 'passes_box': 4, 'dribbles': 3 if win else 1}),
        ("Politano", {'role': 'ATT', 'prog_passes': 4, 'passes_box': 5, 'dribbles': 4}),
        ("Kvaratskhelia", {'role': 'ATT', 'prog_passes': 9 if win else 3, 'passes_box': 7, 'dribbles': 8}),
        ("Lukaku", {'role': 'ATT', 'prog_passes': 2, 'passes_box': 8, 'dribbles': 1}),
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