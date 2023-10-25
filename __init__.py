import requests
import json
import time
import re

url_pattern = re.compile(r'https?://[^\s>"]+|www\.[^\s>"]+')

headers = {'User-Agent': 'TempMailPuppeteerAPI/1.0', 'Accept': 'application/json'}


def mail():
    response = requests.get('https://api.tempmail.lol/generate/rush', headers=headers)
    data = json.loads(response.text)
    return data['address'], data['token']


def get_email_body(email_data):
    if len(email_data['body']) < 50:
        return email_data['html']
    else:
        return email_data['body']


def check_mail(auth = "", url=1):
    while True:
        response = requests.get(f'https://api.tempmail.lol/auth/{auth}', headers=headers)
        email = json.loads(response.text)['email']

        if len(email) > 0:
            email_data = email[0]
            if url == 2:
                data = get_email_body(email_data)
                match = url_pattern.search(data)
                if match:
                    return match.group()
                else:
                    return f"no url found {data} {email_data}"
            elif url == 1:
                return get_email_body(email_data)
            elif url == 3:
                data = get_email_body(email_data)
                match = url_pattern.findall(data)
                if match:
                    return match
                else:
                    return f"no urls found: {data} {email_data}"


        time.sleep(5)