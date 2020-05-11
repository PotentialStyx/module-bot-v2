# module bot v2

### classes:

* Server
* premiumServer
* Command

### use:
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
