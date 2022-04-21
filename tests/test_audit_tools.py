import pytest

from audit_tools import SessionManager
from audit_tools.core.functions import export_file, import_file


def test_session_manager():

    with SessionManager(testing=True) as session:
        assert session is not None

        session.import_data("test_file.csv")

        assert session.products is not None

        assert session.count_product("29XPSPS8", 10)
        assert session.increase_product("29XPSPS8", 5)
        assert session.reduce_product("29XPSPS8", 5)
        assert session.get_product("29XPSPS8") is not None

        session.parse_session_data()

        assert session.get_table_data().columns
        assert session.get_table_data(session.variance_items).columns
        assert session.get_table_data(session.missed_items).columns


def test_file_manager():
    products, file_type = import_file("test_file.csv")
    assert products is not None
    assert export_file(file_type, None, products) is not None
