from flask import Flask
import os, psutil
import socket

app = Flask(__name__)
@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3> <b>Hostname:</b> {hostname} <h3> This is from VM8 </h3> <br/>"
    return html.format(name=os.getenv("NAME", "Roman"), hostname=socket.gethostname())

@app.route("/load")
def load():
    load=psutil.cpu_percent()
#    html = "<h4>Hello....check percentage ....{See}"
    return str(load) #html.format(See=load)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
