from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from util.game_state import get_board_state


def user_turn(driver, game_squares):
    """
    Function to perform actions during the user's turn
    """
    # The content of these lists can change every new turn so need to be reset everytime
    all_conditions = []
    game_state = []
    id_list = []

    # Finding conditions and game squares for current board
    cond_elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'font-bebas-neue') and (contains(@class, "
                                                "'text-xl') or contains(@class, 'text-center'))]")

    buttons = driver.find_elements(By.XPATH, "//button[contains(@id, 'headlessui-popover-button-')]")

    # Appending our lists
    for cond_elem in cond_elems:
        all_conditions.append(cond_elem.text)

    for button in buttons:
        button_id = button.get_attribute("id")
        id_list.append(button_id)

    for key, square in game_squares.items():
        square['XPath'] = id_list[int(key)]
        try:
            play_button = driver.find_element(By.ID, square["XPath"])
            play_button.screenshot(f'board/square_{key}.png')
            game_state.append(get_board_state(square["Path"]))
        except NoSuchElementException:
            print("Play Button not found.")
    print(game_state)

    # Making our move
    for key, square in game_squares.items():
        play_button = driver.find_element(By.ID, square["XPath"])
        if not play_button.get_attribute("disabled"):
            con_one = square["Conditions"][0]
            con_two = square["Conditions"][1]
            condition = (all_conditions[con_one], all_conditions[con_two])
            print(condition)
            play_button.click()
            break

    try:
        input_box = driver.find_element(By.XPATH, "//input[@placeholder='Search player...']")
        input_box.send_keys('Zinedine Zidane')
        first_option = driver.find_element(By.XPATH, "//li[@role='option' and @data-suggestion-index='0']")
        first_option.click()
    except:
        print("Player not found")
