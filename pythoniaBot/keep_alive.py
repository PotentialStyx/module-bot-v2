from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "bot is online"

def run():
    app.run(host='0.0.0.0',port='8080',debug=False)

def keep_alive():
    server = Thread(target=run)
    server.start()
