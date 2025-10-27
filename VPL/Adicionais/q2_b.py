import pandas as pd
import numpy as np

# Carregando o dataframe
d2 = pd.read_csv('Q2.csv', index_col=0)

# b) Utilizando a função 'dependentes' criada por você no exercício anterior (item a da questão 2),
# verifique se os pares de variáveis (x,y), (y,z) e (x,z) são dependentes no
# conjunto de dados 'd2'. Se necessário, realize alterações em sua função.
#
# Crie três variáveis booleanas para armazenar os resultados:
# - dep_xy: True se x e y são dependentes, False caso contrário.
# - dep_yz: True se y e z são dependentes, False caso contrário.
# - dep_xz: True se x e z são dependentes, False caso contrário.
#
# Cole aqui a sua função 'dependentes' da questão 2a.
# def dependentes(v1, v2, p, df):
#    ...

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


# Escreva o seu código aqui para calcular os valores das três variáveis
dep_xy = dependentes('x', 'y', 'P(X,Y,Z)', d2)
dep_yz = dependentes('y', 'z', 'P(X,Y,Z)', d2)
dep_xz = dependentes('x', 'z', 'P(X,Y,Z)', d2)