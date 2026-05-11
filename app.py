import streamlit as st

st.set_page_config(
    page_title="Roadmap de Dados",
    page_icon="📊",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>

.stApp {
    background-color: #f8fbf4;
}

.big-card {
    background: white;
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.step {
    background: white;
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    border-top: 8px solid #3b82f6;
    margin-bottom: 20px;
}

.arrow {
    text-align: center;
    font-size: 40px;
    color: #94a3b8;
}

h1, h2, h3 {
    color: #111827;
}

p {
    color: #475569;
}

</style>
""", unsafe_allow_html=True)

# ---------- HERO ----------
st.markdown("""
<div class="big-card">
    <h1>📊 Roadmap Interativo de Dados</h1>
    <p>
    Um guia para quem quer entrar na área de dados e evoluir como
    Analista ou Engenheiro de Dados.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- ABAS ----------
aba1, aba2, aba3 = st.tabs([
    "🏁 Introdução",
    "📈 Analista",
    "⚙️ Engenheiro"
])

# ---------- INTRODUÇÃO ----------
with aba1:

    st.markdown("""
    ## 📚 Breve histórico sobre dados

    Dados existem há séculos, desde censos populacionais e registros comerciais.
    Com a evolução da computação, passaram a ser armazenados digitalmente e usados
    para gerar decisões estratégicas.

    Hoje, empresas usam dados para:
    - entender clientes
    - reduzir custos
    - prever comportamentos
    - automatizar processos
    - melhorar resultados
    """)

    st.markdown("""
    ## ⚖️ Analista x Engenheiro de Dados

    ### 📈 Analista de Dados
    Trabalha com:
    - dashboards
    - indicadores
    - insights
    - análise de negócio

    ### ⚙️ Engenheiro de Dados
    Trabalha com:
    - pipelines
    - bancos de dados
    - ETL
    - integração
    - infraestrutura de dados
    """)

# ---------- ANALISTA ----------
with aba2:

    st.title("📈 Roadmap Analista de Dados")

    etapas = [
        {
            "titulo": "1. Fundamentos",
            "descricao": "Excel, lógica, estatística e negócio",
            "link": "https://www.youtube.com/results?search_query=excel+analise+de+dados"
        },

        {
            "titulo": "2. SQL",
            "descricao": "SELECT, JOIN, GROUP BY e CTE",
            "link": "https://www.youtube.com/results?search_query=sql+analise+de+dados"
        },

        {
            "titulo": "3. Power BI",
            "descricao": "Dashboards, modelagem e KPIs",
            "link": "https://www.youtube.com/results?search_query=power+bi+iniciante"
        },

        {
            "titulo": "4. DAX",
            "descricao": "Medidas, CALCULATE e contexto",
            "link": "https://www.youtube.com/results?search_query=dax+power+bi"
        },

        {
            "titulo": "5. Portfólio",
            "descricao": "Projetos, GitHub e LinkedIn",
            "link": "https://www.youtube.com/results?search_query=portfolio+dados"
        }
    ]

    for etapa in etapas:

        st.markdown(f"""
        <div class="step">
            <h2>{etapa["titulo"]}</h2>
            <p>{etapa["descricao"]}</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("📚 Estudar", etapa["link"])

        st.markdown("""
        <div class="arrow">↓</div>
        """, unsafe_allow_html=True)

# ---------- ENGENHEIRO ----------
with aba3:

    st.title("⚙️ Roadmap Engenheiro de Dados")

    etapas = [
        {
            "titulo": "1. SQL Forte",
            "descricao": "Performance, índices e otimização",
            "link": "https://www.youtube.com/results?search_query=sql+performance"
        },

        {
            "titulo": "2. Python",
            "descricao": "Pandas, APIs e automações",
            "link": "https://www.youtube.com/results?search_query=python+dados"
        },

        {
            "titulo": "3. ETL / ELT",
            "descricao": "Pipelines e tratamento de dados",
            "link": "https://www.youtube.com/results?search_query=etl+engenharia+de+dados"
        },

        {
            "titulo": "4. Data Warehouse",
            "descricao": "Fato, dimensão e staging",
            "link": "https://www.youtube.com/results?search_query=data+warehouse"
        },

        {
            "titulo": "5. Cloud",
            "descricao": "Azure, AWS e Data Lake",
            "link": "https://www.youtube.com/results?search_query=cloud+dados"
        }
    ]

    for etapa in etapas:

        st.markdown(f"""
        <div class="step">
            <h2>{etapa["titulo"]}</h2>
            <p>{etapa["descricao"]}</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button("📚 Estudar", etapa["link"])

        st.markdown("""
        <div class="arrow">↓</div>
        """, unsafe_allow_html=True)
