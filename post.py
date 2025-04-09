import requests
import json


test_text = "The old, creaky windmill groaned under the weight of the relentless, whispering wind. A lone, rusty bicycle leaned against a weathered fence, its tires flat and forlorn. High above, a flock of crows, like scattered ink blots against the pale sky, wheeled in a silent, chaotic dance. A half-eaten apple, its skin bruised and brown, lay abandoned on a mossy stone. The air was thick with the scent of damp earth and decaying leaves, a melancholy fragrance that spoke of forgotten summers and the slow, inevitable march of time. A single, tattered page of a forgotten book fluttered across the overgrown path, its words obscured by dirt and time. A distant, muffled sound, like the echo of a forgotten melody, drifted on the breeze, a haunting whisper in the vast, quiet landscape."


base_url = "http://127.0.0.1:5000" 
path = "/new"
url = base_url + path

data = { "text": test_text, "notebook_id": "a4yQ-45v35-wqp4", "doc_id": "892", "user_id": "22"}
headers = {"Content-Type": "application/json"}
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 200:
    print("Request successful!")
    print(response.json())
else:
    print(f"Error: {response.status_code}")
    print(response.text)
