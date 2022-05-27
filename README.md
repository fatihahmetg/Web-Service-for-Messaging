# Web-Service-for-Messaging

A small web service that has two endpoints:

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that
message (in hexadecimal format)

2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent
<hash> returns a 404 error.
  
Accessible from https://virtserver.swaggerhub.com/test26585/messages/3.0
  
  
  Generated using OPENAPI with YAML and Swagger tools.
  Python-Flask server.

  See python-flask-server-generated/README.md to run the server.
  
  
## How can you scale your implementation?
  Multithreaded architechture can be used instead of a single thread.
  
## How did you deploy this application?
  I used Swagger's virtual server for this application. 
  
## How can you improve this process and make it easy to maintain?
  I will use CI/CD pipelines and use several containers.
