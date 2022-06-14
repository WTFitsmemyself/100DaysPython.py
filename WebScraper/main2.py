# !pip install pandas requests BeautifulSoup4 
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

base_url = "https://www.numbeo.com/cost-of-living/country_result.jsp"
all_pages_reviews = []
contires = ["Italy", "Iran"]


def scraper():
    for i in contires:
        pagewise_reviews = []
        query_parameter = "?country="+str(i)
        url = base_url + query_parameter
        response = requests.get(url)
        soup = bs(response.content, 'html.parser')
        rev_div = soup.findAll("span", attrs={"class", "emp_number"})

    for j in range(len(rev_div)):
        # finding all the p tags to fetch only the review text
        pagewise_reviews.append(rev_div[j].find("span").text)

    for k in range(len(pagewise_reviews)):
        all_pages_reviews.append(pagewise_reviews[k])
        return all_pages_reviews


# Driver code
reviews = scraper()
i = range(1, len(reviews)+1)
reviews_df = pd.DataFrame({'review': reviews}, index=i)
reviews_df.to_csv('reviews.csv', sep='t')
