from pages.try_sql_page import TrySqlPage


def test_request_select_all(browser):
    link = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
    page = TrySqlPage(browser, link)
    page.open()

    test_query = "SELECT * FROM Customers;"
    page.send_query(test_query)

    page.should_be_result_table()
    page.checking_column_values_in_a_row({'CustomerName': 'Split Rail Beer & Ale', 'City': 'Lander'})


def test_request_with_query(browser):
    link = "https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all"
    page = TrySqlPage(browser, link)
    page.open()

    test_query = "SELECT * FROM Customers WHERE City='London';"
    page.send_query(test_query)

    assert len(page.get_all_table_rows()) == 6, 'Number costumers where citi = London should be 6'
