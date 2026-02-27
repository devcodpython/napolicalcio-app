# data_provider.py
"""
MODULO DATA PROVIDER: Motore con Filtro "VIP" per Serie A e pass-through Coppe.
Versione: 2.4
"""
class DataProvider:
    @staticmethod
    def get_last_matches():
        # 1. La "Lista VIP" richiesta da tuo padre
        serie_a_vip = ["Inter", "Milan", "Juventus", "Como", "Atalanta", "Lazio", "Roma"]

        # 2. Simulazione di un calendario reale grezzo da cui il motore deve estrarre e filtrare
        raw_history = [
            {"comp": "SERIE A", "opponent": "Empoli", "score": "2-0", "date": "15/03", "venue": "H"}, # Verrà scartata
            {"comp": "CHAMPIONS", "opponent": "Barcellona", "score": "2-1", "date": "10/03", "venue": "H"}, # Tenuta (Coppa)
            {"comp": "SERIE A", "opponent": "Juventus", "score": "0-0", "date": "03/03", "venue": "A"}, # Tenuta (VIP)
            {"comp": "SERIE A", "opponent": "Lecce", "score": "3-0", "date": "25/02", "venue": "H"}, # Verrà scartata
            {"comp": "SERIE A", "opponent": "Lazio", "score": "2-1", "date": "22/02", "venue": "H"}, # Tenuta (VIP)
            {"comp": "CHAMPIONS", "opponent": "Real Madrid", "score": "1-1", "date": "18/02", "venue": "A"}, # Tenuta (Coppa)
            {"comp": "COPPA ITA", "opponent": "Fiorentina", "score": "1-0", "date": "12/02", "venue": "H"}, # Tenuta (Coppa)
            {"comp": "SERIE A", "opponent": "Como", "score": "1-1", "date": "08/02", "venue": "A"}, # Tenuta (VIP)
            {"comp": "SERIE A", "opponent": "Milan", "score": "3-1", "date": "01/02", "venue": "A"}, # Tenuta (VIP)
            {"comp": "SERIE A", "opponent": "Roma", "score": "1-0", "date": "25/01", "venue": "H"}, # Tenuta (VIP)
            {"comp": "SUPERCOPPA", "opponent": "Inter", "score": "2-2", "date": "20/01", "venue": "N"}, # Tenuta (Coppa)
            {"comp": "SERIE A", "opponent": "Atalanta", "score": "2-2", "date": "11/01", "venue": "H"}, # Tenuta (VIP)
            {"comp": "SERIE A", "opponent": "Monza", "score": "2-0", "date": "04/01", "venue": "A"} # Verrà scartata
        ]

        # 3. La Logica di Filtraggio Intelligente
        filtered_matches = []
        for match in raw_history:
            if match["comp"] == "SERIE A":
                # Se è Serie A, controlla se l'avversario è nella lista VIP
                if match["opponent"] in serie_a_vip:
                    filtered_matches.append(match)
            else:
                # Se NON è Serie A (Champions, Coppa, ecc.), la tiene sempre
                filtered_matches.append(match)
            
            # Quando il cestino ha esattamente 10 partite, si ferma
            if len(filtered_matches) == 10:
                break
        
        return filtered_matches