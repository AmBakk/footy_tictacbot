import time
from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
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

squares_ids = {"headlessui-popover-button-1": [3, 0],
               "headlessui-popover-button-3": [3, 1],
               "headlessui-popover-button-5": [3, 2],
               "headlessui-popover-button-7": [4, 0],
               "headlessui-popover-button-9": [4, 1],
               "headlessui-popover-button-11": [4, 2],
               "headlessui-popover-button-13": [5, 0],
               "headlessui-popover-button-15": [5, 1],
               "headlessui-popover-button-17": [5, 2]
               }


def check_element_presence(xpath):
    elements = driver.find_elements(By.XPATH, xpath)
    return len(elements) > 0



while True:
    time.sleep(0.5)
    if check_element_presence(my_turn):
        print("YOUR TURN")
        cond_elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'font-bebas-neue') and (contains(@class, 'text-xl') or contains(@class, 'text-center'))]")
        all_conditions = []
        for cond_elem in cond_elems:
            all_conditions.append(cond_elem.text)
        for squares, conditions in squares_ids.items():
            condition = (all_conditions[conditions[0]], all_conditions[conditions[1]])
            print(condition)
            play_button = driver.find_element(By.ID, squares)
            if not play_button.get_attribute("disabled"):
                selected_button = play_button
                play_button.click()
                break
        try:
            input_box = driver.find_element(By.XPATH, "//input[@placeholder='Search player...']")
            player_input = input('Enter your player : ')
            input_box.send_keys(player_input)
            first_option = driver.find_element(By.XPATH, "//li[@role='option' and @data-suggestion-index='0']")
            first_option.click()
        except:
            print("Player not found")
    elif check_element_presence(opp_turn):
        print("THEIR TURN")
        try:
            player_name = selected_button.find_element(By.XPATH, ".//div[@class='text-white text-md font-bebas-neue truncate max-w-full h-6 mt-1 max-w-full']")
            print(player_name.text)
        except:
            print("Player not found")
        # if player_input.lower() in player_name.text.lower():
        #     symbol =
    else:
        print("Game has not started yet")
        start_game = driver.find_elements(By.XPATH,
                                          "//button[contains(@class, 'rounded-md') and contains(text(), 'Without "
                                          "Steals')]")
        if len(start_game) > 0:
            try:
                start_game[0].click()
            except:
                print('Play button not found.')
