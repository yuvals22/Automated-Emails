import time

import pandas
import openpyxl
import datetime
import yagmail
from news import NewsFeed

df = pandas.read_excel(r'C:\ex\Automated_Emails\users.xlsx')
today = datetime.datetime.now().strftime('%Y-%m-%d')
yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

def _send_email():
    row['interest'] = row['interest'].replace(",", " ")
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today,
                         language='en')
    email = yagmail.SMTP(user="YourEmail", password="YourPassword")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today",
               contents=f"Hey {row['name']},\n See what's on about {row['interest']} today.\n {news_feed.get()} \n Yuval")

for index, row in df.iterrows():
    _send_email()

## Nonstop loop
# while True:
#     if datetime.datetime.now().hour == 8 and datetime.datetime.now().minute == 00 :
#         the_function = the_function
#         the_function = the_function
#         the_function = the_function
#     time.sleep(60)
#

