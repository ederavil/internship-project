from all_pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class OffPlan(Page):
    off_plan_sign = (By.CSS_SELECTOR, '[class="menu-text-link-leaderboard w--current"]')
    filter_btn = (By.CSS_SELECTOR, '[class="filter-button w-inline-block"]')
    filter_choice_btn = (By.CSS_SELECTOR, '[data-name="#comletion-select"]')
    future_choice = (By.XPATH, '//option[text()="2025"]')
    apply_filter_btn = (By.CSS_SELECTOR, '[wized="applyFilterButton"]')
    future_tags = (By.XPATH, '//div[contains(., "2025")]')

    def verify_off_plan_page(self):
        self.driver.find_element(*self.off_plan_sign)

    def filter_for_future_launch(self):
        sleep(3)
        self.wait_and_click(*self.filter_btn)
        sleep(6)

        self.wait_and_click(*self.filter_choice_btn)
        self.wait_and_click(*self.future_choice)
        self.wait_and_click(*self.apply_filter_btn)

    def verify_future_launch_tags(self):
        self.driver.find_elements(*self.future_tags)

