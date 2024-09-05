from all_pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    user_field = (By.CSS_SELECTOR, "#email-2")
    pass_field = (By.CSS_SELECTOR, "#field")
    log_btn = (By.CSS_SELECTOR, '[class="login-button w-button"]')
    off_plan_btn = (By.XPATH, '//div[text()="Off-plan"]')

    def open_reely(self):
        self.open_url('https://soft.reelly.io/sign-in')

    def login_reely(self):
        user_log = 'edwinjenell@gmail.com'
        pass_log = 'Edupunk67'
        self.input_text(user_log, *self.user_field)
        self.input_text(pass_log, *self.pass_field)
        self.click(*self.log_btn)

    def click_off_plan(self):
        self.click(*self.off_plan_btn)


