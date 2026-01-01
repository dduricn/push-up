# page de la gestion de l'alimentation 
# bibliotheques 
import streamlit as st
import pandas as pd
from datetime import datetime
from pathlib import Path

# fichier csv brute de donnees 
DATA_FILE = Path("activity_history.csv") 
WEEK_TARGET = 350        # objectif hebdomadaire en pompes
STEP_PUSHUPS = 50        # faire 50 pompes par jour 

def get_current_week_id(): # creation des id_semaine 
    today = datetime.today()
    year, week, weekday = today.isocalendar()
    # weekday: 1 = lundi, ..., 7 = dimanche
    return f"{year}-W{week:02d}", year, week, weekday

def load_data(): # chargement des donnees
    if DATA_FILE.exists():
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["week_id", "year", "week", "pushups"])

def save_data(df): # sauvegarde des donnees
    df.to_csv(DATA_FILE, index=False)

st.markdown(
    "<h1 style='text-align:center;'>Restez actif pour une vie saine</h1>",
    unsafe_allow_html=True
) # titre centré

# algorithme de suivi des pompes
df = load_data()
week_id, year, week, weekday = get_current_week_id()
# créer la ligne de la semaine si besoin
row = df[df["week_id"] == week_id]
if row.empty:
    new_row = {
        "week_id": week_id,
        "year": year,
        "week": week,
        "pushups": 0,
    }
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_data(df)
    row = df[df["week_id"] == week_id]

# gestion des etats de suivi depuis le csv 
if "current_week_pushups" not in st.session_state:
    st.session_state.current_week_pushups = int(row["pushups"].iloc[0])

# --- layout gauche / droite ---
col_left, col_right = st.columns([2, 1])  # 2/3 gauche, 1/3 droite

with col_left:
    # texte semaine + jour
    st.write(f"**Semaine_{week:02d}**")
    st.write(f"Jour {weekday}")

    # bouton Valider -> +50 pompes
    if st.button("+50 Pompes"):
        st.session_state.current_week_pushups += STEP_PUSHUPS
        df.loc[df["week_id"] == week_id, "pushups"] = st.session_state.current_week_pushups
        save_data(df)

    # total 0/350
    current = st.session_state.current_week_pushups
    if current > WEEK_TARGET:
        current = WEEK_TARGET  # pour ne pas dépasser visuellement

    st.write(f"Total hebdomadaire : **{current}/{WEEK_TARGET}**")

    # barre de progression
    st.progress(min(1.0, current / WEEK_TARGET))

with col_right:
    st.markdown(
        """
        <div style='text-align: right; margin-top: 30px;'>
            <img src='https://homefittraining.fr/wp-content/uploads/2021/01/Exercice-animation-pompes-declines-prise-large-avec-gilet-leste-homme.gif'
                 style='width:200px;'>
        </div>
        """,
        unsafe_allow_html=True
    )
