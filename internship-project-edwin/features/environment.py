import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from app.application import Application
from support.logger import logger


def browser_init(context, scenario_name):
    """
    :param scenario_name:
    :param context: Behave context
    """
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    ### HEADLESS MODE ####
    # driver_path = GeckoDriverManager().install()
    # options = webdriver.FirefoxOptions()
    # options.add_argument('headless')
    # service = FirefoxService()
    # context.driver = webdriver.Firefox(
    #     options=options,
    #     service=service
    # )

    ### BROWSERSTACK ###
    bs_user = 'edwinderavil_9QAIl7'
    bs_key = 'JzfDmfVePgvjWQ7YJmLy'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
        "os": "Windows",
        "osVersion": "11",
        'browserName': 'Firefox',
        'browserVersion': '128.0',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)
    context.driver.wait = WebDriverWait(context.driver, 15)

    # context.driver.maximize_window()
    # context.driver.implicitly_wait(5)
    # context.driver.wait = WebDriverWait(context.driver, 15)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
