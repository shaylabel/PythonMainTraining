import json

import requests

url_base = 'https://petstore.swagger.io/v2/'
headers = {'Content-Type': 'application/json'}
user = {
    "id": 3333,
    "username": "user1",
    "firstName": "John",
    "lastName": "David",
    "email": "abc@gmail.com",
    "password": "123456",
    "phone": "054123456",
    "userStatus": 0
}


def test_get_status_code():
    response =requests.get(url_base+'pet/1245')
    assert  response.status_code == 200


def test_get_body():
    response =requests.get('https://petstore.swagger.io/v2/pet/1245')
    json_as_dict = response.json()    # get data from the response as dictionary
    id = json_as_dict ['id']   # getting specific field
    category = json_as_dict['category']  # getting object as dictionary from response
    name = json_as_dict['category']['name'] # getting field from object as dictionary
    assert name =='xyz'
    assert id == 1245

def test_post():

   response = requests.post(url_base+'user',headers=headers, data=json.dumps(user))
   response_code = response.status_code
   assert response_code == 200


def test_post_update():

   response = requests.post(url_base+'user',headers=headers, data=json.dumps(user))
   response_code = response.status_code
   assert response_code == 200
   code_from_res_body = response.json()["code"]
   # the body at response is
   # {
#     "code": 200,
#     "type": "unknown",
#     "message": "6874986831"
# }
   assert code_from_res_body == 200