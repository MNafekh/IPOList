import discord
import requests
import os
import json
from lxml import etree
from datetime import date
from urllib.request import urlopen
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from prettytable import PrettyTable

load_dotenv()

TOKEN = os.getenv('FINN_KEY')

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
