import streamlit as st

st.set_page_config(
    page_title="Trilha de aprendizado - Dados",
    layout="wide"
)

# css
# ordem dos steps vem fundo, titulo, formatacao do texto, card principal, card de cada step, hover, setas, botoes, hover do botao, aba, sidebar, linha de separacao
st.markdown("""
<style>

/* FUNDO GERAL */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* TITULOS GERAIS */
h1, h2, h3 {
    color: #b6c2b9;
    font-family: 'Segoe UI', sans-serif;
}

/* TEXTO */
p, li, span, div {
    color: #f8fafc;
    font-family: 'Segoe UI', sans-serif;
}

/* CARD PRINCIPAL */
.big-card {
    background: rgba(30, 41, 59, 0.95);
    padding: 35px;
    border-radius: 24px;
    box-shadow: 0 8px 28px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 25px;
}

/* CARDS DAS ETAPAS */
.step {
    background: rgba(30, 41, 59, 0.92);
    padding: 25px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.22);
    border-left: 6px solid #84cc16;
    margin-bottom: 20px;
    transition: 0.3s;
}

/* HOVER */
.step:hover {
    transform: translateY(-4px);
    border-left: 6px solid #22c55e;
    box-shadow: 0 10px 28px rgba(0,0,0,0.35);
}

/* SETA */
.arrow {
    text-align: center;
    font-size: 42px;
    color: #64748b;
}

/* BOTÕES */
.stLinkButton a {
    background-color: #84cc16 !important;
    color: #0f172a !important;
    border-radius: 999px !important;
    padding: 10px 18px !important;
    font-weight: bold !important;
    border: none !important;
}

/* HOVER BOTAO */
.stLinkButton a:hover {
    background-color: #a3e635 !important;
    color: #020617 !important;
}

/* ABAS */
button[data-baseweb="tab"] {
    color: #cbd5e1;
    font-size: 16px;
    font-weight: 600;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: #84cc16 !important;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* LINHA HORIZONTAL */
hr {
    border-color: rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="big-card">
    <h1>Trilha de aprendizado - Dados</h1>
    <p>
    O passo a passo para quem deseja mergulhar na área e se tornar um
    Analista de Dados.
    </p>
</div>
""", unsafe_allow_html=True)

aba1, aba2, aba3 = st.tabs([
    "Breve Histórico",
    "Conceitos iniciais",
    "Analista",
])

