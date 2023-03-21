import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.w3schools.com")
bs = BeautifulSoup(resp.text, "html.parser")

for link in bs.find_all("a"):
    print(link['href'])
