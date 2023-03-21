import requests

resp = requests.get("https://restcountries.com/v3.1/all")
if resp.status_code != 200:
    print("Sorry! Could not get details!")
    exit()

countries = resp.json()
for c in sorted(countries, key=lambda d: d['population'], reverse=True)[:10]:
    name = c['name']['common']
    if 'capital' in c:
        capital = c['capital'][0]
    else:
        capital = 'Unknown'
    population = c["population"]
    area = c['area']
    print(f"{name:30} {capital:20} {population:10} {area:10}")
