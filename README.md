# 📊 Sales Ops Analytics: Otimizando o Funil de Vendas

Olá! Seja bem-vindo(a) ao meu projeto de **Sales Operations & Analytics**. 

Este repositório contém uma solução completa de dados — desde a engenharia até a visualização — simulando um cenário real de **Revenue Operations (RevOps)**. O objetivo foi analisar o ciclo de vida de mais de 50.000 leads, identificar gargalos no funil comercial e fornecer insights acionáveis para escalar a operação.

# Desafio de Negócio

A empresa precisava de respostas claras para direcionar seus esforços de vendas e marketing. Minha missão foi responder:

1.  **Atingimento de Meta:** Estamos batendo a meta de vendas mês a mês?
2.  **Eficiência do Funil:** Onde está o nosso maior gargalo? No agendamento de visitas ou no fechamento?
3.  **Canais de Aquisição:** Qual canal traz mais volume e qual traz a melhor qualidade?
4.  **Saúde da Safra (Cohort):** Como a conversão se comporta ao longo do tempo para cada safra de leads?

---

# Tecnologias e Ferramentas Utilizadas

O projeto foi estruturado seguindo as melhores práticas de Engenharia de Dados e Analytics:

* **Linguagem:** Python (Pandas, Matplotlib, Seaborn, Pathlib).
* **Linguagem de Consulta:** SQL (Sintaxe compatível com BigQuery/SQLite via PandasQL).
* **Ambiente:** Jupyter Notebooks.
* **Engenharia:** Pipelines de ETL, tratamento de nulos, padronização de tipos e deduplicação de dados.
* **Exploração:** Profiling automatizado com YData Profiling.

---

# Estrutura do Projeto

A organização dos diretórios foi pensada para garantir reprodutibilidade e clareza:

```plaintext
├── 📂 data/                  # Dados brutos (Excel) - Input original
├── 📂 processed/             # Dados limpos e transformados (CSV) - Data Mart
├── 📂 notebooks/
│   ├── 01_etl_exploracao.ipynb  # Profiling inicial e entendimento dos dados
│   ├── 02_etl_limpeza.ipynb     # Pipeline de limpeza e tratamento
│   ├── 03_analises.ipynb        # Cálculos de KPIs, Funil e Lógica de Negócio
│   └── 04_dashboard.ipynb       # Visualização de dados e Storytelling
├── 📂 queries/
│   └── analise_safra.sql     # Query SQL avançada para análise de Cohort (Safra)
├── 📂 scripts/
│   └── load_data.py          # Script auxiliar para carregamento robusto de arquivos
└── README.md



# Principais Insights e Resultados
Após processar e cruzar as bases de Leads, Visitas e Contratos, cheguei aos seguintes diagnósticos estratégicos:

1. O Gargalo do Funil 
Identificamos que o maior ponto de atrito está no agendamento de visitas.

Lead → Visita: 17.50% (Taxa crítica identificada).

Visita → Venda: 68.10% (Time de fechamento com alta eficiência).

Conversão Global: 11.91%.

Ação sugerida: Revisar a qualificação dos leads (SDRs) antes de passá-los para agendamento.

2. A Força dos Canais 
Google: Campeão de volume, trazendo cerca de 37% de todos os leads.

Indicação: Apresentou a maior taxa de conversão final, validando a importância de estratégias de member-get-member.

3. Análise de Safra (Cohort Analysis) 
Desenvolvi uma query SQL robusta (analise_safra.sql) que isola o comportamento das safras do segundo semestre de 2024. Isso permitiu calcular a conversão real de cada mês, sem o viés de vendas que ainda não aconteceram (maturação do lead).

Visualizações
O projeto conta com visualizações estratégicas geradas no dashboard.ipynb:

Meta vs. Realizado: Gráfico de eixo duplo combinando barras (valores absolutos) e linha (percentual de atingimento) para monitoramento de metas.

Funil de Conversão: Visualização clássica de funil para identificar a perda de volume entre as etapas.

Performance por Canal: Comparativo de volume e eficiência por origem de tráfego.
