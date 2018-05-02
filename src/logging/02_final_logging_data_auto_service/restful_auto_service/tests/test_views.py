
def test_home(pyramid_server):
    res = pyramid_server.get('/', status=200)
    assert b'/api/autos' in res.body


