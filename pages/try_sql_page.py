from pages.base_page import BasePage, logger
from table_results import TableResults
from locators import TrySqlPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TrySqlPage(BasePage, TableResults):
    def should_be_request_field(self) -> None:
        assert self.is_element_present(*TrySqlPageLocators.REQUEST_FIELD), "Request field is not presented"

    def should_be_button_run(self) -> None:
        assert self.is_element_present(*TrySqlPageLocators.BUTTON_RUN), "Run button is not presented"

    def should_be_result_table(self) -> None:
        assert self.is_element_present(*TrySqlPageLocators.RESULT_TABLE), "Result table is not presented"

    def check_request_confirmation_message(self):
        WebDriverWait(self.browser, 5).until(
            EC.text_to_be_present_in_element(
                TrySqlPageLocators.MESSAGE_FEEDBACK, 'You have made changes to the database'))

        # assert self.is_element_present(*TrySqlPageLocators.MESSAGE_FEEDBACK
        #                                ), "Confirmation massage after doing request is not found"
        message = self.browser.find_element(*TrySqlPageLocators.MESSAGE_FEEDBACK).text
        logger.info(f'Confirmation massage after doing request - {message}')

    def send_query(self, query: str) -> None:
        self.should_be_request_field()
        self.should_be_button_run()

        self.browser.execute_script(f'window.editor.doc.setValue("{query}")')
        button_run = self.browser.find_element(*TrySqlPageLocators.BUTTON_RUN)
        button_run.click()


        # self.should_be_request_field()
        # self.browser.execute_script("document.body.innerHTML = arguments[0]",
        #                  '<div class="CodeMirror-code" contenteditable="true" tabindex="5" style="height: 250px;"></div>')
        # request_field = self.browser.find_element(*TrySqlPageLocators.REQUEST_FIELD)
        # self.browser.execute_script("arguments[0].innerHTML='&nbsp;'", request_field)
        # request_field.click()
        # print('click')
        # request_field.clear()
        # self.browser.execute_script(f"return arguments[0].value={query};", request_field)
        # request_field.send_keys(query)

        # request_field.click()
        # request_field = self.browser.find_element(*TrySqlPageLocators.REQUEST_FIELD)
        # request_field.send_keys(query)

    # def get_all_table_rows(self):
    #     rows = self.browser.find_elements(*TrySqlPageLocators.TABLE_ROW)
    #     return tuple(tuple(column.text for column in row.find_elements(*TrySqlPageLocators.TABLE_COLUMN)
    #                        ) for row in rows[1:])

    # def should_be_result_frame(self):
    #     assert self.is_element_present(*TrySqlPageLocators.RESULT_FRAME), "Result frame is not presented"

    # def switch_to_result_frame(self):
    #     self.browser.switch_to.frame(self.browser.find_element(*TrySqlPageLocators.RESULT_FRAME))
    #
    # def switch_to_default_content(self):
    #     self.browser.switch_to.default_content()
