import json

import requests

from PythonCharm.Python.api import api_post as post

def test_post():
    post.test_post_headers_body_json()
    print('\n #stop post test # ')

def test_get():
    r = requests.get('https://petstore.swagger.io/v2/pet/1245')
    respnse_body=r.json()
    # json.dump(respnse_body)
    json.dumps(respnse_body)
    l=len(respnse_body)

    print ("test pass")