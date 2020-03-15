import requests
import json

# API URL specific to POST requests
url = "https://reqres.in/api/users"

# read input json file - noted by the second 'r' argument
file = open('/Users/calebsaleh/API/GET_Request/CreateUser.json')
json_input = file.read()
request_json = json.loads(json_input)

print(request_json)