import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs
from lxml import etree

names = []
salary = []
costs = []
rents = []

countries = ["Italy", "Iran", "Norway"]
base_url = "https://www.numbeo.com/cost-of-living/country_result.jsp"
f = open("index.html", "w", encoding="utf-8")

for i in countries:
    query_param = "?country="+i
    url = base_url + query_param
    response = requests.get(url)
    soup = Bs(response.content, "html.parser")
    table = soup.find_all("span").text

    print(table)
    f.write(str(soup))

f.close()

df = pd.DataFrame({'City Name': names,
                   'Salary': salary,
                   'Cost': costs,
                   'Rent': rents})
df.to_csv('products.csv', index=False, encoding='utf-8')
