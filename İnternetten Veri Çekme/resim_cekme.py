import requests
from bs4 import BeautifulSoup


url = "https://www.nefisyemektarifleri.com/kolay-kek-nasil-yapilir/"

response = requests.get(url)
soup = BeautifulSoup(response.content, features="html.parser")


if response.status_code == 200:
    label = QLabel()
    pixmap = QPixmap()
    pixmap.loadFromData(response.content)
    label.setPixmap(pixmap)
    label.show()
    sys.exit(app.exec_())
else:
    print(f"Failed to download image. URL: {url}")



