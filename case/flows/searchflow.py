from case.base.basepage import BasePage
from case.pages.searchpage import SearchPage
from case.pages.homepage import HomePage
from case.base import para


# import time


class SearchFlow(HomePage, SearchPage):
    """小程序首页方法流程"""

    def check_homepage_path(self):
        self.mini.assertEqual(self.get_current_path(), para.homepage_route)

    def search_flow(self, text):
        HomePage.click_top_search(self)
        self.input_search(text)
        self.click_search_btn()

    def check_search_results(self, text):
        texts = self.get_result_texts()
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        print(texts)
        for i in range(len(texts)):
            self.mini.assertContainTexts(texts[i], text)
