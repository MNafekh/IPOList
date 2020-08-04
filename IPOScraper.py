import discord
import requests
import os
import json
from datetime import date
from requests_html import HTMLSession
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()

TOKEN = os.getenv('FINN_KEY')

#don't know how to get future IPOs, deprecated for now
def get_ipos() -> discord.Embed:
    """
    Returns a list of the IPOs taking place in the current month
    Sample API output:
    {'date': '2020-07-02', 'exchange': 'NYSE', 'name': 'Lemonade, Inc.', 'numberOfShares': 11000000, 'price': '29.00'
        , 'status': 'priced', 'symbol': 'LMND', 'totalSharesValue': 319000000}
    """
    now = date.today()
    fromdt = date(now.year, now.month, 1)
    todt = date(now.year, now.month + 1, 1)
    title = "Upcoming IPOs for {0:%B}".format(now)
    description=""
    url = 'https://finnhub.io/api/v1/calendar/ipo?from=' + str(fromdt) + '&to=' + str(todt) + '&token=' + TOKEN
    print(url)
    r = requests.get(url)
    data = r.json()['ipoCalendar'] 
    for t in data:
        line = t['name'] + " | " + t['date'] + "\n"
        description += line
    return discord.Embed(title=title, description=description)


def get_ipos_nasdank() -> discord.Embed:
    """
    Gets list of IPOs from Nasdaq site
    """
    now = date.today()
    title = "Upcoming IPOs for {0:%B}".format(now)
    session = HTMLSession()
    r = session.get('https://www.investing.com/ipo-calendar/')
    table = r.html.find('.ipoTbl', first=True)    
    rows = table.find('td')
    t = PrettyTable(['Date', 'Company', 'Value', 'Price Range'], align="c")
    cnt = 0
    while cnt < len(rows):
        t.add_row([rows[cnt].text, rows[cnt+1].text, rows[cnt+3].text, rows[cnt+4].text])
        cnt += 6
    description = t.get_string()
    return discord.Embed(title=title, description=description)