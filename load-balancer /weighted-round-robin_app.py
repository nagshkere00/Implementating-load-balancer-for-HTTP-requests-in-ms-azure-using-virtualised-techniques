from flask import Flask, request
from random import randint
import requests, sys

app = Flask(__name__)
#change the ip address according to your machine.
ipAddressWebServer2 = "20.166.1.191:8080"
ipAddressWebServer1 = "20.166.61.62:8080"



@app.route('/weight')
def output():
    global loadofserver1, loadofserver2
    result=loadbalance()
#    print ("Load of the server is : ", loadofserver1)
#    print ("Load of the server is : ", loadofserver2)
    return result


def loadbalance():
    global loadofserver1, loadofserver2
    loadofserver1=float(requests.get("http://" + ipAddressWebServer1 + "/load").content)
    loadofserver2=float(requests.get("http://" + ipAddressWebServer2 + "/load").content)


    if loadofserver1<=loadofserver2:
        loadresult=requests.get("http://" + ipAddressWebServer1 + "/")
        print ("Load of the server1 is : ", loadofserver1)
        sys.stdout.flush()
    else :
        loadresult=requests.get("http://"+ ipAddressWebServer2 + "/")
        print ("Load of the server2 is : ", loadofserver2)
        sys.stdout.flush()
    return str(loadresult.content)+("Load of VM19 is: ")+str(loadofserver1)+("   ")+("Load of VM20 is: ")+str(loadofserver2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)

                                                                                     
#another   
                                                                                     
from flask import Flask, request
import requests, sys

app = Flask(__name__)
#change the ip address according to your machine.
ipAddressWebServer2 = "20.238.39.149:8080"
ipAddressWebServer1 = "13.74.217.223:8080"



@app.route('/weight')
def output():
    global loadofserver1, loadofserver2
    result=loadbalance()
#    print ("Load of the server is : ", loadofserver1)
#    print ("Load of the server is : ", loadofserver2)
    return result


def loadbalance():
    global loadofserver1, loadofserver2
    loadofserver1=float(requests.get("http://" + ipAddressWebServer1 + "/load").content)
    loadofserver2=float(requests.get("http://" + ipAddressWebServer2 + "/load").content)


    if loadofserver1<=loadofserver2:
        loadresult=requests.get("http://" + ipAddressWebServer1 + "/")
        print ("Load of the server1 is : ", loadofserver1)
        sys.stdout.flush()
    else :
        loadresult=requests.get("http://"+ ipAddressWebServer2 + "/")
        print ("Load of the server2 is : ", loadofserver2)
        sys.stdout.flush()
    return str(loadresult.content)+("Load of VM8 is: ")+str(loadofserver1)+("   ")+("Load of VM7 is: ")+str(loadofserver2)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
