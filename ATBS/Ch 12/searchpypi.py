#! python3
# searchpypi.py - opens several search results

import requests, sys, webbrowser, bs4, logging

logging.disable(logging.CRITICAL)
logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.debug("start of program")

print("Searching...")
res = requests.get("https://pypi.org/search/?q=" + " ".join(sys.argv[1:]))
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "html.parser")
logging.debug(str(soup))
linkElems = soup.select(".package-snippet")
logging.debug(str(linkElems))
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = "https://pypi.org" + linkElems[i].get("href")
    logging.debug(str(urlToOpen))
    print("Opening: ", urlToOpen)
    webbrowser.open(urlToOpen)
