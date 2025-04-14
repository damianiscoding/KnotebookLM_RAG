import requests
import json


t = open("text.txt", "r")
text = t.read()


base_url = "http://127.0.0.1:5000" 
path = "/new"
url = base_url + path

data = { "text": text, "notebook_id": "a4yQ-45v35-wqp4", "doc_id": "892", "user_id": "22"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
