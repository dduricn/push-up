# point d'entree de l'application

import streamlit as st 

# pages de navigation des features: 
main_page = st.Page("main_page.py", title="Activité Physique", icon="🏋🏿‍♂️")
page_1 = st.Page("page_1.py", title="Alimentation", icon="🥗")
page_2 = st.Page("page_2.py", title="Statistiques", icon="📊")
#navigation entre les pages 
pg = st.navigation([main_page, page_1, page_2])
st.sidebar.markdown("# affichage des donnees de bases")
# lancer la page 
pg.run() 