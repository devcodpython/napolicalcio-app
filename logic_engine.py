# logic_engine.py
"""
MOTORE DI ANALISI TATTICA
Versione: 3.0 (Analisi Testuali Dinamiche e Variabili)
"""

class AdvancedAnalysisEngine:
    
    @staticmethod
    def analyze_coach_strategy(team_stats):
        # Calcolo simulato per PPDA
        ppda_val = team_stats.get('opp_passes', 400) / max(team_stats.get('def_actions', 40), 1)
        ppda = round(ppda_val, 1)
        
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
        
        # --- TESTI DINAMICI BASATI SUI NUMERI ---
        
        # 1. Fase di Possesso (basata sull'IDT)
        if idt > 60:
            report_possesso = f"Fase di Possesso: Dominio territoriale netto ({idt}%). La squadra ha schiacciato l'avversario nella propria trequarti con un giro palla avvolgente."
        elif idt > 40:
            report_possesso = f"Fase di Possesso: Gestione equilibrata ({idt}%). Buona alternanza tra possesso consolidato e verticalizzazioni improvvise."
        else:
            report_possesso = f"Fase di Possesso: Baricentro basso ({idt}%). La squadra ha faticato a mantenere il controllo del pallone, affidandosi molto alle ripartenze."
            
        # 2. Fase di Non Possesso (basata sul PPDA)
        if ppda < 8:
            report_non_possesso = f"Fase di Non Possesso: Pressing feroce e asfissiante (PPDA: {ppda}). Ottimo recupero palla alto che ha tolto respiro agli avversari."
        elif ppda < 12:
            report_non_possesso = f"Fase di Non Possesso: Pressione moderata (PPDA: {ppda}). La squadra ha scelto momenti specifici per aggredire, mantenendo compattezza."
        else:
            report_non_possesso = f"Fase di Non Possesso: Atteggiamento attendista (PPDA: {ppda}). Linee strette e difesa posizionale per non concedere troppa profondità."
            
        # 3. Chiave Tattica (basata sull'Asimmetria)
        if "Sinistra" in asymmetry:
            chiave_tattica = "Chiave Tattica: Sviluppo offensivo concentrato a sinistra, cercando costantemente l'isolamento e l'uno contro uno di Kvaratskhelia."
        elif "Destra" in asymmetry:
            chiave_tattica = "Chiave Tattica: Sovrapposizioni continue a destra. L'asse Di Lorenzo-Politano è stato il motore principale per scardinare la difesa."
        else:
            chiave_tattica = "Chiave Tattica: Manovra corale ed equilibrata. La squadra ha utilizzato l'intera ampiezza del campo senza dare punti di riferimento."

        return {
            'ppda': str(ppda),
            'asymmetry': asymmetry,
            'idt': idt,
            'report_possesso': report_possesso,
            'report_non_possesso': report_non_possesso,
            'chiave_tattica': chiave_tattica
        }

    @staticmethod
    def analyze_player_advanced(name, stats):
        role = stats.get('role', 'MID')
        
        if role == 'GK':
            saves = stats.get('saves', 0)
            clean_sheet = stats.get('clean_sheet', False)
            
            if saves > 3:
                profile_text = f"Decisivo tra i pali con ben **{saves} parate cruciali** che hanno salvato il risultato."
            elif saves > 0:
                profile_text = f"Attento quando chiamato in causa, ha registrato **{saves} parate** sicure."
            else:
                profile_text = f"Giornata relativamente tranquilla, ordinaria amministrazione senza dover compiere miracoli."
                
            if clean_sheet:
                profile_text += " Monumentale: chiude con la porta inviolata (Clean Sheet)."
            else:
                profile_text += " Nonostante le reti subite, si è dimostrato affidabile nelle uscite."
                
            return {
                'name': name,
                'is_gk': True,
                'saves': saves,
                'profile': profile_text
            }

        prog_passes = stats.get('prog_passes', 0)
        passes_box = stats.get('passes_box', 0)
        dribbles = stats.get('dribbles', 0)
        
        xt = round((prog_passes * 0.15) + (passes_box * 0.2), 2)
        lba = round((dribbles * 0.3) + (passes_box * 0.4), 2)
        
        if role == 'DEF':
            if prog_passes > 5:
                profile_text = f"Regista difensivo: ben {prog_passes} passaggi progressivi. Ha eluso il pressing avversario avviando l'azione con pulizia."
            else:
                profile_text = f"Fase difensiva solida, badando più alla marcatura attenta che alla costruzione dal basso (xT: {xt})."
        elif role == 'MID':
            if passes_box > 3:
                profile_text = f"Dominante negli inserimenti! Ha toccato {passes_box} palloni in area avversaria, creando pericoli costanti (xT: {xt})."
            else:
                profile_text = f"Equilibratore in mezzo al campo. Indice di minaccia (xT) di {xt}, utile a far girare a vuoto la pressione nemica."
        else: # ATT
            if dribbles > 4:
                profile_text = f"Imprendibile nell'uno contro uno! Ha ubriacato i difensori con {dribbles} dribbling riusciti (LBA: {lba})."
            else:
                profile_text = f"Più funzionale alla squadra che brillante palla al piede. Ha lavorato sporco per i compagni (LBA: {lba})."

        return {
            'name': name,
            'is_gk': False,
            'xt': xt,
            'lba': lba,
            'profile': profile_text
        }
