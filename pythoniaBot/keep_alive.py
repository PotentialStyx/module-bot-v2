from flask import Flask
from threading import Thread


app = Flask('')

@app.route('/')
def main():
    return "bot is online"

def run(app,none):
    app.run(host='0.0.0.0',port='8080',debug=False)

def keep_alive(keepApp = True,newApp = app):
    if(keepApp==True):
      server = Thread(target=run,args=(app,0))
      server.start()
    else:
      server = Thread(target=run,args=(newApp,0))
      server.start()
