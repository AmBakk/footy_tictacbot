from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def get_usr_symbol(square, driver):
    button_id = square['XPath']
    try:
        button = driver.find_element(By.ID, button_id)

        inner_div = button.find_element(By.XPATH, ".//div[contains(@class, 'font-bebas-neue') and (contains(@style, "
                                                  "'color: rgb(255, 255, 255);') or contains(@style, 'color: rgb(0, 0, "
                                                  "0);'))]")

        marker = inner_div.text

        return marker
    except NoSuchElementException:
        print(f"Button with ID {button_id} or the inner div was not found.")

        # Close the browser



