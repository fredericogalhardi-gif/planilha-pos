import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hub Opella POs", layout="wide", page_icon="🚀")

# ==========================================
# 1. BASE DE DADOS EMBUTIDA (Simulando as abas)
# ==========================================

# Dados: Planejamento
df_plan = pd.DataFrame([
    {"Semana": "15/08 a 19/08", "Épico": "Novalgina", "Task": "Hub de Kids", "Owner": "Fred", "Deadline": "21/08", "Status": "Ongoing"},
    {"Semana": "15/08 a 19/08", "Épico": "Dorflex", "Task": "Quiz de Superioridade", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing"},
    {"Semana": "25/08 a 29/08", "Épico": "Ajustes Gerais", "Task": "Ajustes Termos e Condições", "Owner": "Fred", "Deadline": "21/08", "Status": "Done"},
    {"Semana": "01/09 a 05/09", "Épico": "Novalgina", "Task": "Atualizar schema e o resto de artigos", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing"},
    {"Semana": "08/09 a 12/09", "Épico": "Targifor", "Task": "Página de Superioridade", "Owner": "Visco", "Deadline": "21/08", "Status": "Ongoing"}
])

# Dados: Contatos (Times das Marcas)
df_times = pd.DataFrame({
    "Marca": ["Dorflex", "Dorflex", "Novalgina", "Novalgina", "Targifor", "Oscal"],
    "Pessoa": ["Yisell Castillo", "Juliana Oliveira", "Juliana Mendes", "Emylaine Silva", "Samia Ghani", "João Trevisan"],
    "Cargo": ["Head", "Manager", "Head", "Analista", "Head", "Manager"]
})

# Dados: Tasks Turma
df_turma = pd.DataFrame({
    "Data": ["25/08", "30/08", "03/07", "15/07"],
    "Zé (Infra/Chatbot)": ["Retornar ao Chatbot em breve", "Retornar ao Chatbot em breve", "Central de cookies", "NVG Flash"],
    "Henrique (Artigos/CMS)": ["Artigos 01 e 02 em Monet", "Artigos da semana", "Ajustes finais Oscal", "Possíveis Artigos"],
    "Malu (Targifor)": ["Artigo TGF em Breve", "Atualizar Schemas com Chico", "Terminou ajustes oscal", "-"],
    "Dan (Kids/Farroupilha)": ["Após isso Flash NVG", "On Hold até superioridade TGF", "Situação chata rolando aqui", "Fazendo hub de kids"]
})

# Dados: Artigos (Agosto 2026)
df_artigos = pd.DataFrame([
    {"Marca": "Dorflex", "Artigo": "Artigo 16", "Status": "Aprovado"},
    {"Marca": "Dorflex", "Artigo": "Artigo 17", "Status": "Em aprovação"},
    {"Marca": "Dorflex", "Artigo": "Artigo 18", "Status": "Produção"},
    {"Marca": "Novalgina", "Artigo": "Artigo 17", "Status": "Ajustes"},
    {"Marca": "Targifor", "Artigo": "Artigo 6", "Status": "Aprovado"},
    {"Marca": "Oscal", "Artigo": "Artigo tal tal tal", "Status": "Deployado"}
])

# ==========================================
# 2. INTERFACE E ABAS
# ==========================================
st.title("🚀 Hub de Operações - POs Opella")
st.markdown("---")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📋 Planejamento", "👥 Contatos", "📅 Cronograma", "💻 Tasks Turma", "📝 Artigos (Agosto)"])

with tab1:
    st.subheader("Visão Tática e Sprints")
    col1, col2 = st.columns(2)
    with col1:
        epico_sel = st.selectbox("🏷️ Filtrar por Épico:", ["Todos"] + df_plan["Épico"].unique().tolist())
    with col2:
        status_sel = st.selectbox("📌 Filtrar por Status:", ["Todos"] + df_plan["Status"].unique().tolist())
    
    df_plan_filt = df_plan.copy()
    if epico_sel != "Todos": df_plan_filt = df_plan_filt[df_plan_filt["Épico"] == epico_sel]
    if status_sel != "Todos": df_plan_filt = df_plan_filt[df_plan_filt["Status"] == status_sel]
    
    st.dataframe(df_plan_filt, use_container_width=True, hide_index=True)

with tab2:
    st.subheader("Estrutura do Time")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("**Stakeholders:**\n\n🇧🇷 Brasil: Leonora")
        st.success("**Time Publicis:**\n\nBeatriz Pedroso (Exec. Business Director)\n\nRenata Carvalho\n\nMayara Nascimento\n\nMatheus Reis")
    with col2:
        st.dataframe(df_times, use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Cronograma Q1/Q2/Q3 2026")
    st.warning("Aqui podemos evoluir para um Gráfico de Gantt, mas o ideal é termos as datas de início e fim cravadas para cada projeto (como Hub de Kids e Landing Page Farroupilha).")

with tab4:
    st.subheader("Backlog Técnico (Turma)")
    st.dataframe(df_turma, use_container_width=True, hide_index=True)

with tab5:
    st.subheader("Status de Publicação - Agosto 2026")
    
    # Adicionando cores automáticas para o status
    def colorir_status(val):
        if val == 'Aprovado' or val == 'Deployado': return 'color: green; font-weight: bold'
        elif val == 'Em aprovação': return 'color: orange; font-weight: bold'
        elif val == 'Ajustes': return 'color: red; font-weight: bold'
        return ''
    
    st.dataframe(df_artigos.style.applymap(colorir_status, subset=['Status']), use_container_width=True, hide_index=True)
