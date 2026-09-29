# %% 

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv", sep = ";")
df

# %%

df["qtdePontos"].astype(float)

# %%

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"])
# %%

df["DtCriacao"].dt.date

# %%
