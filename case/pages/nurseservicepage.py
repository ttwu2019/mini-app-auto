from case.base.basepage import BasePage
from case.base.baseselector import BaseSelector


class NurseServicePage(BasePage):
    """小程序护士服务公共方法"""

    locators = {
        "TO_BUY_BTN": '.tobuy',
        "TO_ORDER": '.btmright'
    }

    """点击立即预约按钮"""

    def click_to_buy_btn(self):
        BaseSelector.waitToClick(self, NurseServicePage.locators['TO_BUY_BTN'])

    """允许提醒"""

    def allow_pop(self):
        self.allow()

    def click_to_order_btn(self):
        BaseSelector.waitToClick(self, NurseServicePage.locators['TO_ORDER'])
