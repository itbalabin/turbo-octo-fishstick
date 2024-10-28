import pytest
from pages.main_page import Main
from pages.project_main_page import Project


@pytest.mark.regression
@pytest.mark.usefixtures('user_login')
class TestProjectSearch:
    def test_smoke_project_page(self, browser):
        main_page = Main(browser)
        main_page.click_first_project()
        project_page = Project(browser)
        project_page.check_about_author()
        project_page.check_blog()
        project_page.check_author_community()
        project_page.check_support_button()
        project_page.click_blog_button()
        project_page.leave_and_check_comment()
        project_page.click_and_check_support_button()
