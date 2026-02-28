# data_provider.py
"""
FORNITORE DI DATI LIVE (API-Football)
Connessione al server globale in tempo reale.
"""
import requests

class DataProvider:
    # La tua chiave personale
    API_KEY = "727e65d57amsh1648a23a7a96eefp1e4daajsnde9ef22a6d29"
    
    @staticmethod
    def get_last_matches():
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
        # 98 è l'ID del Napoli. last=5 prende le ultime 5 partite giocate ufficiali.
        querystring = {"team": "98", "last": "5"}
        headers = {
            "X-RapidAPI-Key": DataProvider.API_KEY,
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        
        try:
            # L'app "telefona" al server per chiedere i dati veri
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            
            matches = []
            # L'API ci dà i dati dalla più vecchia alla più nuova. Noi le giriamo (reversed)
            # per avere l'ultimissima partita giocata in cima al menu.
            for item in reversed(data.get('response', [])):
                comp = item['league']['name']
                home_team = item['teams']['home']['name']
                away_team = item['teams']['away']['name']
                home_goals = item['goals']['home']
                away_goals = item['goals']['away']
                
                # Sicurezza: se una partita non ha gol validi, mettiamo 0
                if home_goals is None: home_goals = 0
                if away_goals is None: away_goals = 0
                
                # Regoliamo la visuale sempre dal punto di vista del Napoli
                if home_team == "Napoli":
                    opponent = f"{away_team} (Casa)"
                    score = f"{home_goals}-{away_goals}" # I gol del Napoli sono i primi
                else:
                    opponent = f"{home_team} (Fuori)"
                    score = f"{away_goals}-{home_goals}" # I gol del Napoli sono i primi
                    
                matches.append({
                    'comp': comp,
                    'opponent': opponent,
                    'score': score
                })
                
            if not matches:
                return [{'comp': 'Sistema', 'opponent': 'Nessuna Partita', 'score': '0-0'}]
                
            return matches
            
        except Exception as e:
            # Se internet non va, non facciamo rompere l'app
            return [{'comp': 'Errore', 'opponent': 'Connessione API fallita', 'score': '0-0'}]
