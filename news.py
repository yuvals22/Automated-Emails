#api key= f107017258474714b83308862c0074ad
import requests

class NewsFeed:
    """ Representing multiple news titles and links as a single string """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "f107017258474714b83308862c0074ad"

    def __init__(self, interest, from_date, to_date, language):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = (f"{self.base_url}" \
               f"qInTitle={self.interest}&" \
               f"from={self.from_date}&" \
               f"to={self.to_date}&" \
               f"Language={self.language}&" \
               f"apiKey={self.api_key}")

        response = requests.get(url)
        content = response.json()
        articles = content["articles"]

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article["url"] + "\n\n"

        return email_body

# news_feed = NewsFeed(interest=('Alibaba', 'stock'),from_date='2021-09-20',to_date='2021-10-02', language= 'en')
# print(news_feed.get())

