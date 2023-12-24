import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
from yt_dlp import YoutubeDL


load_dotenv()

DISCORD_TOKEN = os.getenv("discordToken")
intents = discord.Intents().all
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="/", intents=intents)


URLS = ['https://www.youtube.com/watch?v=BaW_jenozKc']

ydl_opts = {
    'format': 'm4a/bestaudio/best',
    # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'm4a',
    }]
}

with YoutubeDL(ydl_opts) as ydl:
    error_code = ydl.download(URLS)


def requestSong():


    return "Currently playing ..."