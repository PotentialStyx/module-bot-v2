import discord
import traceback
from pythoniaBot.errors import *
from pythoniaBot.classes import *
from pythoniaBot.keep_alive import *
import pythoniaBot
client = discord.Client()

class Bot:
  def __init__(self,token,servers):
    self.token = token
    self.servers = servers


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    yes = False
    for i in bot.servers:
      if i.serverID == message.guild.id:
        yes = True
        server = i
    if(not yes):
      for i in bot.servers:
        if(i.serverID == '*'):
          yes = True
          server = Server('*',i.prefix,i.commands)
    if(yes):
      if(message.content[:len(server.prefix)]==server.prefix):
        commandTemp = message.content[len(server.prefix):]
        for i in server.commands:
          if(i.trigger == commandTemp.split(' ')[0]):
            temp = commandTemp.split(' ')
            del temp[0]
            try:
              await i.runCommand(message,temp,server)
            except Exception as e:
              await message.channel.send('Error: \n```\n{}```'.format(traceback.format_exc()))
    else:
      return(None)
bot = Bot(0,[])
def newBot(token,servers,flask = True,app = pythoniaBot.keep_alive.app):
  if not isinstance(servers,list):
    raise incorrectTypeRecieved('Recived: '+type(servers).__name__ + ' expected a list of Server objects')
  for i in servers:
    if not isinstance(i,Server):
      raise incorrectTypeRecieved('Recived a list with: '+type(servers).__name__ + ' expected a list of Server objects')
  bot.token = token
  bot.servers = servers
  if(flask):
    keep_alive(app == pythoniaBot.keep_alive.app, app)
  client.run(bot.token)
