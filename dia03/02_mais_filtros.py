# %%

import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv", sep = ";")
df

# %%

filtro = df["IdProduto"].isin(["5","11"])
filtro

# %%

df[filtro]

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")
clientes

# %%

filtro = clientes["DtCriacao"].notna()
filtro

# %%

clientes[filtro]
# %%

teste = ~clientes["DtCriacao"].notna()

# %%
clientes[teste]
# %%
