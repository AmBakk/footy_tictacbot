import time

from util.game_state import check_winner, check_element_presence, open_game
from selenium import webdriver
from selenium.webdriver.common.by import By

from util.user_turn import user_turn

driver = webdriver.Chrome()

open_game(driver)

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

opp_turn_over = False
user_symbol = None
opp_symbol = None
prev_conditions = None

wins = 0
losses = 0
previous_user_score = 0
previous_opponent_score = 0

while True:
    time.sleep(0.5)

    if check_element_presence(driver, By.XPATH, my_turn):
        print("YOUR TURN")

        # new_round, prev_conditions = check_new_round(driver, previous_conditions=prev_conditions)

        if user_symbol is None and opp_symbol is None:
            user_symbol = 'X'
            print("You are X's")
            opp_symbol = 'O'

        user_turn(driver, game_squares, user_symbol)

        previous_user_score, previous_opponent_score, winning, wins, losses = check_winner(driver, previous_user_score, wins, losses)

        opp_turn_over = False

    elif check_element_presence(driver, By.XPATH, opp_turn) and not opp_turn_over:
        print("THEIR TURN")

        # new_round, prev_conditions = check_new_round(driver, previous_conditions=prev_conditions)

        if user_symbol is None and opp_symbol is None:
            user_symbol = 'O'
            print("You are O's")
            opp_symbol = 'X'

        opp_turn_over = True

    elif not check_element_presence(driver, By.XPATH, opp_turn) and not check_element_presence(driver, By.XPATH, my_turn):
        user_symbol = None
        opp_symbol = None
        print("Game has not started yet")
        start_game = driver.find_elements(By.XPATH,
                                          "//button[contains(@class, 'rounded-md') and contains(text(), 'Without "
                                          "Steals')]")
        if len(start_game) > 0:
            try:
                start_game[0].click()
            except:
                print('Play button not found.')
