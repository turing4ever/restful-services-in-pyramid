from pyramid import testing
from restful_auto_service.api.auto_api import all_autos


def test_all_autos_forbidden():
    request = testing.DummyRequest()
    resp = all_autos(request)
    err = b'You must specify an Authorization header.'
    assert 403 == resp.status_code
    assert err in resp.body


def test_all_auto_allowed():
    pass