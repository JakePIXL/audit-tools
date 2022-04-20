import pytest
from audit_tools import SessionManager
from audit_tools.core.functions import export_file, import_file


@pytest.fixture()
def session():
    return SessionManager('test_file.csv')


def test_session_manager(session):
    assert session is not None
    assert session.products is not None
    assert session.count_product("29XPSPS8", 10)
    assert session.increase_product("29XPSPS8", 5)
    assert session.reduce_product("29XPSPS8", 5)
    assert session.get_product("29XPSPS8") is not None


def test_file_manager(session):
    assert import_file(file_path='test_file.csv') is not None
    assert export_file(session.file_type, None, session.products) is not None


