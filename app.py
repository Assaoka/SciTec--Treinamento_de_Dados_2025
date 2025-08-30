import streamlit as st
import pandas as pd

if 'df' not in st.session_state:
    st.session_state['df'] = pd.read_parquet('Indian_Kids_Screen_Time_Optimized.parquet')

pg = st.navigation([
    st.Page("pages/1_Dashboard.py", title="Dashboard", icon="📊"),
    st.Page("pages/2_Adicionar_Dados.py", title="Adicionar Dados", icon="➕"),
    st.Page("pages/3_Filtrar_Planilha.py", title="Filtrar Planilha", icon="🔍"),
])


pg.run()