# %%

import pandas as pd

# %%

# Qual a média de transações / dia?

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

transacoes.head()

# %%

transacoes["dt_dia"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

transacoes

# %%

summary = transacoes.agg({
    "IdTransacao": "count",
    "dt_dia": "nunique",
})

transacoes_dia = summary["IdTransacao"] / summary["dt_dia"]

transacoes_dia

# %%
