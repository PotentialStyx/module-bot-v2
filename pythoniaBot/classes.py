import pythoniaBot.errors as errors
from pythoniaBot.discordCustom import context
class Permission:
  def __init__(self,name,importance,ID,inherits = [],canUse = None):
    self.name = name
    self.identifier = ID
    self.roleRank = importance
    self.inherits = inherits
    if(canUse!=None):
      self.canUse = inherits
    else:
      self.canUse = canUse
    self.importance= importance
class Role:
  def __init__(self,name,rank,ID,permissions = [Permission('Null',None,000)]):
    self.name = name
    self.identifier = ID
    self.roleRank = rank
    self.permissions = permissions
  '''
  def printProperties(self):
    print('name: ' + self.name)
    print('ID: ' + str(self.identifier))
    print('rank: ' + str(self.roleRank))
    print('permissions: ' + str(self.permissions))'''
class Server:
  def __init__(self,ID,prefix='**',commands=[],roles = [],permissions = []):
    self.commands=[]
    for i in commands:
      self.addCommand(i)
    self.serverID = ID
    self.prefix = prefix
    if isinstance(roles, list):
      self.roles = roles
    elif isinstance(roles,Role):
      self.roles = []
      self.roles.append(roles)
    if isinstance(permissions, list):
      for i in permissions:
        if isinstance(i,Permission):
          self.perms = permissions
        else:
          if(not isinstance(permission,None)):
            raise errors.incorrectTypeRecieved('recived ' + type(i).__name__ + ' in list of permissions, expected Permission object')
    elif isinstance(permissions,Permission):
      self.perms = []
      self.perms.append(permissions)
    else:
      raise errors.incorrectTypeRecieved('recived '+type(permissions).__name__ + ', expected Permission object or list of Permission object')
  def add_role(self,rolesToAdd):
    if isinstance(rolesToAdd, list):
      for i in rolesToAdd:
        self.roles.append(i)
    if isinstance(rolesToAdd, Role):
      self.roles.append(rolesToAdd)
  def isPremium(self):
    return(False)
  def addCommand(self,command):
    if(command.custom):
      return('Not allowed (not premium server)')
    else:
      self.commands.append(command)

class Command:
  def __init__(self,name,response,commandType,isCustom = True):
    self.trigger = name
    self.response = response
    self.custom = isCustom
    self.ctype = commandType
  async def runCommand(self,message,args,server):
    if(self.ctype == 'func'):
      await self.response(context(message),args,server)
    elif(self.ctype == 'str'):
      await message.channel.send(self.response)
class premiumServer(Server):
  def isPremium(self):
    return(True)
  def addCommand(self,command):
    self.commands.append(command)