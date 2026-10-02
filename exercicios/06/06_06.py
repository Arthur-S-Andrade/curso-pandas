# %%

import pandas as pd

# %%

# Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.head()

# %%

transacoes.groupby(by="IdCliente", as_index=False)["QtdePontos"].describe()

# %%
