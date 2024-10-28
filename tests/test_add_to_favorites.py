import pytest
from pages.main_page import Main
from pages.project_main_page import Project


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestProjectSearch:
    def test_add_to_favorites(self, browser):
        main_page = Main(browser)
        main_page.click_first_project()
        project_page = Project(browser)
        project_page.click_and_check_style_favorite_button()
        project_page.click_and_check_my_favorites_project()
