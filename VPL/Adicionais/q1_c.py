import pandas as pd
import numpy as np

# DataFrame fornecido no exercício
dados = pd.DataFrame({
    'x': np.array([[0]*4, [1]*4, [2]*4, [3]*4]).flatten(),
    'y': list(range(4))*4,
    'P(X,Y)': [0.05, 0.025, 0.075, 0.1, 0.13, 0.09, 0.15, 0.022, 0.03, 0.046, 0.11, 0.015, 0.010, 0.094, 0.005, 0.048]
})

# c) Crie uma função que retorne a probabilidade de uma das variáveis 
# ser maior que um valor passado como parâmetro. Teste sua função para o caso P(X>1).


def probabilidade_maior_que(v, a, p, df):
    # v = string representando o nome da coluna da variável que se deseja calcular as probabilidades 
    # a = valor ao qual a variável v deve ser superior
    # p = string representando o nome da coluna das probabilidades
    # df = dataframe contendo o conjunto de dados
    
    # COMPLETAR FUNÇÃO
    # P_v = df.groupby(v)[p].sum()
    # return P_v[P_v > a].sum()
    return df[df[v] > a][p].sum()

# CHAMAR FUNÇÃO
print(probabilidade_maior_que('x', 1, 'P(X,Y)', dados))