import requests
import os
from bs4 import BeautifulSoup

if not os.path.exists('downloaded_images'):
    os.makedirs('downloaded_images')

# verileri alacagimiz sitenin adresine istek yolluyoruz
r = requests.get('https://www.sinemalar.com/filmler/en-iyi-filmler')
filmListesi = []

# gelen istegin daha duzgun yazdirilmasi icin duzenliyoruz
soup = BeautifulSoup(r.content, features="html.parser")

# sayfa html'indeki filmlerin bulundugu kapsayici etiketi elde ediyoruz
links = soup.find_all("img", {"class": "poster"})


for idx, link in enumerate(links):
    url = link.get('data-src')
    response = requests.get(url)
    if response.status_code == 200:
        file_extension = url.split('.')[-1]
        with open(f"downloaded_images/image_{idx}.{file_extension}", "wb") as f:
            f.write(response.content)
        print(f"Image {idx+1} downloaded successfully!")
    else:
        print(f"Failed to download image {idx+1}. URL: {url}")

