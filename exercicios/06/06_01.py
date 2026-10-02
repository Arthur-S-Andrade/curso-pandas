# %%

import pandas as pd

# %%

# Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

clientes = pd.read_csv("../../data/clientes.csv", sep=";")

clientes.head()

# %%

clientes["socials"] = (clientes["flEmail"] + clientes["flTwitch"] + clientes["flYouTube"] + clientes["flBlueSky"] + clientes["flInstagram"])

clientes

# %%

media = clientes["socials"].mean()
variancia = clientes["socials"].var()
maximo = clientes["socials"].max()

print(f"A média é {media}")
print(f"A variância é {variancia}")
print(f"O máximo é {maximo}")

# %%
