#GET
import requests
api_url = "https://reqres.in/api/unknown/2"
response = requests.get(api_url)
print(response.json())
response.status_code

if response.status_code == 200 : 
    print("200 response: page found")

elif response.status_code == 404 :
    print("404 response: page not found")

elif response.status_code == 400 :
    print("400: response delayed")


#POST
import requests
api_url = "https://reqres.in/api/login"
todo = {
   "email": "eve.holt@reqres.in",
    "password": "cityslicka"
}
response = requests.post(api_url, json=todo)
print(response.json())
response.status_code


if response.status_code == 201 : 
    print("201 response:post page found")

elif response.status_code == 200 :
    print("200 response: post request confirm")

elif response.status_code == 400 :
    print("400: post not found")


