import requests
import json
import time
import subprocess
from datetime import datetime
import os

USER = "ubntCSE"
PASS = "Crashcart123$"

amdata_path = os.path.join("data","amdata")
status_path = os.path.join("data","status")
airview_path = os.path.join("data","airviewdata")
iperf_path = os.path.join("data","iperf")

while(True):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = timestamp.replace(':','-')

    login_data = {
        'username': USER,
        'password': PASS
    }

    au=("ubntCSE","Champion@1")

    s = requests.Session()
    s.post("https://10.1.1.2/api/auth",data=login_data,verify=False)

    amdata_r = s.get("https://10.1.1.2/amdata.cgi", verify=False)

    with open(os.path.join(amdata_path, "amdata_data " + timestamp + ".json"), "w", encoding='utf-8') as amdata_file:
        json.dump(amdata_r.json(), amdata_file, indent=4)

    airview_r = s.get("https://10.1.1.2/airviewdata.cgi", verify=False)

    with open(os.path.join(airview_path,"airview_data " + timestamp + ".json"), "w", encoding='utf-8') as airview_file:
        json.dump(airview_r.json(), airview_file, indent=4)

    status_r = s.get("https://10.1.1.2/status.cgi", verify=False)

    with open(os.path.join(status_path, "status_data " + timestamp + ".json"), "w", encoding='utf-8') as status_file:
        json.dump(status_r.json(), status_file, indent=4)

    print("Webpage results saved json files")
    print("____________________________________")
    print("Almog was here... HAha~")
    print("____________________________________")

    time.sleep(10)
