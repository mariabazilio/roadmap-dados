import streamlit as st

st.set_page_config(
    page_title="Roadmap Dados",
    layout="wide"
)

# ---------------- CSS CLEAN ----------------
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* TITULOS */
h1, h2, h3 {
    color: #e2e8f0;
    font-family: 'Segoe UI', sans-serif;
}

/* TEXTO */
p {
    color: #94a3b8;
    font-family: 'Segoe UI', sans-serif;
}

/* HERO */
.big-card {
    background: rgba(30, 41, 59, 0.6);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 25px;
}

/* CARDS */
.step {
    background: rgba(30, 41, 59, 0.6);
    padding: 16px;
    border-radius: 14px;
    border-left: 3px solid #84cc16;
    margin-bottom: 14px;
    transition: 0.2s;
}

.step:hover {
    transform: translateY(-2px);
    border-left: 3px solid #22c55e;
}

/* TITULO CARD */
.step h2 {
    font-size: 18px;
    margin-bottom: 6px;
}

/* TEXTO CARD */
.step p {
    font-size: 14px;
}

/* SETA */
.arrow {
    text-align: center;
    font-size: 22px;
    color: #64748b;
    opacity: 0.6;
}

/* BOTÕES */
.stLinkButton a {
    background-color: #84cc16 !important;
    color: #020617 !important;
    border-radius: 999px !important;
    padding: 6px 14px !important;
    font-size: 13px !important;
    font-weight: 600 !important;
}

.stLinkButton a:hover {
    background-color: #a3e635 !important;
}

/* ABAS */
button[data-baseweb="tab"] {
    color: #cbd5e1;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #84cc16 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="big-card">
    <h1>🛢 Roadmap Dados</h1>
    <p>Guia prático para se tornar Analista ou Engenheiro de Dados</p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABAS ----------------
aba1, aba2, aba3, aba4 = st.tabs([
    "Histórico",
    "Conceitos",
    "Analista",
    "Engenheiro"
])

# ---------------- HISTÓRICO ----------------
with aba1:

    st.title("🏁 Introdução")

    timeline = [
        {"ano": "19.000 a.C.", "titulo": "Primeiros registros"},
        {"ano": "1640", "titulo": "Estatísticas"},
        {"ano": "1880", "titulo": "Cartões perfurados"},
        {"ano": "1928", "titulo": "Fita magnética"},
        {"ano": "1960", "titulo": "Modelo relacional"},
        {"ano": "Hoje", "titulo": "Big Data & IA"},
    ]

    for item in timeline:
        st.markdown(f"""
        <div class="step">
            <h2>{item["ano"]} — {item["titulo"]}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ---------------- CONCEITOS ----------------
with aba2:

    st.title("📈 Conceitos")

    etapas = [
        {
            "titulo": "1. Banco de Dados",
            "descricao": "SGBDs, modelagem e conceitos fundamentais",
            "link_1": "https://www.ev.org.br",
            "link_2": "https://youtube.com",
            "link_3": "https://youtube.com"
        },
        {
            "titulo": "2. SQL",
            "descricao": "Queries, joins e análise",
            "link_1": "https://youtube.com",
            "link_2": "https://w3schools.com",
            "link_3": "https://colab.research.google.com"
        },
        {
            "titulo": "3. Data Warehouse",
            "descricao": "Fatos, dimensões e modelagem",
            "link_1": "https://youtube.com",
            "link_2": "https://youtube.com",
            "link_3": "https://github.com"
        },
        {
            "titulo": "4. GitLab",
            "descricao": "Gestão de tarefas e versionamento",
            "link_1": "https://youtube.com",
            "link_2": "https://docs.gitlab.com",
            "link_3": "https://docs.gitlab.com"
        }
    ]

    for etapa in etapas:

        st.markdown(f"""
        <div class="step">
            <h2>{etapa["titulo"]}</h2>
            <p>{etapa["descricao"]}</p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.link_button("📖", etapa["link_1"])

        with col2:
            st.link_button("🎥", etapa["link_2"])

        with col3:
            st.link_button("💻", etapa["link_3"])

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ---------------- ANALISTA ----------------
with aba3:

    st.title("📊 Analista de Dados")

    etapas = ["Fundamentos", "SQL", "Power BI", "DAX", "Portfólio"]

    for etapa in etapas:

        st.markdown(f"""
        <div class="step">
            <h2>{etapa}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# ---------------- ENGENHEIRO ----------------
with aba4:

    st.title("⚙️ Engenheiro de Dados")

    etapas = ["SQL Avançado", "Python", "ETL", "Data Warehouse", "Cloud"]

    for etapa in etapas:

        st.markdown(f"""
        <div class="step">
            <h2>{etapa}</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)
