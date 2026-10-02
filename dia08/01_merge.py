# %%

import pandas as pd

# %%

transacoes = pd.read_csv("../data/transacoes.csv", sep=";")

transacoes.head()

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

# %%

transacoes.columns = "IdTransacao", "idCliente", "DtCriacao", "qtdePontos", "DescSistemaOrigem" 

transacoes

# %%

transacoes.merge(right=clientes, how='left', on=['idCliente'], suffixes=["Transacao", "Cliente"])

# %%
