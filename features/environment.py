from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
#Chrome
    service = ChromeService("C:\\Users\\belar\\Automation\\python-selenium-automation\\chromedriver.exe")
    context.driver = webdriver.Chrome(service=service)

#Firefox
    #binary_path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
    #options = webdriver.FirefoxOptions()
    #options.binary_location = binary_path
    #service = FirefoxService("C:\\Users\\belar\\Automation\\internship\\geckodriver.exe")
    #context.driver = webdriver.Firefox(options=options, service=service)

    ## HEADLESS MODE CHROME####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # context.driver = webdriver.Chrome(chrome_options=options, service=Service("C:\\Users\\belar\\Automation\\python-selenium-automation\\chromedriver"))

    ## HEADLESS MODE FIREFOX####
     #options = webdriver.FirefoxOptions()
     #options.add_argument('--headless')
     #context.driver = webdriver.Firefox(options=options, service=Service("C:\\Users\\belar\\Automation\\internship\\geckodriver"))

#Safari
    # context.browser = webdriver.Safari()

    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(driver=context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
