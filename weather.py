#Task-1 remove Hardcoded API key
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.getenv("API_KEY") 

#Task-2 Handle Rate Limiting(429 error)


import requests
import time
urls=["https://wttr.in/Hyderabad",
         "https://wttr.in/Bangalore",
         "https://wttr.in/chennai" ]
try:
  for url in urls:
    response=requests.get(url,params={"format":"j1"})
    response.raise_for_status()
    data=response.json()
    print(data)
    time.sleep(5)
except requests.exceptions.HTTPError as http_err:
    if response.status_code == 429:
        print("Too many requests. Please wait a minute and try again.")
    else:
        print(f"HTTP error occurred: {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Network error. Please check your internet connection.")

except requests.exceptions.Timeout:
    print("Request timed out. Try again later.")

except Exception as err:
    print(f"Something went wrong: {err}")


     

        

    
    
    
except requests.exceptions.ConnectionError:
  print("error connecting to the server")
except requests.exceptions.HTTPError as e:
  print(f"HTTP error occured: {e}")
except requests.exceptions.TImeout:
  print("Requets timed out")
except requests.exceptions.RequestException as err:
  print(f"some other error occurred:{err}")
   




