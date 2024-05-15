import numpy as np
import pandas as pd

import discord
import google.generativeai

GOOGLE_API_KEY = 
DISCORD_BOT_KEY = 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

client.run(DISCORD_BOT_KEY)



