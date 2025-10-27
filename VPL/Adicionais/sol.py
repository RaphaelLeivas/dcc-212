import pandas as pd

# Sabemos que vários fatores relacionados ao estilo de vida de cada um 
# podem ter um grande impacto no risco de doenças cardiovasculares ou infarto.
# Para este exercício, utilizaremos um banco de dados público dos
# Centros para Controles de Doenças dos Estados Unidos (CDC), que realizou 
# pesquisa em 2015 a respeito dos hábitos de vida de 253.680 americanos.
# Este conjunto de dados possui 22 colunas com dados numéricos,
# em sua maioria categóricos binários (0 para não e 1 para sim).

heart = pd.read_csv('VPL/Adicionais/heart_disease_kaggle.csv')
print(heart.columns)

# b) Qual a probabilidade de um fumante (smoker = 1) ter sofrido ataque cardíaco 
# ou possuir doença cardíaca? E qual a probabilidade para um não fumante?
#
# Armazene os resultados nas variáveis 'prob_fumante' e 'prob_nao_fumante'.

# Escreva seu código aqui
prob_fumante = None

prob_nao_fumante = None