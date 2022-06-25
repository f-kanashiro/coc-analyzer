import requests
from config import getBearerToken, getClanTag

url = "https://api.clashofclans.com/v1/clans/" + getClanTag() + "/currentwar"

payload = ""
headers = {
  'Authorization': getBearerToken()
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)