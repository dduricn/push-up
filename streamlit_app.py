# point d'entree de l'application

import streamlit as st 

# pages de navigation des features: 
main_page = st.Page("main_page.py", title="Activité Physique", icon="🏋🏿‍♂️")
page_1 = st.Page("page_1.py", title="Alimentation", icon="🥗")
page_2 = st.Page("page_2.py", title="Statistiques", icon="📊")
#navigation entre les pages 
pg = st.navigation([main_page, page_1, page_2])
with st.sidebar: # modification de la side bar pour le profil utilisateur. 
    st.markdown("# Profil")

    poids = st.number_input("Poids (kg)", min_value=0.0, step=0.1)
    taille = st.number_input("Taille (cm)", min_value=0.0, step=0.5)
    age = st.number_input("Âge", min_value=0, step=1)
    objectif = st.text_input("Objectif (ex: perte de poids)")
    imc = st.text_input("IMC")
    masse_osseuse = st.text_input("Masse osseuse")
    masse_musculaire = st.text_input("Masse musculaire")
    masse_graisseuse = st.text_input("Masse graisseuse")
    masse_hydrique = st.text_input("Masse hydrique")
    # mise a jour du profil utilisateur. 
    if st.button("Mettre à jour le profil"):
        st.success("Profil mis à jour.")
# lancer la page 
pg.run() 