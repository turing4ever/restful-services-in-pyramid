from pyramid import testing
import webtest
import pytest

from restful_auto_service import main
from pyramid.paster import get_appsettings


@pytest.fixture(scope='session')
def pyramid_testing_setup(request):
    def fin():
        testing.tearDown()

    request.addfinalizer(fin)
    request = testing.DummyRequest()
    return testing.setUp(request=request)


@pytest.fixture(scope='session')
def pyramid_server(pyramid_testing_setup):
    settings = get_appsettings('development.ini', name='main')
    return webtest.TestApp(main({}, **settings))
