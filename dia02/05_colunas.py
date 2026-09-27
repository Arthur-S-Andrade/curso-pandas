# %%

import pandas as pd

df = pd.read_csv("../data/transacoes.csv", sep = ";")
df


# %%

df.shape
# %%

df.info(memory_usage="deep")

# %%

df.dtypes

# %%

df = df.rename(columns={
        "QtdePontos": "QtPontos", "DescSistemaOrigem":"SistemaOrigem"
        })

# %%

renamed_columns={
        "QtdePontos": "QtPontos", "DescSistemaOrigem":"SistemaOrigem"
        }

#df = df.rename(columns=renamed_columns)

#utilizando o inplace=True, não é necessário reatribuir o DataFrame. As alterações são feitas direto no DataFrame original
df.rename(columns=renamed_columns, inplace=True)

# %%

df

# %%

colunas = ["IdCliente", "QtPontos"]

df[colunas]

# %%

colunas = list(df.columns)
colunas.sort()
colunas


# %%

df = df[colunas]
df

# %%
