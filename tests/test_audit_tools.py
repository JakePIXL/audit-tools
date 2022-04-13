import pytest

from audit_tools import __version__
from audit_tools.core import SessionManager


@pytest.fixture()
def session():
    return SessionManager('new_products_converted.csv')


def test_version():
    assert __version__ == '0.1.1'


def test_session_manager(session):
    assert session is not None
    assert session.products is not None
    assert session.count_product("29XPSPS8", 10)
    assert session.get_product("29XPSPS8") is not None


