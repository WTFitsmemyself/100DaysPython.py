import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs
from lxml import etree
from lxml.cssselect import CSSSelector

names = []
salary = []
costs = []
rents = []

countries = ["Italy", "Iran", "Norway", "Finland", 'Iraq', 'Mexico', 'France', 'China', 'Sweden']
base_url = "https://www.numbeo.com/cost-of-living/country_result.jsp"

for country in countries:
    name_file = country
    f = open("./countries/" + country + ".html", "w", encoding="utf-8")

    query_param = "?country="+country+"&displayCurrency=USD"
    url = base_url + query_param
    response = requests.get(url)
    soup = Bs(response.content, "html.parser")
    pretty = soup.prettify()

    f.write(str(soup))
    f.close()

    src_lxml = "./countries/" + country + ".html"
    tree = etree.parse(src_lxml)

    name_of_country = tree.xpath("//span[@class='purple_light']/text()")
    cost = tree.xpath("//span[@class='emp_number']/text()")
    salaries = tree.xpath("//span[@class='first_currency']/text()")
    rent = tree.xpath("//span[@class='first_currency']/text()")

    salary_final = list(''.join(map(str.strip, (salaries[-2]))))
    rent_final = list(''.join(map(str.strip, rent[-8])))
    cost_final = list(cost[1])

    items = [salary_final, rent_final, cost_final]
    for item in items:
        if item[-1] == '$':
            item[-1] = ''
        elif item[-2] == '$':
            item[-2] = ''

    str_salary_final = ''.join(map(str.strip, salary_final))
    str_rent_final = ''.join(map(str.strip, rent_final))
    str_cost_final = ''.join(map(str.strip, cost_final))

    names.append(name_of_country[0])
    salary.append(str_salary_final)
    costs.append(str_cost_final)
    rents.append(str_rent_final)

df = pd.DataFrame({
    'City Name': names,
    'Salary': salary,
    'Costs': costs,
    'Rent': rents})

df.to_csv('products.csv', index=False)
