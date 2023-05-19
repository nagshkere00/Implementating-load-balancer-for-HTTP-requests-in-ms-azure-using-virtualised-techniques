from flask import Flask, request
import requests
import sys
import os


app = Flask(__name__)
round_robin=0

#change the ip address in the below lines according to your machines.
ipAddressWebServer1 = "20.238.39.149:8080"
ipAddressWebServer2 = "13.74.217.223:8080"

@app.route('/')
def fun():
    global round_robin
    if round_robin == 0:
        response = requests.get("http://" + ipAddressWebServer1 + "/")
        round_robin = 1
        return str(response.content)
    elif round_robin == 1:
        response = requests.get("http://" + ipAddressWebServer2 + "/")
        round_robin = 0
        return str(response.content)
    else:
        return "Not Found",404

if __name__=="__main__":
    app.run(host='0.0.0.0', port=4000)
