# %%

import pandas as pd

# %%

# -------------------------------------------------------

# 04.01 - Quantos clientes tem vínculo com a Twitch?

df_clientes = pd.read_csv("../../data/clientes.csv", sep=";")

filtro = df_clientes["flTwitch"] == 1

qt_twitch = df_clientes[filtro].shape[0]

print(f"temos {qt_twitch} usuários com a twitch cadastrada")


# %%

# -------------------------------------------------------

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?

filtro = df_clientes["qtdePontos"] > 1000

clientes_mais_1000_pts = df_clientes[filtro].shape[0]

print(f"temos {clientes_mais_1000_pts} clientes com mais de 1000 pontos")

# %%

# -------------------------------------------------------

# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

df_transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")

filtro = (df_transacoes["DtCriacao"] >= "2025-02-01") & (df_transacoes["DtCriacao"] < "2025-02-02")

qt_dia_2025_02_01 = df_transacoes[filtro].shape[0]

print(f"No dia 2025-02-01 tivemos {qt_dia_2025_02_01} transações")


# %%
