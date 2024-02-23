from requests import post
from time import sleep, strftime, localtime

channels = ["815330183648378932", "960875498479681557", "931970787890561128"]
headers = {"Authorization": "YOUR_TOKEN", "Content-Type": "application/json"}
data = {"content": "Its noon my nigga"}

while(True):
    current_time = strftime("%H:%M", localtime())
    if current_time == "12:00":
        for channel in channels:
            resp = post(f"https://discord.com/api/v9/channels/{channel}/messages", headers=headers, json=data)
            print(resp.status_code)
            sleep(1)
    else:
        print("not noon yet")
    sleep(60)