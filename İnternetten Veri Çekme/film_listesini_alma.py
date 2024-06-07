import requests
from bs4 import BeautifulSoup

# verileri alacagimiz sitenin adresine istek yolluyoruz
r = requests.get('https://www.sinemalar.com/filmler/en-iyi-filmler')
filmListesi = []

# gelen istegin daha duzgun yazdirilmasi icin duzenliyoruz
soup = BeautifulSoup(r.content, features="html.parser")

# sayfa html'indeki filmlerin bulundugu kapsayici etiketi elde ediyoruz
link = soup.find_all("div", {"class": "movies"})

# tablodaki her bir filme ulasiyoruz
filmler = link[0].find_all("a", {"class": "movie"})

for film in filmler:
    # her filmin bulundugu etikette ismin yer aldigi alt kapsayiciyi buluyoruz
    filmBaslik = film.find_all("div", {"class": "details"})
    # son olarak sadece isim bilgisinin bulundugu kapsayici etiketi aliyoruz
    isim = filmBaslik[0].find_all("div", {"class": "name"})
    # div icindeki metni listemize ekliyoruz
    filmListesi.append(isim[0].text)

print(filmListesi)

