import requests
from bs4 import BeautifulSoup
from datetime import *


def find_days_to_go(stdate):
    sysdate = datetime.now()
    year = sysdate.year
    sd = datetime.strptime(f"{stdate}-{year}", "%d-%b-%Y")
    td = sd - sysdate
    # print("Timedelta " , td)
    return td.days


WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
if table is None:
    print("Sorry! Could not get details!")
    exit()

for row in table.find_all("tr")[1:]:
    cols = row.find_all("td")
    title = cols[0].text
    timings = cols[1].text
    stdate = cols[2].text
    days = find_days_to_go(stdate)
    print(f"{title:40} {timings:15} {stdate:10}  {days:3}")
