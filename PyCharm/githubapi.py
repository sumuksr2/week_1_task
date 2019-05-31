# The purpose of this program is to look through all GitHub Repositories
# and list out the ones created by a guy called "mojombo".

import requests
import json
import pandas as pd
from pandas.io.json import json_normalize

r = requests.get('https://api.github.com/repositories')
df = pd.DataFrame(r.json())
dfFiltered = df[df['full_name'].str.contains("mojombo")]['name']
print(dfFiltered)

