import requests
import pandas as pd

username = 'xxx' #your email address
password = 'xxx'
apiurl = 'xxx'

login_payload = {'username': username, 'password': password}

# use requests.Session() to handle cookies for you
req = requests.Session()

res = req.post(apiurl + 'xxx', json=login_payload)
# session cookies will be sent with subsequent calls to the API

topic_pl = req.get(apiurl + 'xxxx')
# topic_pl.json()['topics']

if topic_pl.status_code == 200:
    try:
        data = topic_pl.json()
        topics = data.get('topics', [])
        print(topics)
    except ValueError:
        print("Svar kunde inte tolkas som JSON.")
        print("Råtext från API:")
        print(topic_pl.text)
else:
    print(f"Något gick fel. Statuskod: {topic_pl.status_code}")
    print(topic_pl.text)




