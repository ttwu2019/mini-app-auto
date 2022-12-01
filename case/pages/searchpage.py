from case.base.basepage import BasePage
from case.base.baseselector import BaseSelector


class SearchPage(BasePage):
    """小程序搜索页公共方法"""

    locators = {
        "SEARCH_INPUT_CLICK": '.input',
        "SEARCH_INPUT": '.input',
        "SEARCH_BUTTON": '.searchBtn',
        "LAB_RESULTS_TEXT": '.one_right_one'
    }

    """搜索框输入值"""

    def input_search(self, text):
        BaseSelector.waitToInput(self, SearchPage.locators['SEARCH_INPUT'], text)

    """点击搜索按钮"""

    def click_search_btn(self):
        BaseSelector.waitToClick(self, SearchPage.locators['SEARCH_BUTTON'])

    """取得搜索结果的文本"""

    def get_result_texts(self):
        texts = BaseSelector.waitToGetTexts(self, SearchPage.locators['LAB_RESULTS_TEXT'])
        return texts

    """点击服务进入服务详情"""

    def click_service(self):
        BaseSelector.waitToClick(self, SearchPage.locators['LAB_RESULTS_TEXT'])
