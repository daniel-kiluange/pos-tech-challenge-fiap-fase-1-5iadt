# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar o dataset
df = pd.read_csv('dataset_.csv')

# 2. Limpeza dos dados
# Remover linhas com valores ausentes nas colunas principais
df = df.dropna(subset=['idade', 'genero', 'imc', 'filhos', 'fumante', 'regiao', 'encargos'])

# Padronizar valores categóricos
df['genero'] = df['genero'].str.lower().replace({'feminino': 'f', 'masculino': 'm', 'não informado': np.nan})
df['fumante'] = df['fumante'].str.lower().replace({'sim': 1, 'não': 0, 'nao': 0, 'não informado': np.nan})
df['regiao'] = df['regiao'].str.lower().replace({
    'norte': 1, 'nordeste': 2, 'centro-oeste': 3, 'sudoeste': 4, 'sul': 5
})

# Remover linhas com valores categóricos ausentes após padronização
df = df.dropna(subset=['genero', 'fumante', 'regiao'])

# Converter variáveis categóricas em numéricas
df['genero'] = df['genero'].replace({'f': 0, 'm': 1})

# 3. Dividir em treino e validação (20% treino, 80% validação)
X = df[['idade', 'genero', 'imc', 'filhos', 'fumante', 'regiao']]
y = df['encargos']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.8, random_state=42
)

# 4. Treinar o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Validar a predição
y_pred = modelo.predict(X_test)

# 6. Avaliação estatística
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'MSE: {mse:.2f}')
print(f'R²: {r2:.2f}')

# 7. Visualização dos resultados
plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.5)
plt.xlabel('Valores Reais')
plt.ylabel('Previsões')
plt.title('Previsão vs. Valor Real')
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.tight_layout()
plt.show()

# 8. Exibir coeficientes do modelo
coeficientes = pd.DataFrame({
    'Variável': X.columns,
    'Coeficiente': modelo.coef_
})
print('\nCoeficientes do modelo:')
print(coeficientes)

# Observação: Para validação estatística mais avançada (p-value, intervalos de confiança),
# recomenda-se usar statsmodels, mas para regressão básica o scikit-learn já é suficiente.