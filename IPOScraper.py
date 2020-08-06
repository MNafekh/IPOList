import json
import os
from datetime import date

import discord
import requests
from dotenv import load_dotenv
from prettytable import PrettyTable
from texttable import Texttable
from requests_html import HTMLSession

load_dotenv()

def get_ipos():
    title = "Upcoming IPOs"
    session = HTMLSession()

    r = session.get('https://www.marketwatch.com/tools/ipo-calendar')
    #r = session.get('https://www.investing.com/ipo-calendar/')

    # table = r.html.find('.ipoTbl', first=True)    
    # rows = table.find('td')

    table = r.html.find('.table')
    if len(table) > 0:
        rows = table[1].find('td')
        t = PrettyTable(['Company', 'Symbol', 'Price Range', 'Shares', 'Week'], align="l")
        cnt = 0
        while cnt < len(rows):
            t.add_row([rows[cnt].text, rows[cnt+1].text, rows[cnt+3].text, rows[cnt+4].text, rows[cnt+5].text])
            cnt += 6
        return "```\n" + title + "\n" + t.get_string() + "```"
    else:
        return "Marketwatch bein a lil bish. Try again later."
