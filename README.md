# Pós Tech Challenge FIAP - Fase 1

Este projeto desenvolve um modelo preditivo de regressão para estimar os custos médicos individuais cobrados pelo seguro de saúde, conforme desafio proposto na Fase 1 do Pós Tech da FIAP.

## Integrantes do grupo

- Carlos Adriano
- Daniel Kiluange
- Leonardo Nogueira

## Objetivo

Construir um modelo capaz de prever os encargos médicos a partir das características dos clientes, utilizando técnicas de aprendizado supervisionado.

## Estrutura do Projeto

- `atividade.ipynb`: Notebook principal com todo o passo a passo do desenvolvimento, análise e avaliação do modelo.
- `seguro_saude_dataset_2.csv` e `dataset_.csv`: Bases de dados utilizadas para análise e modelagem.
- `lab.py`: Script auxiliar para testes ou análises adicionais.
- `definitions.md`: Descrição do desafio, tarefas, dicionário de dados e critérios de avaliação.
- `requirements.txt`/`Pipfile`: Dependências do projeto.

## Passos Realizados

1. **Exploração dos Dados**
   - Carregamento e análise das características do dataset.
   - Estatísticas descritivas e visualização das distribuições.

2. **Pré-processamento**
   - Limpeza dos dados e tratamento de valores ausentes.
   - Conversão de variáveis categóricas para formatos numéricos.

3. **Modelagem**
   - Separação dos dados em treino e teste (70/30).
   - Criação de pipeline de pré-processamento e regressão linear.

4. **Treinamento e Avaliação**
   - Treinamento do modelo.
   - Avaliação com métricas: R², MAE, RMSE, MAPE.
   - Visualização dos resultados: gráficos de dispersão e resíduos.

5. **Predição**
   - Exemplo de predição para novos dados.

## Dicionário de Dados

- **idade**: Idade do cliente (numérico)
- **genero**: Gênero (`masculino`, `feminino`)
- **imc**: Índice de Massa Corporal
- **fumante**: Se é fumante (`sim`, `não`)
- **regiao**: Região de residência (`norte`, `nordeste`, `centro-oeste`, `sudeste`, `sul`)
- **encargos**: Valor cobrado pelo seguro (target)

## Como Executar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
2. Abra o arquivo atividade.ipynb no Jupyter ou no VSCode e execute as células sequencialmente.

## Resultados
- O modelo apresenta métricas de desempenho e gráficos comparando valores reais vs. previstos, além de análise dos resíduos.
- O pipeline permite fácil adaptação para novos dados.

## Entregáveis
- Código-fonte do projeto e notebook.
- Vídeo explicativo (até 10 minutos) demonstrando o passo a passo, análise e resultados.

## Referências
- definitions.md: Detalhamento do desafio e critérios de avaliação.
- seguro_saude_dataset_2.csv: Base de dados principal.