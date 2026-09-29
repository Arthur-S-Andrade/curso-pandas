# %%
import pandas as pd

# %%

# -------------------------------------------------------

#02.01 - quantas linhas há no arquivo clientes.csv

df_clientes = pd.read_csv("../../data/clientes.csv", sep=";")
df_clientes

# %%

linhas = df_clientes.shape[0]

print(f"o arquivo tem {linhas} linhas")

# %%

# -------------------------------------------------------

#02.02 - quantas colunas do tipo int há no arquivo transacoes.csv

df_transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
df_transacoes

# %%

df_transacoes.columns
# %%

df_transacoes.dtypes

# resposta: apenas 1 ("QtdePontos")

# %%

# -------------------------------------------------------

#03.03 - Quantas colunas do tipo string há no arquivo produtos.csv

df_produtos = pd.read_csv("../../data/produtos.csv", sep=";")
df_produtos

# %%

df_produtos.dtypes

# resposta: todas as 4 colunas são do tipo string

# %%

# -------------------------------------------------------

#03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?

df_clientes.loc[4]["idCliente"]

# %%

# -------------------------------------------------------

#03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv?

df_clientes.iloc[9]["qtdePontos"]
