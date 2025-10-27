import pandas as pd
import numpy as np

# DataFrame fornecido no exercício
dados = pd.DataFrame({
    'x': np.array([[0]*4, [1]*4, [2]*4, [3]*4]).flatten(),
    'y': list(range(4))*4,
    'P(X,Y)': [0.05, 0.025, 0.075, 0.1, 0.13, 0.09, 0.15, 0.022, 0.03, 0.046, 0.11, 0.015, 0.010, 0.094, 0.005, 0.048]
})

print(dados)

# a) Crie uma função para calcular a distribuição de probabilidades de uma
# das variáveis do conjunto de dados mostrado acima. Teste sua função para a variável x.
#
# A função deve se chamar 'distribuicao', retornar uma lista contendo as
# probabilidades e receber os parâmetros:
# > * v = string representando o nome da coluna da variável para a qual se deseja calcular as probabilidades
# > * p = string representando o nome da coluna das probabilidades
# > * df = dataframe contendo o conjunto de dados


def distribuicao(v, p, df):
    # v = string representando o nome da coluna da variável para a qual se deseja calcular as probabilidades
    # p = string representando o nome da coluna das probabilidades
    # df = dataframe contendo o conjunto de dados

    # COMPLETAR FUNÇÃO
    return df.groupby(v)[p].sum()

# CHAMAR FUNÇÃO
print(distribuicao('x', 'P(X,Y)', dados))