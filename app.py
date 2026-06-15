import streamlit as st

st.set_page_config(page_title="Sentinela de Brio", page_icon="🛡️")

st.markdown("""
    <style>
    .stApp { background-color: #f0f2f6; }
    div.stButton > button { width: 100%; background-color: #003366; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Sentinela de Brio")
st.write("Bem-vindo, Agente.")

with st.form("relato"):
    id_agente = st.text_input("ID do Efetivo")
    desafio = st.text_area("Desafio enfrentado?")
    decisao = st.text_area("Como o seu brio guiou a decisão?")
    submit = st.form_submit_button("Enviar Relato")

if submit:
    st.success("Relato enviado ao Servidor Central.")
    st.info("Feedback: Sua postura reflete os valores da PNA. Continue com excelência.")
