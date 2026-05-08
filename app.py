import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Roadmap de Dados",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #0f172a;
}
.card {
    padding: 22px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1e293b, #334155);
    color: white;
    margin-bottom: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.25);
}
.badge {
    display: inline-block;
    padding: 5px 12px;
    border-radius: 999px;
    background-color: #38bdf8;
    color: #082f49;
    font-weight: bold;
    margin-bottom: 10px;
}
.topic {
    background-color: rgba(255,255,255,0.08);
    padding: 8px 12px;
    border-radius: 10px;
    margin: 5px 0;
}
.project {
    background-color: rgba(34,197,94,0.15);
    border-left: 4px solid #22c55e;
    padding: 12px;
    border-radius: 10px;
    margin-top: 12px;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Roadmap Interativo para Análise e Engenharia de Dados")
st.write("Um guia visual para estudantes e estagiários que querem evoluir em SQL, BI, Python, Engenharia de Dados e carreira.")

roadmap = [
    {
        "fase": "01",
        "titulo": "Fundamentos",
        "nivel": "Iniciante",
        "area": "Base",
        "cor": "🟢",
        "topicos": ["SQL básico", "JOINs", "GROUP BY", "Excel", "Modelagem inicial"],
        "projeto": "Criar uma análise simples usando SQL + Excel."
    },
    {
        "fase": "02",
        "titulo": "Análise de Dados",
        "nivel": "Iniciante/Intermediário",
        "area": "BI",
        "cor": "🔵",
        "topicos": ["Power BI", "DAX", "KPIs", "Storytelling", "Dashboards"],
        "projeto": "Criar um dashboard com indicadores de negócio."
    },
    {
        "fase": "03",
        "titulo": "Engenharia de Dados",
        "nivel": "Intermediário",
        "area": "Engenharia",
        "cor": "🟣",
        "topicos": ["ETL/ELT", "Data Warehouse", "Staging", "SCD", "Pipelines"],
        "projeto": "Criar um pipeline CSV/API → tratamento → base final."
    },
    {
        "fase": "04",
        "titulo": "Python para Dados",
        "nivel": "Intermediário",
        "area": "Python",
        "cor": "🟡",
        "topicos": ["Pandas", "APIs", "JSON", "Automação", "Streamlit"],
        "projeto": "Criar um app em Streamlit consumindo ou simulando dados."
    },
    {
        "fase": "05",
        "titulo": "Mercado e Portfólio",
        "nivel": "Carreira",
        "area": "Carreira",
        "cor": "🟠",
        "topicos": ["GitHub", "Documentação", "Cloud básica", "LinkedIn", "Projetos"],
        "projeto": "Publicar projetos no GitHub e divulgar no LinkedIn."
    }
]

df = pd.DataFrame(roadmap)

st.sidebar.title("🎛️ Filtros")
area = st.sidebar.selectbox("Área", ["Todas"] + sorted(df["area"].unique()))
nivel = st.sidebar.selectbox("Nível", ["Todos"] + sorted(df["nivel"].unique()))

df_filtrado = df.copy()

if area != "Todas":
    df_filtrado = df_filtrado[df_filtrado["area"] == area]

if nivel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["nivel"] == nivel]

st.sidebar.divider()
st.sidebar.subheader("📈 Progresso estimado")
progresso = st.sidebar.slider("Meu progresso", 0, 100, 25)
st.sidebar.progress(progresso / 100)

st.subheader("🧭 Trilha principal")

cols = st.columns(2)

for i, row in df_filtrado.reset_index(drop=True).iterrows():
    topicos_html = "".join([f"<div class='topic'>✅ {topico}</div>" for topico in row["topicos"]])

    card_html = f"""
    <div class="card">
        <div class="badge">{row['cor']} Fase {row['fase']}</div>
        <h2>{row['titulo']}</h2>
        <p><b>Nível:</b> {row['nivel']}</p>
        <p><b>Área:</b> {row['area']}</p>
        <h4>Tópicos:</h4>
        {topicos_html}
        <div class="project">
            <b>Projeto sugerido:</b><br>
            {row['projeto']}
        </div>
    </div>
    """

    with cols[i % 2]:
        st.markdown(card_html, unsafe_allow_html=True)

st.divider()

tab1, tab2, tab3 = st.tabs(["🚀 Projetos", "📌 Como usar", "🌐 Publicação"])

with tab1:
    st.subheader("Projetos para colocar no portfólio")
    st.write("""
    - Dashboard de indicadores comerciais ou financeiros  
    - Auditoria entre dois sistemas  
    - Pipeline simples com Python e Pandas  
    - App em Streamlit com filtros e cards  
    - Documentação automática de modelo Power BI  
    """)

with tab2:
    st.subheader("Como estudar")
    st.write("""
    Use as fases em ordem.  
    Primeiro fortaleça SQL e modelagem, depois avance para BI, Engenharia, Python e Portfólio.
    """)

with tab3:
    st.subheader("Como publicar")
    st.write("""
    Para publicar grátis, suba este projeto no GitHub e conecte o repositório no Streamlit Community Cloud.
    """)