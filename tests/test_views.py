import pytest


def test_api_parse_succeeds(client, success_response):
    # TODO: Finish this test. Send a request to the API and confirm that the
    # data comes back in the appropriate format.
    address_string = '123 main st chicago il'
    response = client.get('/api/parse/', {'address': address_string })

    assert response.status_code == 200
    assert response.json() == success_response
    # pytest.fail()


def test_api_parse_raises_error(client, error_response):
    # TODO: Finish this test. The address_string below will raise a
    # RepeatedLabelError, so ParseAddress.parse() will not be able to parse it.
    address_string = '123 main st chicago il 123 main st'

    response = client.get('/api/parse/', {'address': address_string })

    assert response.status_code == 400
    assert response.json() == error_response

    # pytest.fail()
