import requests

# API URL
url = "https://reqres.in/api/users?page=2"

response = requests.delete(url)

# According to the site from which we're fetching the data, 
# we should receive a code 204 if it succeeds

print(response.status_code)

assert response.status_code == 204