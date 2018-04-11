import requests

url = 'http://127.0.0.1:5000/host/add'

data = '{"hostname": "docker02.woodez.net", "vcpu": 4, "sshd": "NOTOK", "inthealth": "OK", "hpsa": "OK", ' \
       '"commvault": "OK", "rootspace": 48}'

response = requests.post(url, data=data)

if response.ok:
    exit(0)
else:
    exit(1)