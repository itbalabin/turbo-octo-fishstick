from pages.base import Base
from locators.search_page import SearchPage
from data.assertions import Assertions
from playwright.sync_api import Page


class Search(Base):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def count_project_and_posts_check(self):
        text_post = self.get_text(SearchPage.LIST_OF_POSTS_BUTTON, 0)
        text_project = self.get_text(SearchPage.LIST_OF_PROJECT_BUTTON, 0)

        assert text_post.strip(
        ) == 'Посты (1)', f"Ожидался текст 'Посты (1)', но найден '{text_post.strip()}'"
        assert text_project.strip(
        ) == 'Проекты (1)', f"Ожидался текст 'Проекты (1)', но найден '{text_post.strip()}'"

    def click_first_project(self):
        self.click_first_element(SearchPage.PROJECT)
