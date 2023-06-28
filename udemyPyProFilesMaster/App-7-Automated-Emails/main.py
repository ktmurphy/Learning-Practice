import yagmail
import pandas
import xlrd
import news
import datetime

##To Use, add password

df = pandas.read_excel('people.xlsx')
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
def send_email(today, yesterday, row):
    news_feed = news.NewsFeed(interest=row['interest'], from_date=yesterday, to_date=today)
    email = yagmail.SMTP(user='mpetry14@gmail.com', password=#ADD')
    email.send(to=row['email'], 
            subject=f'Your {row["interest"]} news for today!', 
            contents=f'Hi {row["name"]},\n\n Here is the news about {row["interest"]}. \n\n{news_feed.get()} \n Katie')

for index, row in df.iterrows():
    send_email(today, yesterday, row)


