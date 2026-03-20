
url="https://wttr.in/Hyderabad"
response=requests.get(url,params={"format":j1})
print(response)
data=response.json()
print(data)