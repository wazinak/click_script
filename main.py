from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from time import sleep
import name


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1600,1400")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-blink-features=AutomationConrtolled")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                            " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.3")
driver = webdriver.Chrome(service=service, options=chrome_options)

user_agent = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/74.0.3729.169 Safari/537.36')
headers = {'User-Agent': user_agent}


def move_to_element(driver: WebDriver, element: WebElement | WebDriver) -> None:
    try:
        webdriver.ActionChains(driver).move_to_element(element).perform()
    except StaleElementReferenceException:
        pass


def element_click(driver: WebDriver | WebElement, path: str) -> bool:
    try:
        driver.find_element(By.XPATH, path).click()
        return True
    except:
        return False


def main():
    url = 'https://h3llo.cloud/ru'
    driver.get(url)
    sleep(1)
    element_click(driver, name.cookie_window)
    sleep(1)
    move_to_element(driver, driver.find_element(By.XPATH, name.switcher_btn))
    element_click(driver, name.switcher_btn)
    count_ass_click = 0
    while True:
        element_click(driver, name.ass_btn)
        count_ass_click += 1
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        print('Послали в жопу', count_ass_click, 'раз(а)')


if __name__ == "__main__":
    main()