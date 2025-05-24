# O problema
Você é um(a) profissional encarregado(a) de desenvolver um modelo
preditivo de regressão para prever o valor dos custos médicos individuais
cobrados pelo seguro de saúde.
A base de dados para este desafio pode ser algo como o demonstrado no
exemplo a seguir:

```csv
dade,gênero,imc,filhos,fumante,região,encargos
56,feminino,29.774373714007336,2,sim,sudoeste,31109.88976
3423336
46,masculino,25.857394655216346,1,não,nordeste,26650.7026
46642694
32,masculino,23.014839993647488,0,não,sudoeste,21459.0379
9039332
```

Você precisa apenas alimentá-la com mais informações ou utilizar outra
de sua preferência.
# Tarefas
- Exploração de dados:
    - Carregue a base de dados e explore suas características;
    - Analise estatísticas descritivas e visualize distribuições relevantes.
- Pré-processamento de dados:
    - Realize a limpeza dos dados, tratando valores ausentes (senecessário);

    - Converta variáveis categóricas em formatos adequados para modelagem.
- Modelagem:
    - Crie um modelo preditivo de regressão utilizando uma técnica à sua escolha (por exemplo: Regressão Linear, Árvores de Decisão etc);
    - Divida o conjunto de dados em conjuntos de treinamento e teste.
- Treinamento e avaliação do modelo:
    - Treine o modelo com o conjunto de treinamento.
- Validação estatística:
    - Utilize métricas estatísticas para validar a eficácia do modelo (p-value, intervalos de confiança).
# O que avaliaremos:
- Apresente resultados visuais, como gráficos de previsões vs. valores reais;
- Elabore um relatório que inclua uma análise dos resultados, insights obtidos e validação estatística.
## Observações:
Esperamos que o modelo seja capaz de fazer previsões confiáveis dos custos médicos individuais com base nas características fornecidas.
# Entregável
1. Como entregável, o grupo deve enviar um vídeo junto com o link do github do projeto e o código desenvolvido, apresentando o passo a passo do que foi utilizado, como a fonte de dados e como os modelos foram criados.
2. O vídeo deve estar disponível em uma plataforma como Youtube e deve conter até 10 minutos no máximo.
Qualquer dúvida, não deixe de nos chamar no Discord, lá poderemos tirar suas dúvidas e auxiliar nesta tarefa. Boa sorte!

## Passos
- preparar Dataset
    - dividir em treinamento e validação 20/80
- limpeza dos dados definir as caracteristicas do dataset
- definir método de aprendizado (machine learn - assitido)
- treinar algorítimo
- validar predição