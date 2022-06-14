import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.numbeo.com/cost-of-living/country_result.jsp"
countries = ["Italy", "Iran", "France"]

for i in countries:
    query_parameter = "?country=" + str(i)
    url = base_url + query_parameter
    response = requests.get(url)
    soup = bs(response.content, "html.parser")
    print(soup)
