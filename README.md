# drohealthapiassessment

### Predict menstruation cycles


##### A REST API that helps predict a woman’s period cycles within a specific timeframe

<emp>Getting Started</emp>
<p><i>To run this application on your machine:</i></p>

* [x] Open up terminal (on MacOS) and switch directory to Desktop by running:

```Python
cd ~

```
* [x] For Windows, open git bash and switch directory to desired folder e.g:

```Python

cd Desktop

```

* [x] Clone the repository by running the command below:


```Python

git clone https://github.com/SanRaph/drohealthapiassessment.git

```

* [x] Next up run the following commands respectively:

```Python
cd drohealthapiassessment
```

```Python
python3 -m venv venv
```
 
* [x] To activate virtual environment (MacOS users):
```Python
source venv/bin/activate
```
* [x] To activate virtual environment (Windows users):
```Python
source venv/Source/activate
```
* [x] Install dependencies as follows (both MacOS & Windows):
```Python
pip3 install -r requirements.txt
```
* [x] To run unit tests, run the command below:
```Python
python3 manage.py test
```

* [x] Run the commands below to make migrations:
```Python
python3 manage.py makemigrations
```
```Python
python3 manage.py migrate
```

* [x] To start the Django server, run:
```Python
python3 manage.py runserver
```
The API endpoints are now available for use.

* [x] Registration
Open Postman, curl or Httpie and register a user by making a POST request to the address below and with a payload in json format.
Endpoint

```Python
 http://localhost:8080/user/account/

```

```Python
Payload

{
    "user":"San",
    "email":"san@san.com",
    "password":"123pass321"
}
```


A response containing the details of the user will be returned to confirm registration
Response with a Token

```Python
{
    "id": 4,
    "username": "quams",
    "email": "quams@quams.com",
    "token": "1560ec66e4fe82d859d619967f0a6a2b8dc0ee37"
}

```

* [x] Login
The registered user can login by making another POST request to the address below and with a payload (email & password) in json format to receive a Token.
Endpoint

```Python
 http://localhost:8080/user/api-token-auth/

```
 
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
* [x] Creation of Cycle (Authorization)
The registered user can create a cycle by making a POST request to the address below and with a payload in json format.
PS: This endpoint requires Token Authentication. The generated token in the requested above can be passed into the headers in the format.
Endpoint

```Python
http://localhost:8080/menstruation

```



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
A response is received in the format below.

 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```

* [x] Updating of Cycle (Authorization)
The registered user can create a cycle by making a PUT request to the address below and with a payload in json format which will update user information.
PS: This endpoint also requires Token Authentication. Follow as shown above.
Endpoint

```Python
[put]  http://localhost:8080/menstruation

```

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

A response containing the name of the user and an updated total_created_cycles will be returned.
 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```
* [x] Listing of Cycle Events (Authorization)
The registered user can view their current cycle events by making a GET request to the address below and without any payload but a path parameter of <i>date</i> needs to be provided in the url.
PS: This endpoint also requires Token Authentication.
Endpoint

```Python
http://localhost:8080/menstruation-list?date=2020-06-20

```

 ```Python
 Headers

"Authorization" : "Token <generated_token>"

```

A response containing the event will be returned.
Expected result has been displayed below
 ```Python
 Response

{
    "total_created_cycles for Anna": 15
}

```

