import pytest
from pages.try_sql_page import TrySqlPage


class TestSqlPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
        self.page = TrySqlPage(browser, link)
        self.page.open()
        yield

    def test_request_select_all(self) -> None:
        test_query = "SELECT * FROM Customers;"
        self.page.send_query(test_query)

        self.page.should_be_result_table()
        self.page.checking_column_values_in_a_row({'CustomerName': 'Split Rail Beer & Ale', 'City': 'Lander'})

    def test_request_with_query(self) -> None:
        test_query = "SELECT * FROM Customers WHERE City='London';"
        self.page.send_query(test_query)

        assert len(self.page.get_all_table_rows()) == 6, 'Number costumers where city = London should be 6'

    def test_create_a_new_entry(self) -> None:
        test_query = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country" \
                     ") VALUES ('Nikita', 'Varlok', 'Mangilik', 'Astana', '123456', 'Kazakhstan');"
        self.page.send_query(test_query)
        self.page.check_request_confirmation_message()

        test_query = "SELECT * FROM Customers WHERE CustomerName='Nikita'"

        self.page.send_query(test_query)
        self.page.checking_column_values_in_a_row({'CustomerName': 'Nikita', 'ContactName': 'Varlok', 'City': 'Astana'})
