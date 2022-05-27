# Web-Service-for-Messaging

A small web service that has two endpoints:

1. /messages takes a message (a string) as a POST and returns the SHA256 hash digest of that
message (in hexadecimal format)

2. /messages/<hash> is a GET request that returns the original message. A request to a non-existent
<hash> returns a 404 error.
  
Accessible from https://virtserver.swaggerhub.com/test26585/messages/3.0
  
  
  Generated using OPENAPI and Swagger tools.
  Python-Flask server.
