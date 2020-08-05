import json
import os
from datetime import date

import discord
import requests
from dotenv import load_dotenv
from prettytable import PrettyTable
from requests_html import HTMLSession

load_dotenv()

def get_ipos() -> discord.Embed:
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
