import os
import time
import requests

import discord
from apscheduler.schedulers.blocking import BlockingScheduler
from discord import Webhook, RequestsWebhookAdapter
from dotenv import load_dotenv

import IPOScraper as api

load_dotenv()

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun', hour='18')
def print_table() :
    hook_id = os.getenv('DANK_HOOK_ID')
    hook_token = os.getenv('DANK_HOOK_TOKEN')

    webhook = Webhook.partial(hook_id, hook_token, adapter=RequestsWebhookAdapter())
    webhook.send(api.get_ipos(), username='IPOBot')

sched.start()