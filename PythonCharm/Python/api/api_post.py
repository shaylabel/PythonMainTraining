import requests
import json


def test_post_headers_body_json():
    url = 'https://httpbin.org/post'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {'key1': 1, 'key2': 'value2'}

    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))


    assert resp.status_code == 200, "Response code is not as expected "

    resp_body = resp.json()
    assert resp_body['url'] == url
