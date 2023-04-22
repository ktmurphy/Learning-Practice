#! python3
import requests, bs4
from pathlib import Path

"""
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup.bs4.BeautifulSoup(res.text, 'html.parser')
type(noStarchSoup)
"""
# p = Path('C:/Users/katie/OneDrive/Documents/Coding/Automate the Boring Stuff book/automate_online-materials')
exampleFile = open(
    "C:/Users/katie/OneDrive/Documents/Coding/Automate the Boring Stuff book/automate_online-materials/example.html"
)
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), "html.parser")
elems = exampleSoup.select("#author")
print(type(elems))
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)


spanElem = exampleSoup.select("span")[0]
print(str(spanElem))
spanElem.get("id")
