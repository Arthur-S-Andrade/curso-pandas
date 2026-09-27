# %%

import pandas as pd
import numpy as np

df = pd.read_csv("../data/clientes.csv", sep = ";")
df

# %%

df["pontos_100"] = df["qtdePontos"] + 100

df.head()

# %%

df["qtSocial"] = df["flEmail"] +	df["flTwitch"] +	df["flYouTube"] +	df["flBlueSky"] +	df["flInstagram"]

df


# %%

df["email_e_twitch"] = (df["flEmail"] == 1) * (df["flTwitch"] == 1)

df

# %%

df["email_twitch"] = (df["flEmail"] == 1) | (df["flTwitch"] == 1)

df

# %%

df["email_e_twitch"] = (df["flEmail"] == 1) * (df["flTwitch"] == 1)

df

# %%

df["qtSocial"] = df["flEmail"] +	df["flTwitch"] +	df["flYouTube"] +	df["flBlueSky"] +	df["flInstagram"]

df

# %%

df["flSocial"] = df["flEmail"] |	df["flTwitch"] |	df["flYouTube"] |	df["flBlueSky"] |	df["flInstagram"]

df

# %%

df["todas_social"] = df["flEmail"] *	df["flTwitch"] *	df["flYouTube"] *	df["flBlueSky"] *	df["flInstagram"]

df

# %%

df["qtdePontos"].describe()

# %%

df["logPontos"] = np.log(df["qtdePontos"] +1)

# %%

import matplotlib.pyplot as plt

plt.hist(df["logPontos"])
plt.grid(True)
plt.show()

# %%
