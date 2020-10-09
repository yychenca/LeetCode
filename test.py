import pandas as pd
import io
import requests
url="https://www.petrinex.gov.ab.ca/publicdata/API/Files/AB/Vol/2019-01/CSV"
zipfile = ZipFile(io.BytesIO(requests.get(url).content))
filename = list(zipfile.NameToInfo.keys())[0]
f = open(filename,'wb')
f.write(zipfile.open(filename).read())
f.close()

df=pd.read_csv(filename)
df
