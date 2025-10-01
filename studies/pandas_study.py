import pandas as pd

ocorrencia_path = '../TP/dados/ocorrencia.csv'    

ocorrencia = pd.read_csv(ocorrencia_path, encoding="latin1", sep=";")
ocorrencia
