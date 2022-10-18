from selenium.webdriver.common.by import By


class TrySqlPageLocators:
    # REQUEST_FIELD = (By.CLASS_NAME, 'CodeMirror-lines')
    REQUEST_FIELD = (By.ID, 'textareaCodeSQL')
    RESULT_FRAME = (By.ID, "iframeResultSQL")
    BUTTON_RUN = (By.CSS_SELECTOR, "button.ws-btn")

    RESULT_TABLE = (By.CSS_SELECTOR, "table.ws-table-all")
    TABLE_ROW = (By.CSS_SELECTOR, "table.ws-table-all tr")
    TABLE_COLUMN = (By.CSS_SELECTOR, "td")
    TABLE_NAMES_OF_COLUMNS = (By.CSS_SELECTOR, "table.ws-table-all tr:nth-child(1)")
    COLUMN_NAME = (By.CSS_SELECTOR, "th")

    # RESULT_TABLE = (By.CSS_SELECTOR, "iframeResultSQL")
    # RESULT_TABLE = (By.XPATH, "//table[@class='w3-table-all']")

    # CONFIRM_OF_ADD = (By.CSS_SELECTOR, "div.alertinner strong")
    # CONFIRM_OF_PRICE = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(3) strong")