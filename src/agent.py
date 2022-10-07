from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import platform
import time
import chess_util

class Agent:

    def init_window(self):
        # ----- Detect OS and web driver -----
        os = platform.system()
        print(f"OS detected: {os}")
        if os == 'Darwin': # Using Mac OS
            self.driver = webdriver.Safari()
        elif os == 'Windows':
            self.driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

        # ----- Other setup -----
        self.action = ActionChains(self.driver)

        # ----- Open window -----
        self.driver.set_window_size(1400,700)
        self.driver.set_window_position(0, 0)
        url = "https://www.chess.com/play/online"
        self.driver.get(url)
        print('Url loaded.')

    def click_main_play_btn(self):
        try:
            play_btn = self.driver.find_element(By.XPATH, "//button[@data-cy='new-game-index-play']")
            print('Play button found.')
            self.action.move_to_element(play_btn).click().perform()
            print('Clicked Play')
        except NoSuchElementException:
            print('Play button not found')

    def start_match_from_main_url(self, difficulty):
        # ----- Click Play -----
        time.sleep(0.5)
        self.click_main_play_btn()

        # ----- Choose difficulty -----
        time.sleep(0.5)
        try:
            difficulty_btn = self.driver.find_element(By.XPATH, f"//label[@for='{difficulty}']")
            print('Difficulty button found.')
            self.action.move_to_element(difficulty_btn).click().perform()
            print('Difficulty selected.')
        except NoSuchElementException:
            print('Difficulty button not found')

        # ----- Click Play as Guest -----
        time.sleep(0.5)
        try:
            play_guest_btn = self.driver.find_element(By.ID, "guest-button")
            print('Play as Guest button found.')
            self.action.move_to_element(play_guest_btn).click().perform()
        except NoSuchElementException:
            print('Play as Guest button not found')

    def close_window(self):
        self.driver.close()

    def verify_existing_opponent(self):
        try:
            opponent_name = self.driver.find_element(By.CLASS_NAME, "user-username-link")
            #print('Opponent tagline found.')
            tag = opponent_name.get_attribute('innerHTML')
            return tag != 'Opponent'
        except NoSuchElementException:
            print('Opponent HTML not found.')
            return False

    def wait_n_secs_for_match_to_start(self, secs):
        for _ in range(secs):
            if self.verify_existing_opponent():
                print('Match started.')
                return True
            else:
                time.sleep(1)
        print('Match was not created.')
        return False

    def read_board(self):
        fen = ""
        for i in range(8, 0, -1):
            nums = 0
            for j in range(1, 9):
                try:
                    piece = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'piece') and contains(@class, 'square-{j}{i}')]")
                    fen += str(nums) if nums != 0 else ""
                    nums = 0
                    if piece.get_attribute("class").split()[1][0] != "s":
                        piece_name = piece.get_attribute("class").split()[1]
                    else:
                        piece_name = piece.get_attribute("class").split()[2]

                    fen += piece_name[1].upper() if piece_name[0] == "w" else piece_name[1].lower()
                except:
                    nums += 1

            fen += str(nums) if nums != 0 else ""
            nums = 0
            fen += "/"
        return fen[:-1]

    def check_is_game_over(self):
        try:
            game_over_modal = self.driver.find_element(By.CLASS_NAME, "game-over-modal-content")
            return True
        except NoSuchElementException:
            return False

    def make_move(self, move):
        if move != 'None':
            try:
                piece_size = self.driver.find_element(By.CSS_SELECTOR, "#board-layout-chessboard").size["height"]/8

                origin = chess_util.get_square_location(move[:2])
                target = chess_util.get_square_location(move[2:4])
                offset_x = piece_size * (int(target[0]) - int(origin[0])) + 5
                offset_y = piece_size * (int(target[1]) - int(origin[1])) + 5
                if self.is_agent_white():
                    offset_y *= -1
                else:
                    offset_x *= -1

                try:
                    origin_push = self.driver.find_element(By.XPATH, f"//div[contains(@class, 'piece') and contains(@class, 'square-{origin[0]}{origin[1]}')]")
                    self.action.drag_and_drop_by_offset(origin_push, offset_x, offset_y).perform()
                    
                except ElementNotInteractableException as e:
                    print(f'Could not interact: {str(e)}')            

            except NoSuchElementException:
                print('Could not make that move')

    def has_turn(self):
        try:
            player_board_layout = self.driver.find_element(By.ID, "board-layout-player-bottom")
            try:
                player_board_layout.find_element(By.CLASS_NAME, "clock-player-turn")
                return True
            except NoSuchElementException:
                return False
        except NoSuchElementException:
            print('Could not check for turn.')
            return False

    def is_agent_white(self):
        try:
            player_board_layout = self.driver.find_element(By.ID, "board-layout-player-bottom")
            try:
                player_board_layout.find_element(By.CLASS_NAME, "clock-white")
                return True
            except NoSuchElementException:
                return False
        except NoSuchElementException:
            print('Could not get color.')
            return 'NA'

    def click_new_10_min(self):
        try:
            new_10_min_btn = self.driver.find_element(By.XPATH, "//*[contains(text(), 'New 10 min')]")
            print('Play again button found.')
            self.action.move_to_element(new_10_min_btn).click().perform()
            print('Clicked Play again')
        except NoSuchElementException:
            print('Play again button not found')