import streamlit as st

st.set_page_config(
    page_title="Roadmap de Dados",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #f8fbf4;
    background-image: radial-gradient(#b9dc91 1.2px, transparent 1.2px);
    background-size: 22px 22px;
}

.hero {
    background: white;
    padding: 35px;
    border-radius: 28px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
    margin-bottom: 40px;
}

.roadmap {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.phase {
    background: white;
    width: 520px;
    padding: 28px;
    border-radius: 26px;
    text-align: center;
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
    border-top: 8px solid #7cc242;
}

.phase h2 {
    margin: 0;
    color: #111827;
}

.phase p {
    color: #64748b;
}

.connector {
    width: 4px;
    height: 55px;
    background: #d9e8cc;
}

.children {
    display: flex;
    justify-content: center;
    gap: 32px;
    margin-bottom: 35px;
    flex-wrap: wrap;
}

.card {
    background: white;
    width: 290px;
    min-height: 180px;
    padding: 24px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    border-top: 7px solid #3b82f6;
}

.card.orange {
    border-top-color: #f97316;
}

.card.green {
    border-top-color: #22c55e;
}

.card.purple {
    border-top-color: #8b5cf6;
}

.card.yellow {
    border-top-color: #eab308;
}

.card h3 {
    color: #111827;
    margin-bottom: 8px;
}

.card p {
    color: #64748b;
    font-size: 15px;
}

.btn {
    display: inline-block;
    margin-top: 10px;
    padding: 9px 14px;
    background: #111827;
    color: white !important;
    border-radius: 999px;
    text-decoration: none;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>📊 Roadmap Interativo de Dados</h1>
    <p>Da base até análise e engenharia de dados, com links de estudo em cada etapa.</p>
</div>
""", unsafe_allow_html=True)

aba1, aba2, aba3 = st.tabs(["🏁 Introdução", "📈 Roadmap Analista", "⚙️ Roadmap Engenheiro"])

with aba1:
    st.markdown("""
    ## Breve histórico sobre dados

    O uso de dados começou muito antes da tecnologia moderna, com registros comerciais,
    censos, controles financeiros e documentos administrativos. Com a evolução da computação,
    os dados passaram a ser armazenados em bancos digitais e usados para apoiar decisões.

    Hoje, dados são usados para entender clientes, medir resultados, prever cenários,
    automatizar processos e melhorar estratégias de negócio.

    ### Analista x Engenheiro de Dados

    **Analista de Dados:** transforma dados em indicadores, dashboards e insights.

    **Engenheiro de Dados:** constrói pipelines, integrações e estruturas para que os dados cheguem com qualidade.
    """)

with aba2:
    st.markdown("""
    <div class="roadmap">

        <div class="phase">
            <h2>📈 Roadmap Analista de Dados</h2>
            <p>Foco em análise, indicadores, dashboards e tomada de decisão.</p>
        </div>

        <div class="connector"></div>

        <div class="children">
            <div class="card green">
                <h3>1. Fundamentos</h3>
                <p>Excel, lógica, estatística básica e entendimento de negócio.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=excel+para+analise+de+dados" target="_blank">Estudar</a>
            </div>

            <div class="card">
                <h3>2. SQL</h3>
                <p>SELECT, JOIN, GROUP BY, CTEs e funções de janela.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=sql+para+analise+de+dados" target="_blank">Estudar</a>
            </div>
        </div>

        <div class="connector"></div>

        <div class="children">
            <div class="card yellow">
                <h3>3. Power BI</h3>
                <p>Modelagem, relacionamentos, visuais, filtros e publicação.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=power+bi+para+iniciantes" target="_blank">Estudar</a>
            </div>

            <div class="card orange">
                <h3>4. DAX</h3>
                <p>CALCULATE, medidas, contexto de filtro e indicadores.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=dax+power+bi+calculate+contexto+de+filtro" target="_blank">Estudar</a>
            </div>

            <div class="card purple">
                <h3>5. Storytelling</h3>
                <p>Transformar números em explicações úteis para o negócio.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=storytelling+com+dados" target="_blank">Estudar</a>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)

with aba3:
    st.markdown("""
    <div class="roadmap">

        <div class="phase">
            <h2>⚙️ Roadmap Engenheiro de Dados</h2>
            <p>Foco em estrutura, pipelines, bancos, qualidade e integração de dados.</p>
        </div>

        <div class="connector"></div>

        <div class="children">
            <div class="card green">
                <h3>1. SQL Forte</h3>
                <p>Consultas avançadas, performance, índices e otimização.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=sql+avancado+performance" target="_blank">Estudar</a>
            </div>

            <div class="card">
                <h3>2. Python</h3>
                <p>Pandas, requests, APIs, JSON e automações.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=python+pandas+api+dados" target="_blank">Estudar</a>
            </div>
        </div>

        <div class="connector"></div>

        <div class="children">
            <div class="card orange">
                <h3>3. ETL / ELT</h3>
                <p>Extração, transformação, carga, logs e tratamento de erros.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=etl+elt+engenharia+de+dados" target="_blank">Estudar</a>
            </div>

            <div class="card purple">
                <h3>4. Data Warehouse</h3>
                <p>Staging, fato, dimensão, granularidade e camadas de dados.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=data+warehouse+fato+dimensao" target="_blank">Estudar</a>
            </div>

            <div class="card yellow">
                <h3>5. Cloud</h3>
                <p>Data Lake, orquestração, deploy e serviços em nuvem.</p>
                <a class="btn" href="https://www.youtube.com/results?search_query=cloud+para+engenharia+de+dados" target="_blank">Estudar</a>
            </div>
        </div>

    </div>
    """, unsafe_allow_html=True)
