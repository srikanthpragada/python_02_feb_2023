import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.khanacademy.org"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
count = 0
for link in bs.find_all("a"):
    href = link['href']
    if href.startswith("javascript:void"):
        continue

    if not href.startswith("http"):
        href = WEBSITE + href

    print(href)
    count += 1

print("Count = ", count)
