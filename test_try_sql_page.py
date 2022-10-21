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
        test_data = {
            'CustomerName': 'Split Rail Beer & Ale',
            'City': 'Lander'
        }
        test_query = "SELECT * FROM Customers;"
        self.page.send_query(test_query)

        self.page.should_be_result_table()
        self.page.checking_column_values_in_a_row(test_data)

    def test_request_with_query(self) -> None:
        test_data = {
            'City': 'London',
        }
        test_query = f"SELECT * FROM Customers WHERE City='{test_data['City']}';"
        self.page.send_query(test_query)

        assert len(self.page.get_all_table_rows()) == 6, f"Number costumers where " \
                                                         f"City = {test_data['City']} should be 6"

    def test_create_a_new_row(self) -> None:
        test_data = {
            # 'CustomerID': '2',
            'CustomerName': 'Nikita',
            'ContactName': 'Varlok',
            'Address': 'Mangilik',
            'City': 'Astana',
            'PostalCode': '123456',
            'Country': 'Kazakhstan'
        }
        quote = "'"
        test_query = f"INSERT INTO Customers ({', '.join(f'{column}' for column in test_data.keys())}) VALUES " \
                     f"({', '.join(f'{quote}{value}{quote}' for value in test_data.values())});"
        self.page.send_query(test_query)
        self.page.check_request_confirmation_message()
        test_query = f"SELECT * FROM Customers WHERE CustomerName='{test_data['CustomerName']}'"

        self.page.send_query(test_query)
        self.page.checking_column_values_in_a_row(test_data)

    def test_update_row(self) -> None:
        test_data = {
            # 'CustomerID': '2',
            'CustomerName': 'Nikita',
            'ContactName': 'Varlok',
            'Address': 'Mangilik',
            'City': 'Astana',
            'PostalCode': '123456',
            'Country': 'Kazakhstan'
        }
        quote = "'"
        test_query = f"UPDATE Customers SET " \
                     f"{', '.join(f'{item[0]}={quote}{item[1]}{quote}' for item in test_data.items())} " \
                     f"WHERE CustomerID=2;"
        self.page.send_query(test_query)
        self.page.check_request_confirmation_message()
        test_query = "SELECT * FROM Customers WHERE CustomerID=2;"
        self.page.send_query(test_query)
        self.page.checking_column_values_in_a_row(test_data)
