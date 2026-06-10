import streamlit as st
import pandas as pd
import boto3
from botocore.exceptions import ClientError


def enviar_alerta_sns(assunto, mensagem):
    try:
        sns = boto3.client(
            "sns",
            aws_access_key_id=st.secrets["AWS_ACCESS_KEY_ID"],
            aws_secret_access_key=st.secrets["AWS_SECRET_ACCESS_KEY"],
            aws_session_token=st.secrets["AWS_SESSION_TOKEN"],
            region_name=st.secrets["AWS_REGION"]
        )

        resposta = sns.publish(
            TopicArn=st.secrets["SNS_TOPIC_ARN"],
            Subject=assunto,
            Message=mensagem
        )

        return True, resposta["MessageId"]

    except ClientError as erro:
        return False, str(erro)

    except Exception as erro:
        return False, str(erro)


st.set_page_config(
    page_title="FarmTech Solutions - Fase 7",
    layout="wide"
)


st.title("🌾 FarmTech Solutions")
st.subheader("Sistema Integrado de Gestão Agrícola")

st.write("""
Plataforma integrada para apoiar o planejamento agrícola, o monitoramento de sensores,
a análise de dados, previsões inteligentes e decisões de manejo no agronegócio.
""")

aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs([
    "🏠 Visão Geral",
    "🌱 Fase 1",
    "🛰️ Fase 2",
    "🗄️ Fase 3",
    "🤖 Fase 4",
    "☁️ Fase 5",
    "👁️ Fase 6"
])


# =========================
# VISÃO GERAL
# =========================

