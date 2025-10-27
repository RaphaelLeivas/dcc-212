import pandas as pd
import numpy as np

# DataFrame fornecido no exercício
dados = pd.DataFrame({
    'x': np.array([[0]*4, [1]*4, [2]*4, [3]*4]).flatten(),
    'y': list(range(4))*4,
    'P(X,Y)': [0.05, 0.025, 0.075, 0.1, 0.13, 0.09, 0.15, 0.022, 0.03, 0.046, 0.11, 0.015, 0.010, 0.094, 0.005, 0.048]
})

# a) Considerando o conjunto de dados mostrado acima, crie uma função 
# que retorne 'True' caso as variáveis x e y sejam dependentes ou 'False' caso contrário.


def dependentes(v1, v2, p, df):
    # v1 = string representando o nome da coluna da primeira variável que se deseja verificar (in)dependência
    # v2 = string representando o nome da coluna da segunda variável que se deseja verificar (in)dependência
    # p = string representando o nome da coluna das probabilidades
    # df = dataframe contendo o conjunto de dados
    # P(X,Y) == P(X) * P(Y) para serem independentes (false)
    p_x = df.groupby(v1)[p].sum()
    p_y = df.groupby(v2)[p].sum()

    for _, row in df.iterrows():
        answer = row[p] == p_x[row[v1]] * p_y[row[v2]]
        if answer == False:
            return True

    return False

# CHAMAR FUNÇÃO
print(dependentes('x', 'y', 'P(X,Y)', dados))