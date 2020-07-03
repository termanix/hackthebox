import requests, base64

url = requests.post("https://www.hackthebox.eu/api/invite/generate", headers={"User-Agent":"HTB User"})
b64c = url.json()["data"]["code"]
print("Here is your HTB Invite Code: ", base64.b64decode(b64c).decode('utf-8'))