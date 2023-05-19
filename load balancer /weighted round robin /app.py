from flask import Flask, request
import requests
import sys
import os
import math
from fractions import gcd

app= Flask(__name__)
round_robin=0
x=0
i= -1
cw= 0
s=[0,1]
w=[2,6]
ipAddressWebServer1= "20.238.39.149"
ipAddressWebServer2= "13.74.217.223"

@app.route('/')
def func():
    global s,w,cw,i
    round_robin = weighted_round_robin()
    if round_robin == 0:
        response = requests.get("http://{}:8080".format(ipAddressWebServer1))

        return str(response.content)
    elif round_robin == 1:
        response = requests.get("http://{}:8080".format(ipAddressWebServer2))
        return str(response.content)
    else:
        return "Not Found",404

def weighted_round_robin():
    global s,w,cw,i
    while True:
        i=(i+1)%2
        if i==0:
            cw=cw-gcd(*w)
            if cw<=0:
                cw=max(w)
                if cw==0:
                    return none
        if w[i]>=cw:
            return s[i]  #W(Si) indicates the weight of Si;

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000)
