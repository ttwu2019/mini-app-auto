from case.base.basepage import BasePage
from case.base.baseselector import BaseSelector


class HomePage(BasePage):
    """小程序首页公共方法"""

    locators = {
        "TOP_ELEMENT": '.data-v-ec48ec48"',
        "TOP_ELEMENT_CAL": 'view[class="closeBtn data-v-ec48ec48"]',
        "TOP_SEARCH_INPUT": 'view[class="uh-bottom data-v-ec48ec48"]',
    }

    """获取当前页面路径"""

    def get_current_path(self):
        return self.current_path()

    """取得首页弹窗元素"""

    def get_popup(self):
        return self.mini.page.element_is_exists(HomePage.locators['TOP_ELEMENT'])

    """关闭首页弹窗"""

    def close_popup(self):
        # 关闭弹窗
        BaseSelector.waitToClick(self, HomePage.locators['TOP_ELEMENT_CAL'])

    """点击首页搜索输入框"""

    def click_top_search(self):
        BaseSelector.waitToClick(self, HomePage.locators['TOP_SEARCH_INPUT'])
