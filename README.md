# Projeto Pipeline de Dados IoT - Temperatura

## Descrição do Projeto

Este projeto consiste em um pipeline de dados que processa leituras de temperatura coletadas de dispositivos IoT. Os dados são armazenados em um banco de dados PostgreSQL, rodando dentro de um container Docker, e visualizados em um dashboard interativo desenvolvido com Streamlit e Plotly.

O objetivo é fornecer uma solução completa para ingestão, processamento e análise das temperaturas registradas, facilitando a obtenção de insights relevantes sobre o comportamento dos dispositivos.

---

## Configuração do Ambiente

1. **Docker**: usado para rodar o banco PostgreSQL isoladamente, garantindo portabilidade e facilidade de instalação.  
2. **Python**: linguagem usada para processar os dados e desenvolver o dashboard.  
3. **Bibliotecas Python**: pandas, SQLAlchemy, psycopg2-binary (para conexão com PostgreSQL), streamlit e plotly para visualização.  
4. **Git e GitHub**: controle de versão e armazenamento do código-fonte.

---

## Como executar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie e ative o ambiente virtual Python:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    source venv/bin/activate # Linux/Mac
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Inicie o container PostgreSQL:

    ```bash
    docker run --name postgres-iot -e POSTGRES_PASSWORD=admin123 -e POSTGRES_USER=postgres -e POSTGRES_DB=iot_db -p 5432:5432 -d postgres
    ```

5. Crie a tabela `temperature_readings` e as views no banco (utilize o cliente psql ou PgAdmin).

6. Execute o script Python para carregar os dados CSV no banco.

7. Rode o dashboard Streamlit:

    ```bash
    streamlit run dashboard.py
    ```

Abra o navegador no endereço `http://localhost:8501`.

---

## Explicação das Views SQL

- **avg_temp_por_dispositivo**: calcula a média de temperatura para cada dispositivo IoT, permitindo identificar quais dispositivos operam em faixas térmicas diferentes.

- **leituras_por_hora**: mostra a quantidade de leituras registradas por hora do dia, ajudando a detectar padrões de atividade ou possíveis falhas no envio de dados.

- **temp_max_min_por_dia**: apresenta as temperaturas máxima e mínima registradas por dia, importante para monitorar variações extremas e anomalias.

---

## Insights possíveis a partir dos dados

- Identificar dispositivos que apresentam temperaturas fora do padrão esperado, podendo indicar falhas ou necessidade de manutenção.

- Verificar horários de pico de coleta de dados para otimizar a infraestrutura.

- Analisar variações térmicas diárias para compreender o impacto do ambiente ou operação dos dispositivos.

---
#
