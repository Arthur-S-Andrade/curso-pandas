# %%

import pandas as pd

# %%

clientes = pd.read_csv("../data/clientes.csv", sep=";")

clientes.head()

# %%

def get_last_id(x):
    return x.split("-")[-1]

clientes["idCliente"].apply(get_last_id)

# %%
