import requests
from urllib.parse import urljoin

URL = 'http://localhost:5001'

def test_get_all_car_endpoint(client):
    """Get all cars from cars endpoint."""

    url = urljoin(URL, 'cars')
    resp = requests.get(url)
    status, resp_json = resp.status_code, resp.json()

    assert type(resp_json) is dict

def test_post_car_endpoint():
    """Get a car from cars endpoint."""

    url = urljoin(URL, 'cars')
    payload = {'make': 'mercedes'}
    resp = requests.post(url, json=payload)
    status, resp_json = resp.status_code, resp.json()
    
    assert 'error' in resp_json and resp_json['error'] == 'Model is required'
