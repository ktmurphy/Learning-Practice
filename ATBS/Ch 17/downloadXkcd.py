#! python3
# downloadXkcd.py - downloads every XKCD comic
import requests, os, bs4, threading, time

startTime = time.time()

url = "https://xkcd.com"
os.makedirs("xkcd", exist_ok=True)


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # download the page
        print("Downloading page %s..." % urlNumber)
        res = requests.get("https://xkcd.com/%s" % urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image")
        else:
            comicUrl = "https:" + comicElem[0].get("src")
            print("Downloading image %s..." % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
    # from old one - prevLink = soup.select('a[rel="prev"]')[0]
    # from old one - url = 'https://xkcd.com' + prevLink.get('href')


downloadThreads = []
for i in range(0, 140, 10):
    start = i
    end = i + 9
    if start == 0:
        start = 1
    downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
for downloadThread in downloadThreads:
    downloadThread.join()
endTime = time.time()
print("Done.")
print(startTime - endTime)
