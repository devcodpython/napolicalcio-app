# data_provider.py
"""
FORNITORE DI DATI
Versione: 4.0 (Dati Reali Aggiornati - Febbraio 2026)
"""

class DataProvider:
    @staticmethod
    def get_last_matches():
        # Lista delle ultime partite reali (dalla più recente alla più vecchia).
        # ATTENZIONE: Il primo numero dello 'score' sono sempre i gol del Napoli!
        return [
            {'comp': 'Serie A', 'opponent': 'Atalanta (Fuori)', 'score': '1-2'},
            {'comp': 'Serie A', 'opponent': 'Roma (Casa)', 'score': '2-2'},
            {'comp': 'Coppa Italia', 'opponent': 'Como (Casa)', 'score': '1-1'},
            {'comp': 'Serie A', 'opponent': 'Genoa (Fuori)', 'score': '3-2'},
            {'comp': 'Serie A', 'opponent': 'Juventus (Casa)', 'score': '1-0'},
            {'comp': 'Supercoppa', 'opponent': 'Inter (Neutro)', 'score': '0-1'},
        ]
