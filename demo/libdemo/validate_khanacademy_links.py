import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.khanacademy.org"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
for link in bs.find_all("a"):
    href = link['href']
    if href.startswith("javascript:void"):
        continue

    if not href.startswith("http"):
        href = WEBSITE + href

    # validate link
    linkresp = requests.get(href)
    print("Validating : ", href, end='')
    if linkresp.status_code == 404:
        print(' -->broken')
    else:
        print(' -->success')
