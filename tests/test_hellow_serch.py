import pytest
from pages.main_page import Main
from locators.base_page import BasePage
from pages.project_main_page import Project
from pages.search_main_page import Search


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestSearch:
    def test_hellow_search(self, browser):
        main_page = Main(browser)
        main_page.click(BasePage.PROJECT_SECTION_BUTTON)
        project_page = Project(browser)
        project_page.input_to_search_on_project_page()
        search_page = Search(browser)
        search_page.count_project_and_posts_check()
        search_page.click_first_project()
