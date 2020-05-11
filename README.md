# module bot v2

### classes:

* Server
* premiumServer
* Command

### use:
* note these are all classes under pythoniaBot.classes (EX. Command would be pythoniaBot.classes.Command or however you import it)
* Command:
  * arguments:
    * Trigger: the trigger phrase if it was help [prefix]help would trigger it
    * Response: either a callback (needs to be async) that it will call or a string that it will always respond with
    * Type: if you made Response a callback this is 'func' if its a string this is 'str'
    * Custom: if this is True non premiumServers wont be able to use the command
  * example:
    ```python
    _help = Command('help','Commands are: \n - help', 'str',False)
    ```
* Server:
  * arguments:
    * ID: this is the sever id use developer mode to get it
    * Prefix: this is the prefix for this server
    * Commands: this is a list of Command objects for that server
  * example:
    ```python
    server = Server(9,'**',[_help,_premium])
    ```
* premiumSerer:
  * this is the same as Server but allows custom commands
  
### how to make functions as commands:
all commands that are fumctions are passes 3 arguments:
1. ctx (some features may not work)
2. args - a list of the other words in the command EX: !help command add \['command','add'] would be arg
3. server this will pass the Server or premiumServer object in
all functions mush also be async or they will not work

### initalizing the bot
to initalize the bot you do:
```python
import pythoniaBot
pythoniaBot.premade.newBot({{token}},{{los}})
```
the token is the token you got from discord and los is a list of the Server/premiumServer objects

note: this will also start a flask server this will be toggleable later
