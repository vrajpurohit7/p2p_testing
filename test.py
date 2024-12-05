import requests
import json
import subprocess
from datetime import datetime

USER = "ubntCSE"
PASS = "Crashcart123$"

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
timestamp = timestamp.replace(':','-')

# login_data = {
#     'username': USER,
#     'password': PASS
# }

# au=("ubntCSE","Champion@1")

# s = requests.Session()
# s.post("https://10.1.1.2/api/auth",data=login_data,verify=False)


# with open("amdata_data " + timestamp + ".json", "w", encoding='utf-8') as amdata_file:
#     json.dump(amdata_r.json(), amdata_file, indent=4)

# airview_r = s.get("https://10.1.1.2/airviewdata.cgi", verify=False)

# with open("airview_data " + timestamp + ".json", "w", encoding='utf-8') as airview_file:
#     json.dump(airview_r.json(), airview_file, indent=4)

# status_r = s.get("https://10.1.1.2/status.cgi", verify=False)

# with open("status_data " + timestamp + ".json", "w", encoding='utf-8') as status_file:
#     json.dump(status_r.json(), status_file, indent=4)


# print(r.status_code)
# print(s.cookies)
# print(r.json())

#### Function to run Iperf and capture the values (TCP, UDP, reverse TCP, reverse UDP)

# TCP Test
tcp_result = subprocess.check_output(["iperf3", "-c", "10.1.1.10", "-t", "10", "-i", "1", "-p", "5201"])
tcp_send = None
tcp_recv = None
for line in tcp_result.decode().splitlines():
    if "sender" in line:
        tcp_send = line
    if "receiver" in line:
        tcp_recv = line

print("step_1")

# UDP Test (for port 5201)
udp_result = subprocess.check_output(["iperf3", "-c", "10.1.1.10", "-u", "-b", "100M", "-t", "10", "-i", "1", "-p", "5201"])
udp_send = None
udp_recv = None
for line in udp_result.decode().splitlines():
    if "sender" in line:
        udp_send = line
    if "receiver" in line:
        udp_recv = line

print("step_2")

# Reverse TCP Test
reverse_tcp_result = subprocess.check_output(["iperf3", "-c", "10.1.1.10", "-t", "10", "-i", "1", "-p", "5201", "--reverse"])
reverse_tcp_send = None
reverse_tcp_recv = None
for line in reverse_tcp_result.decode().splitlines():
    if "sender" in line:
        reverse_tcp_send = line
    if "receiver" in line:
        reverse_tcp_recv = line

print("step_3")

# Reverse UDP Test
reverse_udp_result = subprocess.check_output(["iperf3", "-c", "10.1.1.10", "-u", "-b", "100M", "-t", "10", "-i", "1", "-p", "5201", "--reverse"])
reverse_udp_send = None
reverse_udp_recv = None
for line in reverse_udp_result.decode().splitlines():
    if "sender" in line:
        reverse_udp_send = line
    if "receiver" in line:
        reverse_udp_recv = line

# Organize the data into a dictionary
results = {
    "tcp": {
        "send": tcp_send,
        "recv": tcp_recv
    },
    "udp": {
        "send": udp_send,
        "recv": udp_recv
    },
    "reverse_tcp": {
        "send": reverse_tcp_send,
        "recv": reverse_tcp_recv
    },
    "reverse_udp": {
        "send": reverse_udp_send,
        "recv": reverse_udp_recv
    }
}

# Save the results to a JSON file
with open("iperf3_results " + timestamp + ".json", 'w') as json_file:
    json.dump(results, json_file, indent=4)

print("Results saved to iperf3_results.json")
