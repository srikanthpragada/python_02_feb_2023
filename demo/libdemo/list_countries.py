import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

countries = resp.json()
for c in countries:
    name = c['name']['common']
    if 'capital' in c:
        capital = c['capital'][0]
    else:
        capital = 'Unknown'

    population = c["population"]

    print(f"{name:50} {capital:30} {population:10}")
