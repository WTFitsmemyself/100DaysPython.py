from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

names = []
salary = []
costs = []
rents = []
driver = webdriver.Chrome("/usr/local/bin/chromedriver")
driver.get("https://www.numbeo.com/cost-of-living/country_result.jsp?country=Italy")

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")
for a in soup.findAll('a', href=True, attrs={'class': 'innerWidth'}):
    name = a.find('div', attrs={'class': 'purple_light'})
    salaries = a.find('div', attrs={'class': 'first_currency'})
    cost = a.find('div', attrs={'class': 'in_other_currency'})
    rent = a.find('div', attrs={'class': 'first_currency'})
    names.append(name.text)
    salary.append(salaries.text)
    costs.append(cost.text)
    rents.append(rent.text)

df = pd.DataFrame({'City Name': names,
                   'Salary': salary,
                   'Cost': costs,
                   'Rent': rents})

df.to_csv('products.csv', index=False, encoding='utf-8')
