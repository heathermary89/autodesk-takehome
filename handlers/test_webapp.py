import json
import webapp

client = webapp.app.test_client()
url = '/'

def test_get_request_success():
    mock_accept_header_json = {
        'Accept' : 'application/json',
    }

    mock_accept_header_empty = {}

    mock_accept_header_star = {
        'Accept' : '*/*'
    }

    response1 = client.get(url, headers=mock_accept_header_json)
    assert json.loads(response1.get_data()) == {"message":"Hello, World"}
    assert response1.status_code == 200

    response2= client.get(url, headers=mock_accept_header_empty)
    assert response2.get_data() == b'<p>Hello, World</p>'
    assert response2.status_code == 200

    response3 = client.get(url, headers=mock_accept_header_star)
    assert response3.get_data() == b''
    assert response3.status_code == 200


def test_get_request_failure_not_found():
    response = client.get('{url}*')
    assert response.status_code == 404


def test_post_request_success():
    mock_request_data = {
        'request_id': '123',
        'payload': {
            "this" : "that"
        }
    }

    response = client.post(url, data=json.dumps(mock_request_data))
    assert response.status_code == 200


def test_post_route_failure_bad_request():
    mock_request_data = {}

    response = client.post(url, data=json.dumps(mock_request_data))
    assert response.status_code == 400