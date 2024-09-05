from all_pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class OffPlan(Page):
    off_plan_sign = (By.CSS_SELECTOR, '[class="menu-text-link-leaderboard w--current"]')
    filter_btn = (By.CSS_SELECTOR, '[data-name="Location 2"]')
    on_sale_choice = (By.XPATH, '//option[text()="On Sale"]')
    on_sale_tags = (By.CSS_SELECTOR, '[class="commision_box"]')
    on_sale_txt = (By.CSS_SELECTOR, '[wized="projectStatus"]')

    def verify_off_plan_page(self):
        self.driver.find_element(*self.off_plan_sign)

    def filter_for_future_launch(self):
        self.click(*self.filter_btn)
        sleep(5)
        self.click(*self.on_sale_choice)

    def verify_future_launch_tags(self):
        expected_text = "On sale"
        product_check = 0
        sleep(4)
        tags = self.driver.find_elements(*self.on_sale_tags)
        for tag in tags:
            tag_txt = self.driver.find_element(*self.on_sale_txt).text
            if tag_txt == expected_text:
                product_check += 1
                if product_check > 23:
                    print(f"All of the {product_check} products are checked and contain the correct tag.")
            else:
                print("A tag is not displayed as intended")