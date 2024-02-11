# Implementating-load-balancer-for-HTTP-requests-in-ms-azure-using-virtualised-techniques

AIM:
To implement and demonstrate of Load Balancer for HTTP Requests in MS Azure using Virtualization Techniques.

Apparatus:
Ubuntu machine, MS Azure virtual machines.

Method:
Used flask module in python to configure the webservers and the load balancing server.

Web service:
• Implemented a web service that displays a webpage upon request by the client.
• The service is provided by two or more different web servers (server 2, server 3, etc.), and the servers. will answer according to the selected load balancing scheme(round robin(RR), weighted round robin(WRR), load sensitivity(LS)).
• There is a proxy (server 1) on the ingress.

Web servers:
• Each web server provides a similar webpage but the response indicates which server is used.
• The web server will send spontaneously updates about their load status to the load balancer.
• The load balancer receives all HTTPS requests from the proxy and forwards them to the appropriate web server according to the applied balancing scheme.
• The load balancer forms a “queue” for each web server.

Usage Example:

Build docker image for the Python app on web server 2 and web server 3:
docker build -t pymyweb .
docker run -p 8080:8080 pymyweb

Build docker image for respective load balancing techniques (RR,WRR,LS) on server 1:
docker build -t sk .
docker run -p 8080:8080 sk
