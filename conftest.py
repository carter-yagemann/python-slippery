import pytest

def pytest_addoption(parser):
    parser.addoption('--tor-test', action='store', default='0',
                     help='--tor-test=[0,1]')

@pytest.fixture
def tor_test(request):
    return request.config.getoption('--tor-test')
