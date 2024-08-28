import time

from selenium.common import NoSuchElementException

from game_state import get_game_state
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://playfootball.games/footy-tic-tac-toe/random/')

time.sleep(5)

consent_button = driver.find_elements(By.XPATH,
                                      "//button[contains(@class, 'fc-button fc-cta-consent fc-primary-button')]")
if len(consent_button) > 0:
    consent_button[0].click()

my_turn = "//div[contains(@class, 'flex items-center') and contains(text(), 'YOUR TURN')]"  # XPATH for user turn
opp_turn = "//div[contains(@class, 'flex items-center') and contains(text(), 'THEIR TURN')]"  # XPATH for opponent turn

game_squares = {
    "0": {
        "XPath": None,
        "Conditions": [3, 0],
        "Path": "board/square_0.png"
    },
    "1": {
        "XPath": None,
        "Conditions": [3, 1],
        "Path": "board/square_1.png"
    },
    "2": {
        "XPath": None,
        "Conditions": [3, 2],
        "Path": "board/square_2.png"
    },
    "3": {
        "XPath": None,
        "Conditions": [4, 0],
        "Path": "board/square_3.png"
    },
    "4": {
        "XPath": None,
        "Conditions": [4, 1],
        "Path": "board/square_4.png"
    },
    "5": {
        "XPath": None,
        "Conditions": [4, 2],
        "Path": "board/square_5.png"
    },
    "6": {
        "XPath": None,
        "Conditions": [5, 0],
        "Path": "board/square_6.png"
    },
    "7": {
        "XPath": None,
        "Conditions": [5, 1],
        "Path": "board/square_7.png"
    },
    "8": {
        "XPath": None,
        "Conditions": [5, 2],
        "Path": "board/square_8.png"
    }
}


def check_element_presence(by, path):
    elements = driver.find_elements(by, path)
    return len(elements) > 0


opp_turn_over = False

while True:
    time.sleep(0.5)

    try:
        close_button = driver.find_element(By.XPATH, '//g[@id="assets"]/polygon')
        close_button.click()
    except NoSuchElementException:
        pass

    if check_element_presence(By.XPATH, my_turn):
        print("YOUR TURN")

        cond_elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'font-bebas-neue') and (contains(@class, "
                                                    "'text-xl') or contains(@class, 'text-center'))]")

        all_conditions = []
        game_state = []

        buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'headlessui-popover-button-')]")
        id_list = []

        for button in buttons:
            button_id = button.get_attribute("id")
            id_list.append(button_id)

        for key, square in game_squares.items():
            square['XPath'] = id_list[int(key)]
            try:
                play_button = driver.find_element(By.ID, square["XPath"])
                play_button.screenshot(f'board/square_{key}.png')
                game_state.append(get_game_state(square["Path"]))
            except NoSuchElementException:
                print("Play Button not found.")
        print(game_state)

        for cond_elem in cond_elems:
            all_conditions.append(cond_elem.text)

        for key, square in game_squares.items():
            if check_element_presence(By.ID, square["XPath"]):
                play_button = driver.find_element(By.ID, square["XPath"])
                if not play_button.get_attribute("disabled"):
                    con_one = square["Conditions"][0]
                    con_two = square["Conditions"][1]
                    condition = (all_conditions[con_one], all_conditions[con_two])
                    print(condition)
                    selected_button = play_button
                    play_button.click()
                    break

        try:
            input_box = driver.find_element(By.XPATH, "//input[@placeholder='Search player...']")
            input_box.send_keys('Zinedine Zidane')
            first_option = driver.find_element(By.XPATH, "//li[@role='option' and @data-suggestion-index='0']")
            first_option.click()
        except:
            print("Player not found")

        opp_turn_over = False

    elif check_element_presence(By.XPATH, opp_turn) and not opp_turn_over:
        print("THEIR TURN")

        game_state = []

        try:
            player_name = selected_button.find_element(By.XPATH, ".//div[@class='text-white text-md font-bebas-neue "
                                                                 "truncate max-w-full h-6 mt-1 max-w-full']")
            print(player_name.text)
        except:
            print("Player not found")

        for key, square in game_squares.items():
            try:
                play_button = driver.find_element(By.ID, square["XPath"])
                play_button.screenshot(f'board/square_{key}.png')
                game_state.append(get_game_state(square["Path"]))
            except NoSuchElementException:
                print("Not found")
        print(game_state)

        opp_turn_over = True

        # if player_input.lower() in player_name.text.lower():
        #     symbol =

    elif not check_element_presence(By.XPATH, opp_turn) and not check_element_presence(By.XPATH, my_turn):
        print("Game has not started yet")
        start_game = driver.find_elements(By.XPATH,
                                          "//button[contains(@class, 'rounded-md') and contains(text(), 'Without "
                                          "Steals')]")
        if len(start_game) > 0:
            try:
                start_game[0].click()
            except:
                print('Play button not found.')
