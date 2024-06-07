import requests
from bs4 import BeautifulSoup

url = "https://www.izlesene.com/video/trilece-nasil-yapilir/9152575"

response = requests.get(url)
soup = BeautifulSoup(response.content, features="html.parser")

div = soup.find_all("video", {"id": "adm-player-live_html5_api"})

print(div)
