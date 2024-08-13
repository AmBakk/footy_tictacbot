import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('https://playfootball.games/footy-tic-tac-toe/random/')

time.sleep(15)

consent_button = driver.find_element(By.XPATH, "//button[contains(@class, 'fc-button fc-cta-consent fc-primary-button')]")
consent_button.click()

button = driver.find_element(By.XPATH, "//button[contains(@class, 'rounded-md') and contains(text(), 'Without Steals')]")
button.click()

input("Press Enter to close the browser...")

