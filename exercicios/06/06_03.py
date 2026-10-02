# %%

import pandas as pd

# %%

# Qual usuário teve maior quantidade de pontos debitados?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.head()

# %%

filtro = transacoes["QtdePontos"] < 0

transacoes[filtro].groupby(by="IdCliente")["QtdePontos"].sum().sort_values(ascending=True).head(1)

# %%
