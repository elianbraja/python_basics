from flask import Flask
from datetime import datetime
from python_web_browser.day import dayname

app = Flask(__name__)

@app.route("/")
def hello_world():
    return f"<p>hello, world! Happy {dayname(datetime.now())}</p>"