#historico
with aba1:
    st.title("Breve Histórico")

    st.markdown("""
    A história dos dados é muito mais antiga do que parece. Antes de bancos de dados,
    dashboards e ia, as pessoas já registravam informações para contar,
    organizar e tomar decisões.
    
    Há evidências de registros desde **19.000 a.C.**, passando por
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
            "ano": "1640",
            "titulo": "Estatísticas de saúde pública",
            "texto": "John Graunt coletou dados sobre mortes em Londres, analisando causas, idade e mortalidade.",
            "link": "https://en.wikipedia.org/wiki/John_Graunt"
        },

        {
            "ano": "1880",
            "titulo": "A Gênese do processamento de dados",
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
            "ano": "1960",
            "titulo": "Os primórdios do banco de dados relacional",
            "texto": "Edgar Codd propôs o modelo relacional, base para tabelas com linhas e colunas.",
            "link": "https://en.wikipedia.org/wiki/Edgar_F._Codd"
        },

        {
            "ano": "1990 até hoje",
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
            "📖 Saiba mais",
            item["link"]
        )

# conceitos
with aba2:

    st.title("Conceitos")

    etapas = [
        {
            "titulo": "1. Banco de Dados (SGBDS, Conceitos fundamentais e Modelagem)",
            "descricao": "Ao fim desta etapa, você saberá o que é um banco de dados, a diferença entre bancos x sgbds, relacionamentos e implementação/instalação de um banco real",
            "link_1": "https://www.ev.org.br/trilhas-de-conhecimento/banco-de-dados",
            "link_2": "https://www.youtube.com/watch?v=yQkp1Eze400",
            "link_3": "https://www.youtube.com/watch?v=f4jWaYDsho8"
        },
        {
            "titulo": "2. SQL (Funções, Exercícios e demais questões)",
            "descricao": "Ao fim desta etapa, você deverá ter proficiência e capacidade analítica para construção de querys",
            "link_1": "https://www.youtube.com/watch?v=G7bMwefn8RQ",
            "link_2": "https://www.w3schools.com/sql/default.asp",
            "link_3": "https://colab.research.google.com/"
        },
        {
            "titulo": "3. Datawarehouse (Fatos, dimensões e relacionamentos)",
            "descricao": "Ao fim desta etapa, você deverá saber definir um DataWarehouse, diferenciar dimensões e fatos e aplicar relacionamentos corretamente",
            "link_1": "https://www.youtube.com/watch?v=DDKjB2KeXNw&t=1651s",
            "link_2": "https://www.youtube.com/watch?v=kRSykGdHv48",
            "link_3": "https://github.com/mariabazilio/roadmap-dados/blob/main/exercicios_modelagem_dados_v2.pdf"
            
        },
        
        {
            "titulo": "3. GitLab (O que o distingue do Github e suas principais aplicações",
            "descricao": "Ao fim desta etapa, você terá domínio no gerenciamento de tarefas, criação de tasks e demais funções",
            "link_1": "https://www.youtube.com/watch?v=un8CDE8qOR8",
            "link_2": "https://zup.com.br/blog/git-github-e-gitlab/",
            "link_3": "https://docs.gitlab.com/user/"
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
            st.link_button("📖 Conteúdo", etapa["link_1"])

        with col2:
            st.link_button("📚 Aprofundando", etapa["link_2"])

        with col3:
            st.link_button("💻 Na prática", etapa["link_3"]) 

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)

# analista
with aba3:

    st.title("Roadmap Analista de Dados")

    etapas = [
        {
            "titulo": "1. Fundamentos do Power Query (Uso e aplicações)",
            "descricao": "Ao fim desta etapa, você deverá dominar o uso de power query, manipulação e suas funções básicas aplicadas as ferramentas" ,
            "link_1": "https://hub.asimov.academy/blog/power-query-o-que-e-como-usar/",
            "link_2": "https://www.youtube.com/watch?v=SIbi152Vszg",
            "link_3": "https://www.youtube.com/watch?v=s9uxsHmFNFg"
        },

        {
            "titulo": "1. Dax (Linguagem, construções e etc)",
            "descricao": "Ao fim desta etapa, você deverá dominar o uso de power query, manipulação de daxs e funções básicas do excel" ,
            "link_1": "https://www.datacamp.com/pt/tutorial/power-bi-dax-tutorial-for-beginners",
            "link_2": "https://www.youtube.com/watch?v=3UU42GuxCxk",
            "link_3": "https://www.youtube.com/watch?v=KRSmvg8l9U8"
        },

        {
            "titulo": "3. Data Viz (Power BI).",
            "descricao": "Ao fim desta etapa, você saberá desenvolver um dashboard do 0 em Power Bi",
            "link_1": "https://learn.microsoft.com/en-us/power-bi/report-server/install-report-server",
            "link_2": "https://www.datascienceacademy.com.br/course/microsoft-power-bi-para-business-intelligence-e-data-science",
            "link_3": "https://www.datascienceacademy.com.br/course/microsoft-power-bi-para-business-intelligence-e-data-science"
        },

        {
            "titulo": "4. ?",
            "link_1": "",
            "link_2": "",
            "link_3": ""
        },

        {
            "titulo": "5. ?",
            "link_1": "",
            "link_2": "",
            "link_3": ""
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
            st.link_button("📖 Conteúdo", etapa["link_1"])

        with col2:
            st.link_button("📚 Aprofundando", etapa["link_2"])

        with col3:
            st.link_button("💻 Na prática", etapa["link_3"]) 

        st.markdown('<div class="arrow">↓</div>', unsafe_allow_html=True)
        
