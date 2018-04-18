import requests

# defining the api-endpoint
API_ENDPOINT = "http://192.168.2.213:5000/host/add"

# your API key here
API_KEY = "XXXXXXXXXXXXXXXXX"


def send_data(**data):
    r = requests.post(url=API_ENDPOINT, json=data)
    return {'status': r.status_code, 'outlog': r.text}



######### example usage ##########
# data to be sent to api
data = {'hostname': 'saltmaster01',
            'vcpu': 2,
            'sshd': 'OK',
            'inthealth': 'OK',
            'commvault': 'OK',
            'rootspace': 90}

ret_code = send_data(**data)
print(ret_code.get('status', None))