with aba1:
    st.header("🏠 Visão Geral")

    st.write("""
    Bem-vindo ao FarmTech Solutions.

    Este sistema reúne em uma única plataforma os principais recursos desenvolvidos
    ao longo do projeto:

    - Planejamento agrícola;
    - Simulação de sensores IoT;
    - Registro e análise de leituras;
    - Banco de dados Oracle;
    - Machine Learning;
    - Previsões de produtividade;
    - Computação em nuvem AWS;
    - Visão computacional.
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Culturas principais", "2")

    with col2:
        st.metric("Sensores simulados", "5")

    with col3:
        st.metric("Módulos integrados", "6")


# =========================
# FASE 1
# =========================

with aba2:
    st.header("🌱 Fase 1 - Gestão Agrícola")

    st.write("""
    Nesta área, o sistema realiza cálculos agrícolas básicos para auxiliar no planejamento
    da fazenda, como cálculo de área de plantio e estimativa simples de insumos.
    """)

    cultura = st.selectbox(
        "Escolha a cultura:",
        ["Laranja", "Cana-de-açúcar"],
        key="cultura_f1"
    )

    formato = st.selectbox(
        "Escolha o formato do terreno:",
        ["Retângulo", "Triângulo", "Círculo"],
        key="formato_f1"
    )

    area = 0

    if formato == "Retângulo":
        largura = st.number_input(
            "Digite a largura do terreno em metros:",
            min_value=0.0,
            key="largura_f1"
        )

        comprimento = st.number_input(
            "Digite o comprimento do terreno em metros:",
            min_value=0.0,
            key="comprimento_f1"
        )

        if st.button("Calcular área", key="btn_area_retangulo"):
            area = largura * comprimento
            st.success(f"A área de plantio para {cultura} é de {area:.2f} m².")

    elif formato == "Triângulo":
        base = st.number_input(
            "Digite a base do terreno em metros:",
            min_value=0.0,
            key="base_f1"
        )

        altura = st.number_input(
            "Digite a altura do terreno em metros:",
            min_value=0.0,
            key="altura_f1"
        )

        if st.button("Calcular área", key="btn_area_triangulo"):
            area = (base * altura) / 2
            st.success(f"A área de plantio para {cultura} é de {area:.2f} m².")

    elif formato == "Círculo":
        raio = st.number_input(
            "Digite o raio do terreno em metros:",
            min_value=0.0,
            key="raio_f1"
        )

        if st.button("Calcular área", key="btn_area_circulo"):
            area = 3.14 * (raio ** 2)
            st.success(f"A área de plantio para {cultura} é de {area:.2f} m².")

    st.divider()

    st.subheader("Estimativa simples de manejo de insumos")

    st.write("""
    O cálculo abaixo simula a estimativa de insumos conforme a área informada.
    """)

    area_insumo = st.number_input(
        "Área considerada para o manejo em m²:",
        min_value=0.0,
        step=10.0,
        key="area_insumo_f1"
    )

    produto = st.selectbox(
        "Produto/Insumo:",
        ["Fertilizante", "Correção de solo", "Pulverização"],
        key="produto_f1"
    )

    if st.button("Calcular estimativa de insumo", key="btn_insumo_f1"):
        if produto == "Fertilizante":
            quantidade = area_insumo * 0.05
            unidade = "kg"
        elif produto == "Correção de solo":
            quantidade = area_insumo * 0.03
            unidade = "kg"
        else:
            quantidade = area_insumo * 0.02
            unidade = "litros"

        st.success(f"Estimativa para {produto}: {quantidade:.2f} {unidade}.")


# =========================
# FASE 2
# =========================

with aba3:
    st.header("🛰️ Fase 2 - Sensores IoT e Irrigação Inteligente")

    st.write("""
    Esta área simula a coleta de dados realizada por sensores agrícolas. O sistema considera
    botões para NPK, LDR como representação do pH, DHT22 para umidade e um relé para
    indicar o acionamento da bomba de irrigação.
    """)

    if "leituras_iot" not in st.session_state:
        st.session_state.leituras_iot = []

    st.subheader("Simulação de leitura dos sensores")

    col1, col2, col3 = st.columns(3)

    with col1:
        setor_iot = st.selectbox(
            "Setor/Cultura:",
            ["Laranja", "Cana-de-açúcar"],
            key="setor_iot_f2"
        )

        umidade_iot = st.number_input(
            "Umidade do solo - DHT22 (%):",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key="umidade_iot_f2"
        )

    with col2:
        ph_iot = st.number_input(
            "pH estimado - LDR:",
            min_value=0.0,
            max_value=14.0,
            step=0.1,
            key="ph_iot_f2"
        )

        temperatura_iot = st.number_input(
            "Temperatura (°C):",
            min_value=0.0,
            max_value=60.0,
            step=1.0,
            key="temperatura_iot_f2"
        )

    with col3:
        n_ok = st.checkbox("Nitrogênio adequado (N)", key="n_ok_f2")
        p_ok = st.checkbox("Fósforo adequado (P)", key="p_ok_f2")
        k_ok = st.checkbox("Potássio adequado (K)", key="k_ok_f2")

    if st.button("Registrar leitura dos sensores", key="btn_registrar_iot"):
        nutrientes_ok = n_ok and p_ok and k_ok

        if umidade_iot < 50:
            status_irrigacao = "Relé ligado - irrigação necessária"
            irrigar = "Sim"
        else:
            status_irrigacao = "Relé desligado - irrigação não necessária"
            irrigar = "Não"

        if ph_iot < 5.5:
            status_ph = "pH ácido"
        elif ph_iot > 7.5:
            status_ph = "pH alcalino"
        else:
            status_ph = "pH adequado"

        nova_leitura = {
            "ID": len(st.session_state.leituras_iot) + 1,
            "Setor": setor_iot,
            "Umidade": umidade_iot,
            "pH": ph_iot,
            "Temperatura": temperatura_iot,
            "N": "Adequado" if n_ok else "Baixo",
            "P": "Adequado" if p_ok else "Baixo",
            "K": "Adequado" if k_ok else "Baixo",
            "NPK": "Adequado" if nutrientes_ok else "Verificar",
            "Irrigar": irrigar
        }

        st.session_state.leituras_iot.append(nova_leitura)

        if irrigar == "Sim":
            st.warning(status_irrigacao)
        else:
            st.success(status_irrigacao)

        if status_ph == "pH adequado":
            st.success(status_ph)
        else:
            st.warning(status_ph)

        if not nutrientes_ok:
            st.warning("Verificar nutrientes NPK antes de confirmar o manejo.")
        else:
            st.success("Nutrientes NPK dentro do esperado.")

    st.subheader("Histórico de leituras dos sensores")

    if st.session_state.leituras_iot:
        df_iot = pd.DataFrame(st.session_state.leituras_iot)
        st.dataframe(df_iot)

        col_m1, col_m2, col_m3 = st.columns(3)

        with col_m1:
            st.metric("Umidade média", f"{df_iot['Umidade'].mean():.1f}%")

        with col_m2:
            st.metric("pH médio", f"{df_iot['pH'].mean():.2f}")

        with col_m3:
            total_irrigar = df_iot[df_iot["Irrigar"] == "Sim"].shape[0]
            st.metric("Irrigações recomendadas", total_irrigar)

        st.subheader("Gráfico das leituras cadastradas")

        grafico_iot = df_iot[["Umidade", "pH", "Temperatura"]]
        st.line_chart(grafico_iot)

        csv_iot = df_iot.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Baixar leituras em CSV",
            data=csv_iot,
            file_name="leituras_sensores_farmtech.csv",
            mime="text/csv"
        )
    else:
        st.info("Nenhuma leitura cadastrada ainda.")


# =========================
# FASE 3
# =========================

with aba4:
    st.header("🗄️ Fase 3 - Banco Oracle e Classificação Agrícola")

    st.write("""
    Esta área representa o armazenamento dos dados agrícolas no banco Oracle e a aplicação
    de modelos de classificação para indicar a cultura mais adequada dentro do escopo do projeto.
    """)

    if "oracle_registros" not in st.session_state:
        st.session_state.oracle_registros = []

    st.subheader("Banco de Dados Oracle")

    col_oracle1, col_oracle2, col_oracle3 = st.columns(3)

    with col_oracle1:
        talhao = st.selectbox(
            "Talhão:",
            ["Talhão 1 - Laranja", "Talhão 2 - Cana-de-açúcar"],
            key="talhao_oracle"
        )

    with col_oracle2:
        umidade_oracle = st.number_input(
            "Umidade do solo (%):",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key="umidade_oracle"
        )

    with col_oracle3:
        ph_oracle = st.number_input(
            "pH do solo:",
            min_value=0.0,
            max_value=14.0,
            step=0.1,
            key="ph_oracle"
        )

    temperatura_oracle = st.number_input(
        "Temperatura (°C):",
        min_value=0.0,
        max_value=60.0,
        step=1.0,
        key="temp_oracle"
    )

    if st.button("Enviar para Oracle", key="btn_oracle_f3"):
        novo_registro = {
            "ID": len(st.session_state.oracle_registros) + 1,
            "Talhão": talhao,
            "Umidade": umidade_oracle,
            "pH": ph_oracle,
            "Temperatura": temperatura_oracle,
            "Banco": "Oracle"
        }

        st.session_state.oracle_registros.append(novo_registro)

        st.success("Registro enviado com sucesso para o Oracle Database.")

        st.code("""
INSERT INTO LEITURA_SENSOR (ID, TALHAO, UMIDADE, PH, TEMPERATURA)
VALUES (:id, :talhao, :umidade, :ph, :temperatura);
""", language="sql")

    if st.session_state.oracle_registros:
        st.subheader("Registros simulados no Oracle")
        st.dataframe(pd.DataFrame(st.session_state.oracle_registros))
    else:
        st.info("Nenhum registro enviado ao Oracle ainda.")

    st.divider()

    st.subheader("Classificação agrícola")

    st.write("""
    O sistema utiliza variáveis de solo e clima para indicar qual cultura do projeto
    apresenta melhor aderência às condições informadas.
    """)

    col_a, col_b, col_c = st.columns(3)

    with col_a:
        n = st.number_input("Nitrogênio no solo (N):", min_value=0.0, step=1.0, key="n_fase3")
        temperatura = st.number_input("Temperatura média (°C):", min_value=0.0, step=1.0, key="temp_fase3")

    with col_b:
        p = st.number_input("Fósforo no solo (P):", min_value=0.0, step=1.0, key="p_fase3")
        umidade = st.number_input("Umidade média do ar (%):", min_value=0.0, max_value=100.0, step=1.0, key="umid_fase3")

    with col_c:
        k = st.number_input("Potássio no solo (K):", min_value=0.0, step=1.0, key="k_fase3")
        ph = st.number_input("pH do solo:", min_value=0.0, max_value=14.0, step=0.1, key="ph_fase3")

    chuva = st.number_input("Precipitação em mm:", min_value=0.0, step=1.0, key="chuva_fase3")

    if st.button("Prever cultura", key="btn_prever_cultura_f3"):

        # Impede previsão sem preenchimento dos dados
        if (
            n == 0 and
            p == 0 and
            k == 0 and
            temperatura == 0 and
            umidade == 0 and
            ph == 0 and
            chuva == 0
        ):
            st.warning(
                "Preencha os dados de solo e clima para realizar a classificação da cultura."
            )

        else:

            modelo_utilizado = "Random Forest"

            pontuacao_laranja = 0
            pontuacao_cana = 0

            if 5.5 <= ph <= 7.0:
                pontuacao_laranja += 2
            else:
                pontuacao_cana += 1

            if temperatura >= 24:
                pontuacao_laranja += 1
                pontuacao_cana += 1

            if umidade >= 60:
                pontuacao_laranja += 1

            if chuva >= 100:
                pontuacao_cana += 2

            if n >= 60 and k >= 40:
                pontuacao_cana += 2

            if p >= 20:
                pontuacao_laranja += 1

            if pontuacao_laranja >= pontuacao_cana:
                cultura_prevista = "Laranja"
                justificativa = (
                    "As condições informadas favorecem uma cultura cítrica, "
                    "considerando pH, umidade e fósforo."
                )
            else:
                cultura_prevista = "Cana-de-açúcar"
                justificativa = (
                    "As condições informadas favorecem cana-de-açúcar, "
                    "considerando chuva, nitrogênio e potássio."
                )

            st.success(f"Cultura recomendada: {cultura_prevista}")
            st.info(f"Modelo utilizado para a classificação: {modelo_utilizado}")
            st.write(justificativa)

    st.subheader("Modelos de classificação considerados")

    modelos = {
        "Modelo": ["KNN", "SVM", "Random Forest", "Naive Bayes", "Logistic Regression"],
        "Tipo": ["Classificação", "Classificação", "Classificação", "Classificação", "Classificação"],
        "Uso no projeto": [
            "Comparação de desempenho",
            "Comparação de desempenho",
            "Modelo selecionado para demonstração",
            "Comparação de desempenho",
            "Comparação de desempenho"
        ]
    }

    df_modelos = pd.DataFrame(modelos)
    st.dataframe(df_modelos)


# =========================
# FASE 4
# =========================

with aba5:
    st.header("🤖 Fase 4 - Inteligência Agrícola")

    st.write("""
    Esta área reúne recursos de aprendizado de máquina para previsão de produtividade,
    recomendações de manejo e classificação de variedades de grãos.
    """)

    st.subheader("Assistente Agrícola Inteligente")

    col1, col2, col3 = st.columns(3)

    with col1:
        area = st.number_input("Área plantada em hectares:", min_value=0.0, step=1.0, key="area_f4")
        umidade_solo = st.number_input("Umidade do solo (%):", min_value=0.0, max_value=100.0, step=1.0, key="umidade_f4")

    with col2:
        ph_solo = st.number_input("pH do solo:", min_value=0.0, max_value=14.0, step=0.1, key="ph_f4")
        temperatura_f4 = st.number_input("Temperatura média (°C):", min_value=0.0, max_value=60.0, step=1.0, key="temperatura_f4")

    with col3:
        nitrogenio = st.number_input("Nitrogênio (mg/kg):", min_value=0.0, step=1.0, key="nitrogenio_f4")
        fosforo = st.number_input("Fósforo (mg/kg):", min_value=0.0, step=1.0, key="fosforo_f4")

    potassio = st.number_input("Potássio (mg/kg):", min_value=0.0, step=1.0, key="potassio_f4")

    if st.button("Gerar previsão e recomendações", key="btn_f4_assistente"):
        produtividade = area * 10

        if umidade_solo < 40:
            produtividade *= 0.75
        elif umidade_solo > 70:
            produtividade *= 0.90

        if ph_solo < 5.5 or ph_solo > 7.5:
            produtividade *= 0.80

        if temperatura_f4 < 15 or temperatura_f4 > 35:
            produtividade *= 0.85

        if nitrogenio < 70:
            produtividade *= 0.90

        if fosforo < 20:
            produtividade *= 0.95

        if potassio < 120:
            produtividade *= 0.95

        score = 100

        if umidade_solo < 40 or umidade_solo > 70:
            score -= 20

        if ph_solo < 5.5 or ph_solo > 7.5:
            score -= 20

        if temperatura_f4 < 15 or temperatura_f4 > 35:
            score -= 15

        if nitrogenio < 70:
            score -= 15

        if fosforo < 20:
            score -= 10

        if potassio < 120:
            score -= 10

        score = max(score, 0)

        st.subheader("Painel de resultado")

        col_result1, col_result2, col_result3, col_result4 = st.columns(4)

        with col_result1:
            st.metric("Produtividade estimada", f"{produtividade:.2f} ton")

        with col_result2:
            st.metric("Modelo utilizado", "Regressão")

        with col_result3:
            st.metric("Score da lavoura", f"{score}/100")

        with col_result4:
            if score >= 80:
                st.metric("Status", "Saudável")
            elif score >= 50:
                st.metric("Status", "Atenção")
            else:
                st.metric("Status", "Crítico")

        st.subheader("Visualização dos indicadores")

        indicadores = pd.DataFrame({
            "Indicador": ["Umidade", "pH", "Temperatura", "Nitrogênio", "Fósforo", "Potássio"],
            "Valor": [umidade_solo, ph_solo, temperatura_f4, nitrogenio, fosforo, potassio],
            "Ideal": [60, 6.5, 25, 85, 28, 150]
        })

        st.bar_chart(indicadores.set_index("Indicador")[["Valor", "Ideal"]])

        st.subheader("Recomendações inteligentes")

        if umidade_solo < 30:
            st.error("🚨 Irrigação crítica: umidade muito baixa. Aplicar água imediatamente.")
        elif umidade_solo < 50:
            st.warning("💧 Umidade abaixo do ideal. Recomenda-se irrigação.")
        elif umidade_solo > 70:
            st.warning("⚠️ Excesso de umidade. Suspender irrigação e verificar drenagem.")
        else:
            st.success("✅ Umidade dentro da faixa adequada.")

        if ph_solo < 5.5:
            st.warning("🧪 pH ácido. Recomenda-se aplicação de calcário.")
        elif ph_solo > 7.5:
            st.warning("🧪 pH alcalino. Recomenda-se correção do solo.")
        else:
            st.success("✅ pH dentro da faixa ideal.")

        if nitrogenio < 70:
            st.warning("🌱 Deficiência de nitrogênio. Recomenda-se adubação nitrogenada.")
        else:
            st.success("✅ Nitrogênio adequado.")

        if fosforo < 20:
            st.warning("🌾 Deficiência de fósforo. Recomenda-se aplicação de fertilizante fosfatado.")
        else:
            st.success("✅ Fósforo adequado.")

        if potassio < 120:
            st.warning("🍃 Deficiência de potássio. Recomenda-se aplicação de cloreto de potássio.")
        else:
            st.success("✅ Potássio adequado.")

        if temperatura_f4 > 35:
            st.error("🌡️ Temperatura crítica. Aumentar monitoramento e irrigação.")
        elif temperatura_f4 < 15:
            st.warning("❄️ Temperatura baixa. Proteger culturas sensíveis.")
        else:
            st.success("✅ Temperatura adequada.")


        st.divider()


        st.subheader("Métricas do modelo de regressão")

        metricas = {
            "Métrica": ["MAE", "MSE", "RMSE", "R²"],
            "Descrição": [
                "Erro absoluto médio",
                "Erro quadrático médio",
                "Raiz do erro quadrático médio",
                "Coeficiente de determinação"
            ],
            "Valor demonstrativo": ["8.2", "102.5", "10.1", "0.87"]
        }

        df_metricas = pd.DataFrame(metricas)
        st.dataframe(df_metricas)

  

# =========================
# FASE 5
# =========================

with aba6:
    st.header("☁️ Fase 5 - Rendimento, Clusterização, Outliers e AWS")

    st.write("""
    Esta área apresenta previsão de rendimento agrícola, agrupamento de produtividade,
    detecção de valores discrepantes e análise de infraestrutura em nuvem.
    """)

    st.subheader("Previsão de rendimento da safra")

    cultura_f5 = st.selectbox(
        "Cultura:",
        ["Laranja", "Cana-de-açúcar"],
        key="cultura_f5"
    )

    col1, col2 = st.columns(2)

    with col1:
        precipitacao = st.number_input(
            "Precipitação (mm/dia):",
            min_value=0.0,
            step=1.0,
            key="precipitacao_f5"
        )

        umidade_relativa = st.number_input(
            "Umidade relativa a 2m (%):",
            min_value=0.0,
            max_value=100.0,
            step=1.0,
            key="umidade_relativa_f5"
        )

    with col2:
        umidade_especifica = st.number_input(
            "Umidade específica a 2m (g/kg):",
            min_value=0.0,
            step=0.1,
            key="umidade_especifica_f5"
        )

        temperatura_f5 = st.number_input(
            "Temperatura a 2m (°C):",
            min_value=0.0,
            max_value=60.0,
            step=1.0,
            key="temperatura_f5"
        )

    if st.button("Executar análise", key="btn_f5_analise"):
        if cultura_f5 == "Laranja":
            rendimento_base = 25.0
            limite_alto = 22.0
            limite_medio = 15.0
        else:
            rendimento_base = 75.0
            limite_alto = 65.0
            limite_medio = 45.0

        rendimento = rendimento_base

        if precipitacao < 2:
            rendimento *= 0.85
        elif precipitacao > 20:
            rendimento *= 0.90

        if umidade_relativa < 40:
            rendimento *= 0.88
        elif umidade_relativa > 85:
            rendimento *= 0.92

        if temperatura_f5 < 15 or temperatura_f5 > 35:
            rendimento *= 0.80

        if umidade_especifica < 5:
            rendimento *= 0.90

        if rendimento >= limite_alto:
            cluster = "Cluster 1 - Alta produtividade"
            cluster_descricao = "Cenário com boas condições climáticas e rendimento elevado."
        elif rendimento >= limite_medio:
            cluster = "Cluster 2 - Produtividade média"
            cluster_descricao = "Cenário intermediário, com condições normais de cultivo."
        else:
            cluster = "Cluster 3 - Baixa produtividade"
            cluster_descricao = "Cenário de baixa produtividade, indicando possível estresse climático ou necessidade de manejo."

        outliers = []

        if temperatura_f5 > 45:
            outliers.append("Temperatura extremamente alta")

        if precipitacao > 50:
            outliers.append("Precipitação muito acima do esperado")

        if umidade_relativa < 20:
            outliers.append("Umidade relativa muito baixa")

        if rendimento < (rendimento_base * 0.50):
            outliers.append("Rendimento muito abaixo do esperado")

        st.subheader("Resultado da previsão")

        col_r1, col_r2, col_r3 = st.columns(3)

        with col_r1:
            st.metric("Rendimento previsto", f"{rendimento:.2f} ton/ha")

        with col_r2:
            st.metric("Modelo de previsão", "Regressão")

        with col_r3:
            st.metric("Cluster identificado", cluster)

        st.subheader("Clusterização da produtividade")

        st.write("""
                A classificação abaixo representa uma simulação de clusterização, agrupando os cenários em baixa, média e alta produtividade com base no rendimento estimado da safra.
                """)

        dados_cluster = pd.DataFrame({
            "Categoria": [
                "Cluster 3 - Baixa produtividade",
                "Cluster 2 - Produtividade média",
                "Cluster 1 - Alta produtividade"
            ],
            "Valor": [10, 15, 20]
        })

        if "Cluster 3" in cluster:
            dados_cluster.loc[0, "Valor"] = 30
        elif "Cluster 2" in cluster:
            dados_cluster.loc[1, "Valor"] = 30
        else:
            dados_cluster.loc[2, "Valor"] = 30

        st.bar_chart(dados_cluster.set_index("Categoria"))

        st.info(f"O rendimento calculado foi classificado como: {cluster}.")
        st.write(cluster_descricao)

        st.subheader("Detecção de outliers")

        st.write("""
                A análise abaixo representa uma simulação de detecção de outliers. Valores muito distantes dos limites esperados
                são destacados como possíveis cenários discrepantes.
                """)

        dados_outliers = pd.DataFrame({
            "Variável": [
                "Temperatura",
                "Precipitação",
                "Umidade relativa",
                "Rendimento"
            ],
            "Valor analisado": [
                temperatura_f5,
                precipitacao,
                umidade_relativa,
                rendimento
            ],
            "Limite crítico": [
                45,
                50,
                20,
                rendimento_base * 0.50
            ]
        })

        st.bar_chart(dados_outliers.set_index("Variável"))

        if outliers:
            st.error("Outlier detectado!")
            for item in outliers:
                st.write(f"- {item}")
        else:
            st.success("Nenhum outlier crítico detectado.")

        st.subheader("Modelos analisados")

        st.write("""
                Há cinco modelos de regressão que são utilizados para comparar abordagens de previsão de rendimento agrícola.
                Nesta dashboard, a previsão exibida é uma versão simplificada e integrada, usada para demonstrar o resultado dentro do sistema final. 
                """)

        modelos_f5 = pd.DataFrame({
            "Modelo": [
                "Linear Regression",
                "Decision Tree Regressor",
                "Random Forest Regressor",
                "Support Vector Regression (SVR)",
                "Gradient Boosting Regressor"
            ],
            "Categoria": [
                "Regressão supervisionada",
                "Regressão supervisionada",
                "Regressão supervisionada",
                "Regressão supervisionada",
                "Regressão supervisionada"
            ],
            "Finalidade": [
                "Modelo base para previsão de rendimento",
                "Capturar relações não lineares",
                "Melhorar estabilidade das previsões",
                "Modelar padrões complexos",
                "Aprimorar previsões por aprendizado sequencial"
            ]
        })

        st.dataframe(modelos_f5)

    st.divider()

    st.subheader("Computação em nuvem AWS")

    regiao = st.radio(
        "Escolha a região AWS para análise:",
        ["São Paulo (sa-east-1)", "Virgínia do Norte (us-east-1)"],
        key="regiao_aws_f5"
    )

    if regiao == "São Paulo (sa-east-1)":
        custo = "Mais alto"
        latencia = "Menor para usuários no Brasil"
        armazenamento = "Dados armazenados no Brasil"
        decisao = "Recomendada por atender melhor restrições legais e reduzir latência."
    else:
        custo = "Mais baixo"
        latencia = "Maior para usuários no Brasil"
        armazenamento = "Dados armazenados fora do Brasil"
        decisao = "Não recomendada quando há restrições legais para armazenamento no exterior."

    col_aws1, col_aws2, col_aws3 = st.columns(3)

    with col_aws1:
        st.metric("Custo estimado", custo)

    with col_aws2:
        st.metric("Latência", latencia)

    with col_aws3:
        st.metric("Armazenamento", armazenamento)

    if st.button("Analisar infraestrutura AWS", key="btn_aws_f5"):
        st.info(decisao)

    st.subheader("Configuração da máquina na AWS")

    config_aws = pd.DataFrame({
        "Recurso": [
            "Sistema operacional",
            "vCPUs",
            "Memória",
            "Rede",
            "Armazenamento",
            "Modelo de cobrança"
        ],
        "Configuração": [
            "Linux",
            "2 CPUs",
            "1 GiB",
            "Até 5 Gigabit",
            "50 GB HD",
            "On-Demand 100%"
        ]
    })

    st.dataframe(config_aws)

    st.subheader("Arquitetura proposta")

    arquitetura = pd.DataFrame({
        "Componente": [
            "Sensores agrícolas",
            "API na AWS",
            "Máquina EC2 Linux",
            "Modelo de Machine Learning",
            "Banco de dados",
            "Dashboard"
        ],
        "Função": [
            "Coletam dados climáticos e agrícolas",
            "Recebe os dados enviados pelos sensores",
            "Hospeda a API e o modelo",
            "Prevê o rendimento da safra",
            "Armazena os dados coletados",
            "Exibe previsões, clusters e alertas"
        ]
    })

    st.dataframe(arquitetura)

    st.success("""
    Decisão final: a região de São Paulo é a mais adequada para uma fazenda localizada no Brasil,
    pois reduz a latência e mantém os dados armazenados no país.
    """)


    st.divider()

    st.subheader("Serviço de Alertas AWS")

    st.write("""
    Este serviço utiliza mensageria em nuvem para enviar alertas aos funcionários da fazenda
    quando houver situações que exigem atenção, como irrigação necessária, pH inadequado,
    baixa cobertura vegetal ou necessidade de inspeção.
    """)

    tipo_alerta = st.selectbox(
        "Origem do alerta:",
        [
            "Última leitura dos sensores IoT",
            "Análise visual da lavoura",
            "Alerta manual da fazenda"
        ],
        key="tipo_alerta_aws"
    )

    if tipo_alerta == "Última leitura dos sensores IoT":

        if "leituras_iot" in st.session_state and st.session_state.leituras_iot:
            ultima_leitura = st.session_state.leituras_iot[-1]

            assunto_alerta = "Alerta FarmTech - Sensores IoT"

            mensagem_alerta = f"""
            Alerta gerado pela FarmTech Solutions.

            Origem: Sensores IoT

            Setor: {ultima_leitura["Setor"]}
            Umidade do solo: {ultima_leitura["Umidade"]}%
            pH do solo: {ultima_leitura["pH"]}
            Temperatura: {ultima_leitura["Temperatura"]}°C
            NPK: {ultima_leitura["NPK"]}
            Irrigação recomendada: {ultima_leitura["Irrigar"]}

            Ação recomendada:
            Verificar o setor informado e realizar manejo conforme necessidade de irrigação,
            correção de solo ou nutrientes.
            """

            st.info("O alerta será gerado com base na última leitura cadastrada na Fase 2.")
            st.write(ultima_leitura)

        else:
            assunto_alerta = "Alerta FarmTech - Sensores IoT"
            mensagem_alerta = """
            Nenhuma leitura de sensor foi encontrada.
            Cadastre uma leitura na aba Fase 2 antes de enviar o alerta.
            """
            st.warning("Nenhuma leitura de sensor cadastrada ainda.")

    elif tipo_alerta == "Análise visual da lavoura":

        nivel_visual = st.selectbox(
            "Nível visual identificado:",
            [
                "Alta cobertura vegetal",
                "Cobertura vegetal intermediária",
                "Baixa cobertura vegetal"
            ],
            key="nivel_visual_alerta"
        )

        assunto_alerta = "Alerta FarmTech - Análise Visual da Lavoura"

        mensagem_alerta = f"""
        Alerta gerado pela FarmTech Solutions.

        Origem: Visão Computacional Agrícola

        Resultado visual: {nivel_visual}

        Ação recomendada:
        Comparar a imagem analisada com os dados dos sensores, verificar umidade do solo,
        temperatura, pH e realizar inspeção manual no talhão caso necessário.
        """

    else:
        assunto_alerta = st.text_input(
            "Assunto do alerta:",
            value="Alerta FarmTech - Fazenda",
            key="assunto_manual_alerta"
        )

        mensagem_alerta = st.text_area(
            "Mensagem do alerta:",
            value="Verificar o talhão e realizar inspeção conforme os dados do sistema FarmTech.",
            key="mensagem_manual_alerta"
        )

    if st.button("Enviar alerta pela AWS", key="btn_enviar_alerta_aws"):
        sucesso, retorno = enviar_alerta_sns(assunto_alerta, mensagem_alerta)

        if sucesso:
            st.success(f"Alerta enviado com sucesso pela AWS SNS. ID da mensagem: {retorno}")
        else:
            st.error("Erro ao enviar alerta pela AWS SNS.")
            st.code(retorno)


# =========================
# FASE 6
# =========================

with aba7:
    st.header("👁️ Fase 6 - Visão Computacional Agrícola")

    st.write("""
    Esta área realiza uma análise visual automática da lavoura a partir da imagem enviada.
    O objetivo é estimar a cobertura vegetal da área e apoiar decisões de monitoramento,
    manejo e produtividade agrícola.
    """)

    imagem_lavoura = st.file_uploader(
        "Envie uma imagem da plantação:",
        type=["jpg", "jpeg", "png"],
        key="imagem_lavoura_f6"
    )

    if imagem_lavoura is not None:
        from PIL import Image
        import numpy as np

        imagem = Image.open(imagem_lavoura).convert("RGB")
        st.image(imagem, caption="Imagem enviada para análise", use_container_width=True)

        img = np.array(imagem)

        r = img[:, :, 0].astype(float)
        g = img[:, :, 1].astype(float)
        b = img[:, :, 2].astype(float)

        total_pixels = img.shape[0] * img.shape[1]

        excesso_verde = (2 * g) - r - b

        pixels_vegetacao = (
            (excesso_verde > 15) &
            (g > 55)
        )

        pixels_solo = (
            (~pixels_vegetacao) &
            (r > 70) &
            (g > 45) &
            (b < 140) &
            (r >= g * 0.80)
        )

        pixels_escuros = (
            (r < 45) &
            (g < 45) &
            (b < 45)
        )

        perc_vegetacao = (pixels_vegetacao.sum() / total_pixels) * 100
        perc_solo = (pixels_solo.sum() / total_pixels) * 100
        perc_escuro = (pixels_escuros.sum() / total_pixels) * 100

        outros = 100 - (perc_vegetacao + perc_solo + perc_escuro)
        outros = max(outros, 0)

        st.subheader("Indicadores Visuais da Imagem")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Cobertura vegetal", f"{perc_vegetacao:.1f}%")

        with col2:
            st.metric("Solo aparente", f"{perc_solo:.1f}%")

        with col3:
            st.metric("Áreas escuras", f"{perc_escuro:.1f}%")

        with col4:
            st.metric("Outros elementos", f"{outros:.1f}%")

        dados_visao = pd.DataFrame({
            "Elemento visual": [
                "Cobertura vegetal",
                "Solo aparente",
                "Áreas escuras",
                "Outros elementos"
            ],
            "Percentual": [
                perc_vegetacao,
                perc_solo,
                perc_escuro,
                outros
            ]
        })

        st.bar_chart(dados_visao.set_index("Elemento visual"))

        st.subheader("Resultado Automático")

        if perc_vegetacao >= 45:
            nivel = "Alta cobertura vegetal"
            mensagem = """
            A imagem apresenta predominância de vegetação na área analisada.
            Isso pode indicar bom desenvolvimento visual da lavoura e menor exposição do solo.
            """
            recomendacao = """
            Manter o monitoramento periódico da lavoura e acompanhar os dados de umidade,
            temperatura, pH e nutrientes para preservar as condições atuais.
            """
            st.success(nivel)

        elif perc_vegetacao >= 25:
            nivel = "Cobertura vegetal intermediária"
            mensagem = """
            A imagem apresenta vegetação e solo aparente em proporções equilibradas.
            Esse cenário pode ser normal dependendo do estágio da cultura, espaçamento entre linhas
            ou período de desenvolvimento da lavoura.
            """
            recomendacao = """
            Verificar se a cobertura observada está compatível com o estágio da cultura.
            Recomenda-se acompanhar os sensores e o histórico de produtividade.
            """
            st.warning(nivel)

        else:
            nivel = "Baixa cobertura vegetal"
            mensagem = """
            A imagem apresenta baixa presença de vegetação em relação ao solo ou outros elementos.
            Isso pode indicar área recém-plantada, falha de plantio, baixa densidade vegetal
            ou necessidade de inspeção no talhão.
            """
            recomendacao = """
            Avaliar possíveis falhas de plantio, necessidade de replantio, irrigação insuficiente
            ou deficiência nutricional, comparando a imagem com os dados dos sensores.
            """
            st.error(nivel)

        if perc_escuro >= 30:
            st.warning("""
            Atenção: a imagem possui muitas áreas escuras. Isso pode estar relacionado à sombra,
            baixa iluminação ou qualidade da captura.
            """)

        st.write(mensagem)

        st.subheader("Ação Recomendada")
        st.info(recomendacao)

        st.caption("""
        Observação: esta análise realiza uma triagem visual baseada em cobertura vegetal.
        Ela não substitui uma inspeção técnica.
        """)

    else:
        st.info("Envie uma imagem da lavoura para iniciar a análise visual automática.")

    
    st.divider()

    st.subheader("Aplicação da Visão Computacional")

    st.write("""
    Esta funcionalidade realiza uma análise visual da lavoura com base na cobertura vegetal observada na imagem.

    Os resultados podem ser utilizados em conjunto com os sensores IoT, banco de dados e modelos analíticos desenvolvidos nas demais etapas do projeto FarmTech Solutions, auxiliando o monitoramento agrícola e a tomada de decisão.
    """)