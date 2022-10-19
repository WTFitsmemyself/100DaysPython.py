import requests
import pandas as pd
from lxml import html

data_need = []

url = "https://haveibeenpwned.com/PwnedWebsites"
response = requests.get(url)

tree = html.fromstring(response.text)
datas = tree.xpath("//div[@class='col-sm-10']/p[2]/text()[8]")


for data in datas:
    ok_data = data.split(",")
    data_need.append(ok_data)


df = pd.DataFrame({
    'data': data_need})

df.to_csv('dataFile.csv', index=False)
