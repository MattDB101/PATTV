from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

DRIVER_PATH = './drivers/chromedriver/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
service = Service(executable_path=DRIVER_PATH)

def check_user(username):
    try:
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(f'https://www.twitch.tv/{username}')
        live_status = driver.find_element(By.CLASS_NAME, 'channel-status-info--offline')

        if (live_status):
            print(f'\n{username} is offline.\n')
            return False
        
    except NoSuchElementException: 
            print(f'\n{username} is online.\n')
            return True
        
    finally:
        driver.quit()
        