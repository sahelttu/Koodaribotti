import os

import discord
from dotenv import load_dotenv
from datetime import datetime

date_format = "%d/%m/"
now = datetime.now()
wappu = datetime(now.year, 5, 1)
wappunextyear = datetime(now.year+1, 5, 1)
delta = wappu - now
delta2 = wappunextyear - now
final = delta.days
final2 = delta2.days
koodiprojektit = ["laskin", "pankkiautomaatti", "kalenteri",
                  "discord-botti", "twitter-botti", "tasoloikkapeli",
                  "peliklooni (esimerkiksi Tetris", "tekstiseikkailu",
                  "labyrintti", "shakkibotti", "pacman-botti",
                  "database :isags:", "nettisivu portfoliolle", "tietovisa",
                  "Sakarin villapaitapeli remake", ]


class CommandHandler:

    def __init__(self, client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def command_handler(self, message):
        for command in self.commands:
            if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return message.channel.send(str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return message.channel.send(str(command['function'](message, self.client, args)))
                            break
                        else:
                            return message.channel.send('command "{}" requires {} argument(s)"{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

ch = CommandHandler(client)


def python_function(message, client, args):
    try:
        return 'https://docs.python.org/3/'
    except Exception as e:
        return e


ch.add_command({
    'trigger': '!python',
    'function': python_function,
    'args_num': 0,
    'args_name': ['string'],
    'description': 'Antaa linkin python-dokkariin'
})


def wappu_function(message, client, args):
    try:
        if final > 0:
            return '{} päivää vappuun :beers:'.format(final)
        elif final == 0:
            return ':beers: NYT ON VAPPU :beers:'
        elif final < 0:
            return '{} päivää vappuun :beers:'.format(final2)
    except Exception as e:
        return e


ch.add_command({
    'trigger': '!milloinvappu',
    'function': wappu_function,
    'args_num': 0,
    'args_name': ['string'],
    'description': 'Laskee päiviä vappuun'
})

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Mashed"))
    return 'Ha-haloo? :robot:'


@client.event
async def on_message(message):
    if message.author == client.user:
        pass
    else:

        try:
            await ch.command_handler(message)
        except TypeError as e:
            pass
        except Exception as e:
            print(e)


client.run(TOKEN)
