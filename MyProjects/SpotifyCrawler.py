from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
from datetime import date, timedelta

dates = []
url_list = []
final = []

# map site
url = "https://spotifycharts.com/regional/us/daily/"
start_date = date(2019, 9, 1)
end_date = date(2020, 9, 1)
delta = end_date - start_date

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    day_string = day.strftime("%Y-%m-%d")
    dates.append(day_string)


def add_url():
    for date in dates:
        c_string = url + date
        url_list.append(c_string)


add_url()

for u in url_list:
    read_pg = requests.get(u)
    sleep(2)
    soup = BeautifulSoup(read_pg.text, "html.parser")
    songs = soup.find("table", {"class": "chart-table"})
    song_scrape(u)


def song_scrape(x):
    pg = x
    for tr in songs.find("tbody").findAll("tr"):
        artist = tr.find("td", {"class": "chart-table-track"}).find("span").text
        artist = artist.replace("by ", "").strip()
        title = tr.find("td", {"class": "chart-table-track"}).find("strong").text
        song_id = tr.find("td", {"class": "chart-table-image"}).find("a").get("href")
        song_id = song_id.split("track/")[1]
        url_date = x.split("daily/")[1]
        final.append([title, artist, song_id, url_date])


final_df = pd.DataFrame(final, columns=["Title", "Artist", "Song ID", "Chart Date"])
with open('spotifyData.csv', 'w') as f:
    final_df.to_csv(f, header=True, index=False)
