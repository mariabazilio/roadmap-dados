import streamlit as st

st.set_page_config(
    page_title="Roadmap Dados",
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
    <h1>📊 Roadmap Dados</h1>
    <p>
    O Beabá para quem deseja mergulhar na área e se tornar um
    Analista ou Engenheiro de Dados.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- ABAS ----------
aba1, aba2, aba3, aba4 = st.tabs([
    "🏁 Breve Histórico",
    "🛠️ Conceitos iniciais",
    "📈 Analista",
    "⚙️ Engenheiro"
])

# Breve histótico sobre dados (surgimento e etc)

with aba1:
    st.title("🏁 Introdução ao mundo dos dados")

    st.markdown("""
    A história dos dados é muito mais antiga do que parece. Antes de bancos de dados,
    dashboards e inteligência artificial, as pessoas já registravam informações para contar,
    organizar e tomar decisões.
    
    Segundo a 365 Data Science, há evidências de registros desde **19.000 a.C.**, passando por
    estatísticas de saúde pública, cartões perfurados, armazenamento magnético, bancos relacionais
    e a era da internet. 
    """)

    timeline = [
        {
            "ano": "19.000 a.C.",
            "titulo": "Primeiros registros",
            "texto": "O osso de Ishango é citado como uma das primeiras evidências de contagem e registro de informações.",
            "link": "https://en.wikipedia.org/wiki/Ishango_bone"
        },

        {
            "ano": "1640s",
            "titulo": "Estatísticas de saúde pública",
            "texto": "John Graunt coletou dados sobre mortes em Londres, analisando causas, idade e mortalidade.",
            "link": "https://en.wikipedia.org/wiki/John_Graunt"
        },

        {
            "ano": "1880s",
            "titulo": "Processamento de dados",
            "texto": "Herman Hollerith criou máquinas com cartões perfurados para acelerar o processamento do censo.",
            "link": "https://en.wikipedia.org/wiki/Herman_Hollerith"
        },

        {
            "ano": "1928",
            "titulo": "Armazenamento magnético",
            "texto": "Fritz Pfleumer patenteou a fita magnética, tecnologia que influenciou formas modernas de armazenamento.",
            "link": "https://en.wikipedia.org/wiki/Fritz_Pfleumer"
        },

        {
            "ano": "1960s",
            "titulo": "Banco de dados relacional",
            "texto": "Edgar Codd propôs o modelo relacional, base para tabelas com linhas e colunas.",
            "link": "https://en.wikipedia.org/wiki/Edgar_F._Codd"
        },

        {
            "ano": "1990s até hoje",
            "titulo": "Internet, Big Data e IA",
            "texto": "Com a internet, Google, Big Data, Machine Learning e IA, os dados passaram a ser gerados e usados em escala massiva.",
            "link": "https://www.ibm.com/topics/big-data"
        }
    ]

    for item in timeline:

        st.markdown(f"""
        <div class="step">
            <h2>{item["ano"]} — {item["titulo"]}</h2>
            <p>{item["texto"]}</p>
        </div>
        """, unsafe_allow_html=True)

        st.link_button(
            "📚 Saiba mais",
            item["link"]
        )

        st.markdown("""
        <div class="arrow">↓</div>
        """, unsafe_allow_html=True)

    st.caption(
        "Fonte-base: 365 Data Science — The History of Data: From Ancient Times to Modern Day."
    )

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

# Conceitos gerais comuns pras duas profissões
with aba2:

    st.title("📈 Conceitos primordiais para entrada no mercado")

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

# Analista
with aba3:

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
        
# Engenheiro
with aba4:

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
