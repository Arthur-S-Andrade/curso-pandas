# %%

import pandas as pd
import numpy as np

# %%

# ------------------------------------------------

# 05.01 - Crie uma coluna nova “twitch_points” que possua como valores o resultado da multiplicação do saldo de pontos e a marcação da twitch

clientes = pd.read_csv("../../data/clientes.csv", sep=";")

clientes["twitch_points"] = clientes["flTwitch"] * clientes["qtdePontos"]

clientes.sample(10)

# %%

# ------------------------------------------------

# 05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova

clientes["log_pontos"] = np.log(clientes["qtdePontos"] + 1) #+ 1 apenas pra tirar os valores de log "-inf" que se referem ao log neperiano de 0

# %%

clientes.head(10)

# %%

# ------------------------------------------------

# 05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.

clientes["flSocial"] = clientes["flTwitch"] | clientes["flEmail"] | clientes["flYouTube"] | clientes["flBlueSky"] | clientes["flInstagram"]

clientes.head()

# %%

# ------------------------------------------------

# 05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?

order_maior = clientes.sort_values("qtdePontos", ascending=False)

order_menor = clientes.sort_values("qtdePontos")

maior = order_maior.iloc[0]["idCliente"]

menor = order_menor.iloc[0]["idCliente"]

print(f"o id do cliente com o maior saldo de pontos é: {maior} \n o id do cliente com menor saldo de pontos é: {menor}")

# %%

# ------------------------------------------------

# 05.05 - Selecione a primeira transação diária de cada cliente

transacoes = pd.read_csv("../../data/transacoes.csv", sep=";")
transacoes = transacoes.sort_values("DtCriacao")

transacoes["data"] = pd.to_datetime(transacoes["DtCriacao"]).dt.date

transacoes.drop_duplicates(keep="first", subset=["IdCliente", "data"])

# %%
