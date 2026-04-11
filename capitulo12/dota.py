# %%

import requests
import pandas as pd

url = 'https://api.opendota.com/api/heroes'

resp = requests.get(url)

df = pd.DataFrame(resp.json())
df
# %%

df.to_csv('capitulo12/heroes_dota.csv', sep=';', index=False)