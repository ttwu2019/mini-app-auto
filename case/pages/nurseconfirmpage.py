from case.base.basepage import BasePage
from case.base.baseselector import BaseSelector


class NurseConfirmPage(BasePage):
    """小程序护士服务公共方法"""

    locators = {
        "SELECT_TIME": '.changeTime',

        "TO_ADDRESS_LIST": '.placeTwo_itme_right',
        "SELECT_ADDRESS": '.adib-title',

        "TO_USERINFO": '.placeTwo_itme_right',
        "SELECT_USERINFO": '.data-v-8b8873fc',

        "TO_INPUT_DEMO": '.placeThree_ul_right',
        "REBOX_DEMO": '.reBoxRea',
        "DEMO_CONFIRM_BTN": "view[data-event-opts='tap,succmask,$event']",
        "RADIO_BTN_SERVICE": '.servertip',
        "SUBMIT_BTN": '.submitbtn',
        "ORDER_SUCCESS_LAB": '.ment',
        "LOOK_ORDER": 'view[data-event-opts="tap,gotopage,2"',  # 查看订单
        "RETURN_TOP_PAGE": 'view[data-event-opts="tap,gotopage,1"'  # 返回首页
    }

    """点击立即预约按钮"""

    def click_select_time(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['SELECT_TIME'])

    def confirm_service_time(self):
        BaseSelector.pick_time(self, 'picker')

    def click_select_addr(self):
        BaseSelector.waitToClicks(self, NurseConfirmPage.locators['TO_ADDRESS_LIST'], 0)

    def click_addr(self):
        BaseSelector.waitToClicks(self, NurseConfirmPage.locators['SELECT_ADDRESS'], 0)

    def click_select_userinfo(self):
        BaseSelector.waitToClicks(self, NurseConfirmPage.locators['TO_USERINFO'], 1)

    def click_userinfo(self):
        BaseSelector.waitToClicks(self, NurseConfirmPage.locators['SELECT_USERINFO'], 4)

    def click_select_demo(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['TO_INPUT_DEMO'])

    def input_demo(self, text):
        BaseSelector.waitToInput(self, NurseConfirmPage.locators['REBOX_DEMO'], text)

    def click_demo_confirm_btn(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['DEMO_CONFIRM_BTN'])

    def click_service_radio_btn(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['RADIO_BTN_SERVICE'])

    def click_submit_btn(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['SUBMIT_BTN'])

    def is_order_success(self):
        return BaseSelector.waitSelectorIsExist(self, NurseConfirmPage.locators['LOOK_ORDER'])

    # return BaseSelector.waitSelectorIsExist(self, NurseConfirmPage.locators['ORDER_SUCCESS_LAB'])

    def click_look_order(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['LOOK_ORDER'])

    def click_return_top_page(self):
        BaseSelector.waitToClick(self, NurseConfirmPage.locators['RETURN_TOP_PAGE'])
