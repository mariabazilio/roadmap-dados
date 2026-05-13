import streamlit as st

st.set_page_config(
    page_title="Roadmap Dados",
    layout="wide"
)

# ---------------- CSS ----------------
st.markdown("""
<style>

/* FUNDO */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* TITULOS */
h1, h2, h3 {
    color: #e2e8f0;
}

/* TEXTO */
p {
    color: #94a3b8;
}

/* HERO */
.hero {
    background: rgba(30, 41, 59, 0.6);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
}

/* TIMELINE */
.timeline {
    position: relative;
    margin: 40px 0;
}

.timeline::after {
    content: '';
    position: absolute;
    width: 3px;
    background-color: #334155;
    top: 0;
    bottom: 0;
    left: 50%;
}

/* CONTAINER */
.container-tl {
    padding: 10px 40px;
    position: relative;
    width: 50%;
}

.left { left: 0; }
.right { left: 50%; }

/* CARD */
.content {
    background: rgba(30, 41, 59, 0.7);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid #334155;
}

/* TEXTO CARD */
.content p {
    font-size: 14px;
}

/* BOLINHA */
.container-tl::after {
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
    right: -8px;
    background-color: #84cc16;
    border: 3px solid #0f172a;
    top: 20px;
    border-radius: 50%;
}

.right::after {
    left: -8px;
}

/* BOTÃO */
.btn-tl {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 14px;
    background-color: #84cc16;
    color: #020617;
    border-radius: 999px;
    font-size: 13px;
    text-decoration: none;
    font-weight: 600;
}

.btn-tl:hover {
    background-color: #a3e635;
}

/* ABAS */
button[data-baseweb="tab"] {
    color: #cbd5e1;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #84cc16 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
    <h1>🛢 Roadmap de Dados</h1>
    <p>Explore o caminho para se tornar Analista ou Engenheiro de Dados</p>
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

    texto_intro = st.text_area(
        "✍️ Edite a introdução:",
        """Os dados evoluíram desde registros primitivos até Big Data e Inteligência Artificial.

Hoje, são fundamentais para tomada de decisão nas empresas e impulsionam inovação.

Neste roadmap, você verá o caminho completo para se tornar um profissional de dados."""
    )

    st.markdown(f"""
    <div class="content">
        <p>{texto_intro}</p>
    </div>
    """, unsafe_allow_html=True)

# ---------------- FUNÇÃO TIMELINE ----------------
def render_timeline(etapas):

    html = '<div class="timeline">'

    for i, e in enumerate(etapas):
        side = "left" if i % 2 == 0 else "right"

        html += f"""
        <div class="container-tl {side}">
            <div class="content">
                <h3>{e["titulo"]}</h3>
                <p>{e["desc"]}</p>
                <a class="btn-tl" href="{e["link"]}" target="_blank">Saiba mais</a>
            </div>
        </div>
        """

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

# ---------------- CONCEITOS ----------------
with aba2:

    st.title("📈 Conceitos Fundamentais")

    etapas = [
        {"titulo": "Banco de Dados", "desc": "Modelagem, SGBDs e conceitos básicos", "link": "https://www.ev.org.br"},
        {"titulo": "SQL", "desc": "Consultas, joins e manipulação de dados", "link": "https://w3schools.com"},
        {"titulo": "Data Warehouse", "desc": "Fato, dimensão e ETL", "link": "https://youtube.com"},
        {"titulo": "GitLab", "desc": "Versionamento e gestão de tarefas", "link": "https://docs.gitlab.com"}
    ]

    render_timeline(etapas)

# ---------------- ANALISTA ----------------
with aba3:

    st.title("📊 Roadmap Analista de Dados")

    etapas = [
        {"titulo": "Excel", "desc": "Base para análise de dados", "link": "#"},
        {"titulo": "SQL", "desc": "Consulta e manipulação de dados", "link": "#"},
        {"titulo": "Power BI", "desc": "Criação de dashboards", "link": "#"},
        {"titulo": "DAX", "desc": "Cálculos e métricas avançadas", "link": "#"}
    ]

    render_timeline(etapas)

# ---------------- ENGENHEIRO ----------------
with aba4:

    st.title("⚙️ Roadmap Engenheiro de Dados")

    etapas = [
        {"titulo": "Python", "desc": "Manipulação e processamento de dados", "link": "#"},
        {"titulo": "ETL", "desc": "Construção de pipelines de dados", "link": "#"},
        {"titulo": "Data Warehouse", "desc": "Modelagem e armazenamento", "link": "#"},
        {"titulo": "Cloud", "desc": "AWS, Azure ou GCP", "link": "#"}
    ]

    render_timeline(etapas)
