import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs
from lxml import etree
from currency_converter import CurrencyConverter

names = []
salary = []
costs = []
rents = []

countries = ["Italy", "Iran", "Norway", "Finland", 'Iraq', 'Mexico', 'France']
base_url = "https://www.numbeo.com/cost-of-living/country_result.jsp"
c = CurrencyConverter()

for country in countries:
    name_file = country
    f = open("./countries/" + country + ".html", "w", encoding="utf-8")

    query_param = "?country="+country
    url = base_url + query_param
    response = requests.get(url)
    soup = Bs(response.content, "html.parser")

    f.write(str(soup))
    f.close()

    src_lxml = "./countries/" + country + ".html"
    tree = etree.parse(src_lxml)

    name_of_country = tree.xpath("//span[@class='purple_light']/text()")
    cost = tree.xpath("//span[@class='emp_number']/text()")
    salaries = tree.xpath("//span[@class='first_currency']/text()")
    rent = tree.xpath("//span[@class='first_currency']/text()")

    salary_final = ''.join(map(str.strip, (salaries[-2])))
    rent_final = ''.join(map(str.strip, rent[-8]))

    names.append(name_of_country[0])
    salary.append(salary_final)
    costs.append(cost[1])
    rents.append(rent_final)


df = pd.DataFrame({
    'City Name': names,
    'Salary': salary,
    'Costs': costs,
    'Rent': rents})

df.to_csv('products.csv', index=False)
