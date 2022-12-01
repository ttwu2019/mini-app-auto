from case.base.basepage import BasePage
from case.base.baseselector import BaseSelector


class NurOrderDetailPage(BasePage):
    """小程序护士订单详情公共方法"""

    locators = {
        "CAL_ORDER_BTN": "button[data-event-opts='tap,bindCanlefix,$0,detailinfo.orduid']",
        "CAL_CONFIRM_BTN": "view[data-event-opts='tap,bindcancelOrder,$event']",
    }

    def click_cal_order_btn(self):
        BaseSelector.waitToClick(self, NurOrderDetailPage.locators['CAL_ORDER_BTN'])

    def click_cal_confirm_btn(self):
        BaseSelector.waitToClick(self, NurOrderDetailPage.locators['CAL_CONFIRM_BTN'])
