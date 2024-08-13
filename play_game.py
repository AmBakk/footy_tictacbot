import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://playfootball.games/footy-tic-tac-toe/random/')

time.sleep(5)

consent_button = driver.find_elements(By.XPATH,
                                     "//button[contains(@class, 'fc-button fc-cta-consent fc-primary-button')]")
if len(consent_button) > 0:
    consent_button[0].click()

my_turn = "//div[contains(@class, 'flex items-center') and contains(text(), 'YOUR TURN')]"  # XPATH for user turn
opp_turn = "//div[contains(@class, 'flex items-center') and contains(text(), 'THEIR TURN')]"  # XPATH for opponent turn

squares_ids = ["headlessui-popover-button-1", "headlessui-popover-button-3",
               "headlessui-popover-button-5", "headlessui-popover-button-7",
               "headlessui-popover-button-9", "headlessui-popover-button-11",
               "headlessui-popover-button-13", "headlessui-popover-button-15",
               "headlessui-popover-button-17"]


def check_element_presence(xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    return len(elements) > 0


while True:
    time.sleep(0.5)
    if check_element_presence(my_turn):
        print("YOUR TURN")
        for square_id in squares_ids:
            play_button = driver.find_elements(By.ID, square_id)
            if not play_button[0].get_attribute("disabled"):
                play_button[0].click()
                break
        input_box = driver.find_element(By.XPATH, "//input[@placeholder='Search player...']")
        input_box.send_keys('Zinedine Zidane')
        first_option = driver.find_element(By.XPATH, "//li[@role='option' and @data-suggestion-index='0']")
        first_option.click()
    elif check_element_presence(opp_turn):
        print("THEIR TURN")
    else:
        print("Game has not started yet")
        start_game = driver.find_elements(By.XPATH,
                                          "//button[contains(@class, 'rounded-md') and contains(text(), 'Without Steals')]")
        if len(start_game) > 0:
            start_game[0].click()
