from pages.base_page import BasePage
from locators import TrySqlPageLocators
from selenium import webdriver
from conftest import logger


class TableResults:
    def get_columns_names(self) -> dict[str: int]:
        column_names = self.browser.find_element(*TrySqlPageLocators.TABLE_NAMES_OF_COLUMNS).text.split()
        column_names = dict(zip(column_names, range(0, len(column_names))))
        return column_names

    def get_all_table_rows(self) -> tuple[tuple[str, ...], ...]:
        rows = self.browser.find_elements(*TrySqlPageLocators.TABLE_ROW)
        return tuple(tuple(column.text for column in row.find_elements(*TrySqlPageLocators.TABLE_COLUMN)
                           ) for row in rows[1:])

    def checking_column_values_in_a_row(self, cells: dict) -> None:
        """For check need dictionary of columns values:
        {'name_of_column': 'value_of_column'}"""
        indexes = self.get_columns_names()
        for column_name, value in cells.copy().items():
            assert column_name in indexes, 'Name of column not found in the table'
            cells[indexes[column_name]] = cells.pop(column_name)
        rows = self.get_all_table_rows()

        for row in rows:
            if all(map(lambda item: row[item[0]] == item[1], cells.items())):
                logger.info(f'{cells.values()} found in row № {row[0]}')
                break
        else:
            raise ValueError('Cell not found in table')
