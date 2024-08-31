from all_pages.main_page import MainPage
from all_pages.base_page import Page
from all_pages.off_plan import OffPlan
# from all_pages.off_plan import OffPlan


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)
        self.main_page = MainPage(driver)
        self.off_plan = OffPlan(driver)

