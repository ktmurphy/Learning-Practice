import requests


class NewsFeed:
    """Representing multiple new titles and links as a single string.
    """
    ## TO USE, add api
    base_url = "https://newsapi.org/v2/everything?"
    api = ##ADD API
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)
        emailBody = ''
        for article in articles: 
            emailBody = emailBody = emailBody + article['title'] + "\n" + article['url'] + "\n\n"
        return emailBody

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        response.close()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f'{self.base_url}' \
        f'qInTitle={self.interest}&' \
        f'from={self.from_date}&' \
        f'to={self.to_date}&' \
        f'language={self.language}&' \
        f'apiKey={self.api}'
        
        return url

if __name__ == 'main':
    news_feed = NewsFeed(interest='nasa', from_date='2023-06-12', to_date = '2023-06-13', language = 'en')
    print(news_feed.get())
        
