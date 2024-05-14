import numpy as np
import pandas as pd

import discord
import google.generativeai

GOOGLE_API_KEY = 'AIzaSyBl3nMIbRZQMfKjq5LX4I1k06_ocIndbVM'
DISCORD_BOT_KEY = 'MTIzMzY1ODcxNTA4NTczODAzNQ.Gqzhfc.fHgTmJFsnFGoNwIdhzwDZIgkXZ7VIZ_XWtY3_k'

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client.run(DISCORD_BOT_KEY)



