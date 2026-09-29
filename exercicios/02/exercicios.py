# %%
#leia o arquivo transacoes.csv com a formatação correta;
#adicione uma coluna com valores 1;
#salve o dataframe com nome: transacoes_1

import pandas as pd

# %%

df = pd.read_csv("../../data/transacoes.csv", sep=";")
df


# %%

df["valores_1"] =  1
df

# %%
df.to_csv("transacoes_1.csv", index=False)

# %%
