import streamlit as st

st.set_page_config(page_title="Roadmap Dados", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

h1, h2, h3 {
    color: #e2e8f0;
}

p {
    color: #94a3b8;
}

/* CARD */
.card {
    background: rgba(30, 41, 59, 0.7);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #334155;
    margin-bottom: 15px;
}

/* BOTÃO */
.stLinkButton a {
    background-color: #84cc16 !important;
    color: #020617 !important;
    border-radius: 999px !important;
}

/* LINHA CENTRAL */
.line {
    border-left: 2px solid #334155;
    height: 100%;
    margin: auto;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="card">
    <h1>🛢 Roadmap de Dados</h1>
    <p>Guia prático para Analista e Engenheiro de Dados</p>
</div>
""", unsafe_allow_html=True)

# ---------------- ABAS ----------------
aba1, aba2, aba3, aba4 = st.tabs([
    "Introdução",
    "Conceitos",
    "Analista",
    "Engenheiro"
])

# ---------------- INTRODUÇÃO ----------------
with aba1:

    st.title("🏁 Introdução ao mundo dos dados")

    texto = st.text_area(
        "✍️ Edite a introdução:",
        """Os dados evoluíram desde registros primitivos até Big Data e Inteligência Artificial.

Hoje, são fundamentais para tomada de decisão nas empresas."""
    )

    st.markdown(f'<div class="card"><p>{texto}</p></div>', unsafe_allow_html=True)

    # TIMELINE COM ANOS
    timeline = [
        ("19.000 a.C.", "Primeiros registros"),
        ("1640", "Estatísticas de saúde"),
        ("1880", "Cartões perfurados"),
        ("1928", "Fita magnética"),
        ("1960", "Modelo relacional"),
        ("Hoje", "Big Data e IA"),
    ]

    for ano, texto in timeline:
        st.markdown(f"""
        <div class="card">
            <h3>{ano}</h3>
            <p>{texto}</p>
        </div>
        """, unsafe_allow_html=True)

# ---------------- FUNÇÃO TIMELINE VISUAL ----------------
def timeline_layout(etapas):

    for i, e in enumerate(etapas):

        col1, col2, col3 = st.columns([4,1,4])

        if i % 2 == 0:
            # esquerda
            with col1:
                st.markdown(f"""
                <div class="card">
                    <h3>{e['titulo']}</h3>
                    <p>{e['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.link_button("Saiba mais", e["link"])

            with col2:
                st.markdown('<div class="line"></div>', unsafe_allow_html=True)

        else:
            # direita
            with col2:
                st.markdown('<div class="line"></div>', unsafe_allow_html=True)

            with col3:
                st.markdown(f"""
                <div class="card">
                    <h3>{e['titulo']}</h3>
                    <p>{e['desc']}</p>
                </div>
                """, unsafe_allow_html=True)
                st.link_button("Saiba mais", e["link"])

# ---------------- CONCEITOS ----------------
with aba2:

    st.title("📈 Conceitos")

    etapas = [
        {"titulo": "Banco de Dados", "desc": "Modelagem e SGBDs", "link": "https://www.ev.org.br"},
        {"titulo": "SQL", "desc": "Consultas e joins", "link": "https://w3schools.com"},
        {"titulo": "Data Warehouse", "desc": "Fato, dimensão e ETL", "link": "https://youtube.com"},
        {"titulo": "GitLab", "desc": "Versionamento e tarefas", "link": "https://docs.gitlab.com"},
    ]

    timeline_layout(etapas)

# ---------------- ANALISTA ----------------
with aba3:

    st.title("📊 Analista de Dados")

    etapas = [
        {"titulo": "Excel", "desc": "Base de análise", "link": "#"},
        {"titulo": "SQL", "desc": "Consulta de dados", "link": "#"},
        {"titulo": "Power BI", "desc": "Dashboards", "link": "#"},
        {"titulo": "DAX", "desc": "Métricas avançadas", "link": "#"},
    ]

    timeline_layout(etapas)

# ---------------- ENGENHEIRO ----------------
with aba4:

    st.title("⚙️ Engenheiro de Dados")

    etapas = [
        {"titulo": "Python", "desc": "Manipulação de dados", "link": "#"},
        {"titulo": "ETL", "desc": "Pipelines", "link": "#"},
        {"titulo": "Data Warehouse", "desc": "Modelagem", "link": "#"},
        {"titulo": "Cloud", "desc": "AWS / Azure / GCP", "link": "#"},
    ]

    timeline_layout(etapas)
