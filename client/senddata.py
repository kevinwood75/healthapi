import requests

# defining the api-endpoint
API_ENDPOINT = "http://192.168.2.242:5000/host/add"

# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"


# data to be sent to api
data = {'hostname': 'tfiadm1.woodez.net',
            'vcpu': 2,
            'sshd': 'OK',
            'inthealth': 'OK',
            'commvault': 'OK',
            'rootspace': 78}



# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, json=data)
if r.status_code != 200:
    exit(1)
else:
    exit(0)

# print(r.status_code, r.text)