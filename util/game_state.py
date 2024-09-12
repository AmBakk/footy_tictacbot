import time

import cv2
import numpy as np
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


def open_game(driver):
    driver.get('https://playfootball.games/footy-tic-tac-toe/random/')

    time.sleep(5)

    driver.execute_script("window.scrollBy(0, 250);")
    driver.maximize_window()

    consent_button = driver.find_elements(By.XPATH,
                                          "//button[contains(@class, 'fc-button fc-cta-consent fc-primary-button')]")
    if len(consent_button) > 0:
        consent_button[0].click()


def get_board_state(image_path):
    """
    Using screenshots of each board square to assess the current board state
    """
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to HSV (Hue, Saturation, Value) color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Focus on the central region where the shirt is likely to be
    h, w, _ = hsv_image.shape
    shirt_region = hsv_image[int(h*0.25):int(h*0.75), int(w*0.25):int(w*0.75)]

    # Define color range for detecting blue (O)
    blue_lower = np.array([100, 100, 50])
    blue_upper = np.array([140, 255, 255])

    # Define color range for detecting white (X)
    white_lower = np.array([0, 0, 160])
    white_upper = np.array([180, 40, 255])

    # Create masks for blue and white colors
    blue_mask = cv2.inRange(shirt_region, blue_lower, blue_upper)
    white_mask = cv2.inRange(shirt_region, white_lower, white_upper)

    # Count the number of pixels in each mask
    blue_pixels = cv2.countNonZero(blue_mask)
    white_pixels = cv2.countNonZero(white_mask)

    # Determine the color with the most pixels
    if blue_pixels > white_pixels:
        return 'O'
    elif white_pixels > blue_pixels:
        return 'X'
    else:
        return ''


def check_new_game(previous_board, current_board):
    if all(square == '' for square in current_board) and any(square != '' for square in previous_board):
        return True


def get_current_score(driver):
    """
    Get the score for the current game
    """
    try:
        score_element = driver.find_element(By.XPATH,
                                            "//div[contains(@class, 'text-black font-black bg-green-400')]")

        score_text = score_element.text.strip()

        user_score, opponent_score = score_text.split('-')

        # Convert to integers
        user_score = int(user_score)
        opponent_score = int(opponent_score)
        print(f"Current score : {user_score} - {opponent_score}")

        return user_score, opponent_score

    except NoSuchElementException:
        print("Score element not found.")
        return None, None


def check_winner(driver, previous_user_score, wins, losses):
    user_score, opponent_score = get_current_score(driver)

    # Check if you're currently winning
    winning = user_score > opponent_score

    # Check if the game has ended
    if user_score == 3:
        wins += 1
        print(f"You Won!\n{wins} - {losses}")
    elif opponent_score == 3:
        losses += 1
        print(f"You Lost!\n{wins} - {losses}")
    elif user_score < previous_user_score and winning:
        wins += 1
        print(f"Opponent left. You Won!\n{wins} - {losses}")

    return user_score, opponent_score, winning, wins, losses


def check_element_presence(driver, by, path):
    elements = driver.find_elements(by, path)
    return len(elements) > 0


# def check_new_round(driver, previous_conditions=None):
#     if previous_conditions is None:
#         previous_conditions = []
#
#     new_conditions = []
#     cond_elems = driver.find_elements(By.XPATH, "//div[contains(@class, 'font-bebas-neue') and (contains(@class, "
#                                                 "'text-xl') or contains(@class, 'text-center'))]")
#
#     for cond in cond_elems:
#         new_conditions.append(cond.text)
#
#     if previous_conditions != new_conditions:
#         print(previous_conditions, new_conditions)
#         print('new round')
#         return True, new_conditions.copy()
#
#     print('no new round')
#     return False, previous_conditions

