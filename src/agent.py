from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import platform
import time

class Agent:

    def init_window(self):
        # ----- Detect OS and web driver -----
        os = platform.system()
        if os == 'Darwin': # Using Mac OS
            print(f"OS detected: {os}")
            self.driver = webdriver.Safari()

        # ----- Other setup -----
        self.action = ActionChains(self.driver)

        # ----- Open window -----
        self.driver.set_window_size(1000,800)
        self.driver.set_window_position(0, 0)
        url = "https://www.chess.com/play/online"
        self.driver.get(url)
        print('Url loaded.')

    def start_match_from_main_url(self):
        # ----- Click Play -----
        time.sleep(1)
        try:
            play_btn = self.driver.find_element(By.XPATH, "//button[@data-cy='new-game-index-play']")
            print('Play button found.')
            self.action.move_to_element(play_btn).click().perform()
            print('Clicked Play')
        except NoSuchElementException:
            print('Play button not found')

        # ----- Choose difficulty -----
        time.sleep(1)
        try:
            difficulty = 'advanced' # new, beginner, intermediate, advanced
            difficulty_btn = self.driver.find_element(By.XPATH, f"//label[@for='{difficulty}']")
            print('Difficulty button found.')
            self.action.move_to_element(difficulty_btn).click().perform()
            print('Difficulty selected.')
        except NoSuchElementException:
            print('Difficulty button not found')

        # ----- Click Play as Guest -----
        time.sleep(1)
        try:
            play_guest_btn = self.driver.find_element(By.ID, "guest-button")
            print('Play as Guest button found.')
            self.action.move_to_element(play_guest_btn).click().perform()
        except NoSuchElementException:
            print('Play as Guest button not found')

    def close_window(self):
        self.driver.close()