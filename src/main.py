from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import platform
import time

# ----- Detect OS and web driver -----
os = platform.system()
if os == 'Darwin': # Using Mac OS
    print(f"OS detected: {os}")
    driver = webdriver.Safari()

# ----- Other setup -----
action = ActionChains(driver)

# ----- Open window -----
driver.set_window_size(1000,800)
driver.set_window_position(0, 0)
url = "https://www.chess.com/play/online"
driver.get(url)
print('Url loaded.')

# ----- Click Play -----
time.sleep(1)
try:
    play_btn = driver.find_element(By.XPATH, "//button[@data-cy='new-game-index-play']")
    print('Play button found.')
    action.move_to_element(play_btn).click().perform()
    print('Clicked Play')
except NoSuchElementException:
    print('Play button not found')

# ----- Choose difficulty -----
time.sleep(1)
try:
    difficulty = 'advanced' # new, beginner, intermediate, advanced
    difficulty_btn = driver.find_element(By.XPATH, f"//label[@for='{difficulty}']")
    print('Difficulty button found.')
    action.move_to_element(difficulty_btn).click().perform()
    print('Difficulty selected.')
except NoSuchElementException:
    print('Difficulty button not found')

# ----- Click Play as Guest -----
time.sleep(1)
try:
    play_guest_btn = driver.find_element(By.ID, "guest-button")
    print('Play as Guest button found.')
    action.move_to_element(play_guest_btn).click().perform()
except NoSuchElementException:
    print('Play as Guest button not found')

# ----- Close the window -----
time.sleep(5)
driver.close()