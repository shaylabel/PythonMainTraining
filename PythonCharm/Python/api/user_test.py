import json

import requests

from PythonCharm.Python.api import api_post as post

headers = {'Content-Type': 'application/json'}


def test_post_create_user():
    print('\n #stop post test # ')
    url = "https://petstore.swagger.io/v2/user/kd"
    payload='{"id": 0,"username": "kd","firstName": "koby","lastName": "d","email": "koby@gmail.com","password": "111","phone": "111111","userStatus": 0}'

    post.test_post_headers_body_json()
    x = requests.put(url, headers=headers, data=json.dumps(payload, indent=4))
    print ("test pass")

def test_post_create_user1():
    print('\n #stop post test # ')
    url = "https://petstore.swagger.io/v2/user/kd"
    payload='{"id": 0,"username": "kd","firstName": "koby","lastName": "d","email": "koby@gmail.com","password": "111","phone": "111111","userStatus": 0}'

    post.test_post_headers_body_json()
    x = requests.put(url, headers=headers, data=json.dumps(payload, indent=4))
    print ("test pass")



def test_post_headers_body_json():
    url = "https://petstore.swagger.io/v2/user/kd"

    # Additional headers.
    headers = {'Content-Type': 'application/json','accept': 'application/json'}

    # Body
    payload = {'id':1, 'username':'kd','firstName':'koby','lastName':'koby','email':'koby@gmail.com','password':'1q2w','phone':'123456','userStatus':0}
    payload1= {'username': 'ddd', 'firstName': 'value2'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload1, indent=4))

    assert resp.status_code == 200, "Response code is not as expected "

    resp_body = resp.json()
    assert resp_body['url'] == url