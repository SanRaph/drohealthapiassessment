# drohealthapiassessment

### Predict menstruation cycles


##### This is a REST API REST API that helps estimate a woman’s period cycles within a specific timeframe

Getting Started
To run this application locally:

Open up terminal (on MacOS) and switch directory to Desktop by running:

```Python
cd ~

```
For Windows, open git bash and switch directory to desired folder e.g:

```Python

cd Desktop

```

Clone the repository by running:


```Python

git clone https://github.com/SanRaph/drohealthapiassessment.git

```

Then run the following commands consecutively

```Python
cd drohealthapiassessment
```

```Python
python3 -m venv venv
```
 
To activate virtual environment (MacOS users):
```Python
source venv/bin/activate
```
To activate virtual environment (Windows users):
```Python
source venv/Source/activate
```
Install dependencies as follows (both MacOS & Windows):
```Python
pip3 install -r requirements.txt
```
To run unit tests, run the command below:
```Python
python3 manage.py test
```

Make migrations by running the commands below:
```Python
python3 manage.py makemigrations
```
```Python
python3 manage.py migrate
```

To start the Django server, run:
```Python
python3 manage.py runserver
```
The API endpoints are now available to be used
Registration
Open Postman and register a user for by making a POST request to the address below and with a payload in json format. A sample has been provided below
Endpoint

 http://localhost:8080/user/account/

```Python
Payload

{
    "user":"San",
    "email":"san@san.com",
    "password":"123pass321"
}
```


A response containing the details of the user will be received to confirm registration
Response with a Token

```Python
{
    "id": 4,
    "username": "quams",
    "email": "quams@quams.com",
    "token": "1560ec66e4fe82d859d619967f0a6a2b8dc0ee37"
}

```

Login
The registered user can login by making another POST request to the address below and with a payload (email & password) in json format. A sample also has been provided below
Endpoint

 http://localhost:8080/user/api-token-auth/
 
 ```Python
Payload

{
    "username": "sanraph",
    "password": "raphytex"
}
```
A response token will be returned as a respons.

 ```Python
Response

{
    "token": <random_generated_token>
}
```
Creation of Cycle (Authorization)
The registered user can create a cycle by making a POST request to the address below and with a payload in json format. A sample also has been provided below
Note: This endpoint requires Token Authentication. The generated token in the LOGIN endpoint can be passed into the headers in the format also described below
Endpoint
http://localhost:8080/menstruation


 ```Python
 Headers

"Authorization" : "Token <generated_token>"
Payload

{
    "Last_period_date":"2022-08-20",
    "Cycle_average":25,
    "Period_average": 5,
    "Start_date":"2022-09-26",
    "End_date":"2021-09-26"
}


```
A response containing the name of the user and total_created_cycles will be received.
Expected result has been displayed below

 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```

Updating of Cycle (Authorization)
The registered user can create a cycle by making a PUT request to the address below and with a payload in json format which will update user information. A sample also has been provided below
Note: This endpoint also requires Token Authentication. The generated token in the LOGIN endpoint needs to be passed into the headers in the format also described below
Endpoint

[put]  http://localhost:8080/menstruation

 ```Python
Headers

"Authorization" : "Token <generated_token>"
Payload

{
   "Last_period_date":"2022-08-20",
    "Cycle_average":25,
    "Period_average": 6,
    "Start_date":"2022-09-26",
    "End_date":"2021-09-26"
}

```

A response containing the name of the user and total_created_cycles will be received.
Expected result has been displayed below
 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```
Listing of Cycle Events (Authorization)
The registered user can view their current cycle events by making a GET request to the address below and without any payload. However, a path parameter (date) needs to be provided in the url. An example has been provided below
Note: This endpoint also requires Token Authentication. The generated token in the LOGIN endpoint needs to be passed into the headers in the format also described below
Endpoint

http://localhost:8080/menstruation-list

 ```Python
 Headers

"Authorization" : "Token <generated_token>"

```

A response containing the event and the date will be received.
Expected result has been displayed below
 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```
