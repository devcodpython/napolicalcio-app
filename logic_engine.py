# logic_engine.py
"""
MOTORE DI ANALISI TATTICA
Versione: 2.0 (Intelligenza per Portieri e Difensori)
"""

class AdvancedAnalysisEngine:
    
    @staticmethod
    def analyze_coach_strategy(team_stats):
        # Calcolo simulato per PPDA
        ppda = round(team_stats.get('opp_passes', 400) / max(team_stats.get('def_actions', 40), 1), 1)
        
        # Asimmetria
        left = team_stats.get('att_left', 33)
        right = team_stats.get('att_right', 33)
        if left > right + 10:
            asymmetry = "Sbilanciata a Sinistra (Catena Kvara)"
        elif right > left + 10:
            asymmetry = "Sbilanciata a Destra (Catena Politano/Di Lorenzo)"
        else:
            asymmetry = "Equilibrata"
            
        # Dominio Territoriale (IDT)
        idt = round((team_stats.get('passes_final_third', 100) / team_stats.get('total_passes', 500)) * 100 * 2, 1)
        idt = min(idt, 99.9)
        
        return {
            'ppda': str(ppda),
            'asymmetry': asymmetry,
            'idt': idt,
            'report_possesso': "Fase di Possesso: La squadra ha mantenuto un baricentro alto, cercando costantemente l'imbucata per le punte.",
            'report_non_possesso': f"Fase di Non Possesso: Pressing aggressivo registrato con un PPDA di {ppda}. Ottimo recupero palla alto.",
            'chiave_tattica': f"Chiave Tattica: L'attacco si è sviluppato principalmente con una manovra {asymmetry.lower()}."
        }

    @staticmethod
    def analyze_player_advanced(name, stats):
        role = stats.get('role', 'MID')
        
        # LOGICA SPECIALE PER IL PORTIERE (Risolve il Problema 3: Meret)
        if role == 'GK':
            saves = stats.get('saves', 0)
            clean_sheet = stats.get('clean_sheet', False)
            
            profile_text = f"La prestazione di {name} tra i pali è stata determinante. Ha registrato **{saves} parate cruciali**."
            if clean_sheet:
                profile_text += " Ha garantito sicurezza all'intero reparto, mantenendo la porta inviolata (Clean Sheet)."
            else:
                profile_text += " Nonostante le reti subite, ha gestito bene le uscite e la costruzione dal basso."
                
            return {
                'name': name,
                'is_gk': True,
                'saves': saves,
                'profile': profile_text
            }

        # LOGICA PER I GIOCATORI DI MOVIMENTO
        prog_passes = stats.get('prog_passes', 0)
        passes_box = stats.get('passes_box', 0)
        dribbles = stats.get('dribbles', 0)
        
        xt = round((prog_passes * 0.15) + (passes_box * 0.2), 2)
        lba = round((dribbles * 0.3) + (passes_box * 0.4), 2)
        
        if role == 'DEF':
            profile_text = f"Fase difensiva solida. Ha contribuito alla prima costruzione con {prog_passes} passaggi progressivi, eludendo la pressione avversaria."
        elif role == 'MID':
            profile_text = f"Perno del centrocampo. Ha generato un Indice di Minaccia (xT) di {xt}, verticalizzando bene l'azione verso le fasce e gli attaccanti."
        else: # ATT
            profile_text = f"Spina nel fianco per la difesa avversaria. Forte propensione offensiva con {dribbles} dribbling riusciti e {passes_box} palloni toccati in area (LBA: {lba})."

        return {
            'name': name,
            'is_gk': False,
            'xt': xt,
            'lba': lba,
            'profile': profile_text
        }