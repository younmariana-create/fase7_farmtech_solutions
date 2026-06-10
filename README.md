# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<img src="logo-fiap.png" alt="FIAP" border="0" width="40%" height="40%">
</p>

<br>

# FarmTech Solutions

## Grupo FarmTech Solutions

## 👨‍🎓 Integrantes:

- Henrique Honorio da Silva – RM 567102  
- João Victor Matos de Paiva – RM 568345  
- Luiz Frederico Nunes Campêlo – RM 567319  
- Manoella Menezes Weiser – RM 567531  
- Mariana Carvalho Youn – RM 568548 

## 👩‍🏫 Professores:

### Tutor(a)

- Sabrina Otoni

### Coordenador(a)

- André Godoi Chiovato

---

## 📜 Descrição

A FarmTech Solutions é uma plataforma integrada de monitoramento agrícola desenvolvida durante o Projeto de Inteligência Artificial da FIAP.

O objetivo do sistema é auxiliar produtores rurais na coleta, armazenamento, análise e monitoramento de informações da lavoura por meio da integração de diversas tecnologias estudadas ao longo das fases do projeto.

Durante o desenvolvimento foram implementadas funcionalidades relacionadas à gestão agrícola, armazenamento de dados, análise de informações, visão computacional, dashboards interativas e serviços de computação em nuvem.

Na Fase 7 foi realizada a integração de todas as funcionalidades desenvolvidas anteriormente em uma única aplicação construída com Python e Streamlit. Além disso, foi implementado um serviço de mensageria utilizando Amazon SNS, permitindo o envio de alertas automáticos por e-mail aos responsáveis pela fazenda.

Os alertas podem ser gerados a partir de leituras dos sensores IoT, análises visuais da lavoura ou registros manuais realizados pelo usuário. As mensagens enviadas apresentam recomendações de ações corretivas para auxiliar no manejo agrícola e na tomada de decisão.

O sistema demonstra a aplicação prática de conceitos de Inteligência Artificial, Internet das Coisas (IoT), Computação em Nuvem, Banco de Dados, Machine Learning e Visão Computacional em um cenário agrícola.

---

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

* **dados**: arquivos utilizados pelo sistema para armazenamento de informações agrícolas.

* **fase1_gestao_agricola**: estrutura referente às funcionalidades desenvolvidas na Fase 1.

* **fase2_banco_dados**: estrutura referente às funcionalidades desenvolvidas na Fase 2.

* **fase3_machine_learning**: estrutura referente às funcionalidades desenvolvidas na Fase 3.

* **fase4_dashboard_base**: estrutura referente à dashboard inicial desenvolvida na Fase 4.

* **fase5_aws_alertas**: estrutura relacionada à implementação dos serviços AWS.

* **fase6_visao_computacional**: estrutura referente às funcionalidades de análise visual da lavoura.

* **.streamlit**: arquivos de configuração da aplicação Streamlit.

* **app.py**: arquivo principal contendo a integração de todas as fases do projeto.

* **requirements.txt**: lista de dependências necessárias para execução.

* **README.md**: documentação principal do projeto.

---

## 🚀 Funcionalidades Implementadas

### Fase 1 – Gestão Agrícola

* Cadastro de informações agrícolas.
* Monitoramento dos setores da fazenda.
* Controle de indicadores do cultivo.

### Fase 2 – Banco de Dados

* Registro das leituras dos sensores.
* Armazenamento dos dados coletados.
* Consulta das informações cadastradas.

### Fase 3 – Machine Learning

* Processamento dos dados agrícolas.
* Apoio à tomada de decisão.

### Fase 4 – Dashboard

* Interface gráfica desenvolvida com Streamlit.
* Visualização integrada dos dados.

### Fase 5 – AWS

* Configuração do Amazon SNS.
* Criação de tópicos e assinaturas.
* Integração com Python utilizando boto3.

### Fase 6 – Visão Computacional

* Análise visual da lavoura.
* Classificação dos níveis de cobertura vegetal.

### Fase 7 – Integração Final

* Integração das Fases 1, 2, 3, 4, 5 e 6.
* Dashboard única para gerenciamento da fazenda.
* Sistema de alertas automáticos por e-mail utilizando AWS SNS.

---

## ☁️ Serviço de Alertas AWS

Foi implementado um serviço de mensageria utilizando Amazon SNS.

O sistema permite gerar alertas a partir de:

* Leituras dos sensores IoT.
* Resultados da análise visual da lavoura.
* Alertas cadastrados manualmente.

Os alertas são enviados por e-mail aos responsáveis pela fazenda contendo recomendações de ações corretivas para auxiliar no manejo agrícola.

### Evidências da Solução

Inserir nesta seção:

* Print da dashboard principal.
* Print da criação do tópico SNS.
* Print da assinatura confirmada.
* Print do alerta enviado com sucesso.
* Print do e-mail recebido.

---

## 🔧 Como executar o código

### Pré-requisitos

* Python 3.11 ou superior
* Visual Studio Code
* Conta AWS Academy Learner Lab
* Bibliotecas listadas em requirements.txt

### Instalação

Clone o repositório:

```bash
git clone LINK_DO_REPOSITORIO
```

Acesse a pasta do projeto:

```bash
cd FASE7_FARMTECH_SOLUTIONS
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
streamlit run app.py
```

---

## 🎥 Vídeo Demonstrativo

Link do vídeo no YouTube (Não Listado):

INSERIR_LINK_DO_VIDEO

---

## 🗃 Histórico de lançamentos

* 0.7.0 - Junho/2026

  * Integração completa das fases.
  * Implementação do serviço AWS SNS.
  * Dashboard final do projeto.

* 0.6.0

  * Implementação da visão computacional.

* 0.5.0

  * Implementação dos serviços AWS.

* 0.4.0

  * Desenvolvimento da dashboard.

* 0.3.0

  * Implementação dos modelos de análise.

* 0.2.0

  * Estruturação do banco de dados.

* 0.1.0

  * Desenvolvimento da gestão agrícola.

---

# 📋 Licença

<p>
<img style="height:22px;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg">
<img style="height:22px;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg">

MODELO GIT FIAP por FIAP está licenciado sob
<a href="http://creativecommons.org/licenses/by/4.0/">Attribution 4.0 International</a>.
</p>