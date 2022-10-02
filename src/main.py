import time

from agent import Agent

agent = Agent()

agent.init_window()
agent.start_match_from_main_url()


# ----- Close the window -----
time.sleep(10)
agent.close_window()