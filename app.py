import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hub Opella POs", layout="wide", page_icon="🚀")

# ==========================================
# 0. TELA DE LOGIN COM SECRETS
# ==========================================
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔒 Acesso Restrito")
    st.markdown("Bem-vindo ao Hub de Operações da Opella. Por favor, insira a senha para continuar.")
    
    senha = st.text_input("Senha de acesso:", type="password")
    
    if st.button("Entrar"):
        if senha == st.secrets["senha_acesso"]:
            st.session_state.autenticado = True
            st.rerun() 
        else:
            st.error("❌ Senha incorreta. Tente novamente.")
    st.stop()

# ==========================================
# 1. BASE DE DADOS MEGA DETALHADA (Semana 17/08 a 21/08)
# ==========================================
dados_plan = [
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "Ajustes de Cookies no footer", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Status ticket - Falta DFX -Devops"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "Ajustes Termos e Condições", "Owner": "Fred", "Deadline": "21/08", "Status": "Done", "Comentário": "Finalizado"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "NVG | Ajustar UX da Home", "Owner": "Fred", "Deadline": "21/08", "Status": "Done", "Comentário": "Mexemos na semana do dia 11/08 - Talvez perdemos"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "NVG | Alterar para Pop up de Flash", "Owner": "Fred", "Deadline": "21/08", "Status": "Done", "Comentário": "Feito dia 11 também"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "NVG | Grupo 7 Schemas", "Owner": "Ju", "Deadline": "21/08", "Status": "Done", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "DFX | Grupo 5 Schemas", "Owner": "Ju", "Deadline": "21/08", "Status": "Done", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "DFX | Arrumar H1 da Home", "Owner": "Ju", "Deadline": "21/08", "Status": "Done", "Comentário": "Mexemos na semana do dia 11/08 - Talvez perdemos"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "TGF | Página de Superioridade (Checar se perdemos progresso)", "Owner": "Visco", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Mexemos na semana do dia 11/08 - Talvez perdemos"},
    {"Semana": "17/08 a 21/08", "Épico": "Ajustes Gerais", "Task": "TGF | Dois Artigos", "Owner": "Ju", "Deadline": "21/08", "Status": "Done", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "Atualizar schema e o resto de artigos [NVG]", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Grupo 07"},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "Mensagem de acompanhamento assícrona", "Owner": "Fred", "Deadline": "21/08", "Status": "Ongoing", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "Hub de Kids", "Owner": "Fred", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Enviado para validação"},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "NVG | Alterar vídeo de pdp de Flash", "Owner": "Ju", "Deadline": "21/08", "Status": "To do", "Comentário": "Aguardando envierem o vídeo"},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "Atualizar banners", "Owner": "Ju", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "Planejamento de Q4", "Owner": "Visco", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Novalgina", "Task": "QBR", "Owner": "Visco", "Deadline": "21/08", "Status": "Done", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "Atualizar schema e o resto de artigos [DFX]", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Grupo 5 malu terminou"},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "Mensagem de acompanhamento assícrona", "Owner": "Fred", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "Quiz de Superioridade", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Aguardando pilar montar texto"},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "Farroupilha", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Enviada para validação - é prioridade"},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "Planejamento de Q4", "Owner": "Visco", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Dorflex", "Task": "QBR", "Owner": "Visco", "Deadline": "21/08", "Status": "Done", "Comentário": "Faltam alguns detalhes"},
    {"Semana": "17/08 a 21/08", "Épico": "Targifor", "Task": "Refatoração do Quiz", "Owner": "Visco", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "V1 enviada, aguardando validação"},
    {"Semana": "17/08 a 21/08", "Épico": "Targifor", "Task": "Página de Superioridade", "Owner": "Fred", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Oscal", "Task": "Desenvolvimento", "Owner": "Ju", "Deadline": "21/08", "Status": "Done", "Comentário": "Ajustes finais"},
    {"Semana": "17/08 a 21/08", "Épico": "Oscal", "Task": "Incluir e-mail do sac", "Owner": "Ju", "Deadline": "21/08", "Status": "To do", "Comentário": "sac@opella.com"},
    {"Semana": "17/08 a 21/08", "Épico": "Oscal", "Task": "Oscal errado na pdp", "Owner": "Ju", "Deadline": "21/08", "Status": "To do", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Oscal", "Task": "Plano de redirecionamento", "Owner": "Fred", "Deadline": "21/08", "Status": "Ongoing", "Comentário": "Aguardar novas URL's"},
    {"Semana": "17/08 a 21/08", "Épico": "Publicação de Artigos", "Task": "Artigos da semana", "Owner": "Ju", "Deadline": "21/08", "Status": "Ongoing", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Publicação de Artigos", "Task": "Criar Brand Requests e Artigos", "Owner": "Ju", "Deadline": "21/08", "Status": "To do", "Comentário": "Criar épico de Artigos e Brand Requests"},
    {"Semana": "17/08 a 21/08", "Épico": "Chatbot", "Task": "Acompanhar DPR", "Owner": "Visco", "Deadline": "14/08", "Status": "Ongoing", "Comentário": ""},
    {"Semana": "17/08 a 21/08", "Épico": "Chatbot", "Task": "Desenvolvimento", "Owner": "Visco", "Deadline": "14/08", "Status": "Ongoing", "Comentário": ""}
]

df_plan = pd.DataFrame(dados_plan)

# Funções de cor para a tabela ficar bonita
def colorir_status_planilha(val):
    if val == 'Done': return 'background-color: #d4edda; color: #155724; font-weight: bold' # Verde
    elif val == 'Ongoing': return 'background-color: #fff3cd; color: #856404; font-weight: bold' # Amarelo
    elif val == 'To do': return 'background-color: #f8d7da; color: #721c24; font-weight: bold' # Vermelho
    return ''

# (Os outros dataframes de Contatos e Turma mantive simplificados pro código não ficar gigante, 
#  mas o foco é mostrar a aba 1 parruda)
df_times = pd.DataFrame({
    "Marca": ["Dorflex", "Novalgina", "Targifor", "Oscal"],
    "Pessoa": ["Yisell Castillo", "Juliana Mendes", "Samia Ghani", "João Trevisan"],
    "Cargo": ["Head", "Head", "Head", "Manager"]
})
df_turma = pd.DataFrame({"Data": ["25/08"], "Zé (Infra/Chatbot)": ["Retornar ao Chatbot em breve"]})

# ==========================================
# 2. INTERFACE 
# ==========================================
col_title, col_logout = st.columns([8, 1])
with col_title:
    st.title("🚀 Hub de Operações - POs Opella")
with col_logout:
    if st.button("🚪 Sair"):
        st.session_state.autenticado = False
        st.rerun()

st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📋 Planejamento Detalhado", "👥 Contatos", "💻 Outras Abas"])

# ==========================================
# ABA 1 - O PLANEJAMENTO REAL
# ==========================================
with tab1:
    st.markdown("### 📅 Sprints e Visão Tática (Semana 17/08 a 21/08)")
    
    # Grid de Filtros
    c1, c2, c3 = st.columns(3)
    with c1:
        epico_sel = st.selectbox("🏷️ Filtrar por Épico:", ["Todos"] + df_plan["Épico"].unique().tolist())
    with c2:
        owner_sel = st.selectbox("👤 Filtrar por Responsável:", ["Todos"] + df_plan["Owner"].unique().tolist())
    with c3:
        status_sel = st.selectbox("📌 Filtrar por Status:", ["Todos"] + df_plan["Status"].unique().tolist())
    
    # Aplica os filtros
    df_plan_filt = df_plan.copy()
    if epico_sel != "Todos": df_plan_filt = df_plan_filt[df_plan_filt["Épico"] == epico_sel]
    if owner_sel != "Todos": df_plan_filt = df_plan_filt[df_plan_filt["Owner"] == owner_sel]
    if status_sel != "Todos": df_plan_filt = df_plan_filt[df_plan_filt["Status"] == status_sel]
    
    st.markdown(f"**Exibindo {len(df_plan_filt)} tarefas:**")
    
    # Renderiza a tabela com o CSS de cores que criamos lá em cima!
    st.dataframe(
        df_plan_filt.style.map(colorir_status_planilha, subset=['Status']),
        use_container_width=True,
        hide_index=True,
        height=600 # Deixa a tabela mais alta pra caber tudo sem apertar
    )

with tab2:
    st.subheader("Estrutura do Time")
    st.dataframe(df_times, use_container_width=True, hide_index=True)

with tab3:
    st.subheader("Tasks da Turma e Cronogramas")
    st.info("O foco da visualização agora foi aprimorado na aba 1. As demais abas mantiveram a estrutura anterior.")
