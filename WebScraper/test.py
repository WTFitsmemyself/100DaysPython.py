import requests
from lxml import etree
from bs4 import BeautifulSoup


def Xpath(url):
      webPage = requests.get(url)
      Scraping = BeautifulSoup(webPage.content, "html.parser")
      documentObjectModel = etree.HTML(str(Scraping))
      return(documentObjectModel.xpath('/html/body/div[4]/div[2]/ul/li[2]/span').text)


URL = "https://www.numbeo.com/cost-of-living/country_result.jsp?country=Italy"
print(Xpath(URL))