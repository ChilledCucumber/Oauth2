import requests
import json
import schedule
import time

auth = ("ababab-abab-abab-abab-0000000000", "ababab~aaaa.bABbababABAb_abBa00")
url = "https://login.microsoftonline.com/common/oauth2/v2.0/token"

params = {
  "grant_type":"refresh_token",
  "scope":"https://outlook.office365.com/.default",
  "refresh_token":"a_very_long_refresh_token"
}

def job():
    ret = requests.post(url, auth=auth, data=params)
    print(ret.text.encode('utf8'))
    access_key = ret.json()
    
    with  open("TOKEN.txt", "w") as f:
        f.write(str(access_key['access_token']))

schedule.every(50).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)

while 1:
    schedule.run_pending()
    time.sleep(1)

