# %%

import pandas as pd

# %%

# Quais são os usuários que mais fizeram transações? Considere os 10 primeiros

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.groupby(by="IdCliente")["IdTransacao"].count().sort_values(ascending=False).head(10)

# %%
