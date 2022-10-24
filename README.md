### Install
```shell
pip install Flask
```

### GET, POST, PUT, DELETE
```shell
CRUD
CREATE = POST
READ   = GET
UPDATE = PUT
DELETE = DELETE

# create
@app.route('api/v1/predict', methods=['POST'])
# read
@app.route('/', methods=['GET'])
# update
@app.route('/', methods=['PUT'])
# delete
@app.route('/', methods=['DELETE'])
```
### ROUTE
```shell
url = http://127.0.0.1:5000/api/v1/predict
# submit a POST request to the url
data = {"age": 30, "income": 40000, "height": 165, "credit_score": 700}
# we get a response back
response = {"probability": 0.95}

# USING CURL
curl -X POST -d {"age": 30, "income": 40000, "height": 165, "credit_score": 700} \
    http://127.0.0.1:5000/api/v1/predict

response = {"probability": 0.95}  

```

### Frameworks
```shell
Java - SpringBoot
Python - Flask and FastAPI
Go - Fiber
React - 
```
### Testing Endpoints/Route/Destinations
```shell
Postman, HTTPIE, Insomnia, Curl, Browser, Any programming language
```

### Implementation
   - Build API
   - Dockerize it
   - Kubernetes - will generate public IP address (10.10.23.45)
   - Link this PUBLIC IP to our domain name eg. https://elbowai.com/api/v1/books
