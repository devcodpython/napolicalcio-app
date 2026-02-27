# config.py
"""
MODULO CONFIGURAZIONE: Gestisce costanti, colori e parametri tecnici.
Versione: 1.0
"""

class Config:
    # --- COLORI UFFICIALI ---
    # Azzurro Napoli (Hex e RGBA per Kivy)
    COLOR_AZZURRO_NAPOLI = [0, 0.58, 0.827, 1]  # #0094D3
    COLOR_BIANCO = [1, 1, 1, 1]                # #FFFFFF
    
    # --- IMPOSTAZIONI GRAFICHE ---
    APP_NAME = "Napoli Strategy Dashboard"
    LOGO_N_RATIO = 0.6  # Dimensione della N rispetto al cerchio
    SIDEBAR_WIDTH = 300 # Larghezza menu laterale
    
    # --- LOGICA ANALISI INEDITA (Soglie) ---
    # Soglie per Indice Fedeltà Tattica (IFT)
    IFT_THRESHOLD_HIGH = 85
    IFT_THRESHOLD_MID = 60
    
    # Moltiplicatori per Valore di Rottura (VdR)
    VDR_MULTIPLIER_DRIBBLING = 15
    VDR_MULTIPLIER_FORWARD_PASS = 10
    VDR_MULTIPLIER_RECOVERY = 5

    # --- DATI ---
    MAX_MATCHES_SIDEBAR = 10
    MOCK_DATA_URL = "https://stats-napoli-api-mock.com" # Esempio per test