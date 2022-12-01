import time

from case.pages.searchpage import SearchPage
from case.pages.nurseservicepage import NurseServicePage
from case.pages.nurseconfirmpage import NurseConfirmPage
from case.pages.nurorderdetailpage import NurOrderDetailPage
from case.flows.searchflow import SearchFlow


class NurseOrderFlow(SearchPage, NurseServicePage, NurseConfirmPage, NurOrderDetailPage):
    """小程序护士订单相关方法流程"""

    def check_order_success(self, text, demo):
        # """通过首页搜索找到护士服务"""
        # SearchFlow.search_flow(self, text)
        # SearchPage.click_service(self)
        #
        # """护士服务详情页面操作"""
        # time.sleep(10)
        # NurseServicePage.click_to_buy_btn(self)
        # time.sleep(10)
        # self.allow()
        #
        # time.sleep(10)
        # NurseServicePage.click_to_order_btn(self)
        #
        # """护士订单确认页面操作"""
        # # NurseConfirmPage.click_select_time(self)
        # NurseConfirmPage.confirm_service_time(self)
        # NurseConfirmPage.click_select_addr(self)
        # NurseConfirmPage.click_addr(self)
        # NurseConfirmPage.click_select_userinfo(self)
        # NurseConfirmPage.click_userinfo(self)
        # NurseConfirmPage.click_select_demo(self)
        # NurseConfirmPage.input_demo(self, demo)
        #
        # NurseConfirmPage.click_demo_confirm_btn(self)
        # NurseConfirmPage.click_service_radio_btn(self)
        # NurseConfirmPage.click_submit_btn(self)
        #
        # """检查护士订单下单成功"""
        # self.mini.assertTrue(NurseConfirmPage.is_order_success(self))

        # ====================================================================================

        """通过首页搜索找到护士服务"""
        SearchFlow.search_flow(self, text)
        self.click_service()

        """护士服务详情页面操作"""
        self.click_to_buy_btn()
        self.allow()
        self.click_to_order_btn()

        """护士订单确认页面操作"""
        # NurseConfirmPage.click_select_time(self)
        self.confirm_service_time()
        self.click_select_addr()
        self.click_addr()
        self.click_select_userinfo()
        self.click_userinfo()
        self.click_select_demo()
        self.input_demo(demo)

        self.click_demo_confirm_btn()
        self.click_service_radio_btn()
        self.click_submit_btn()

        # self.click_look_order()
        """检查护士订单下单成功"""
        self.mini.assertTrue(NurseConfirmPage.is_order_success(self))

    def cal_order(self):
        """护士订单下单成功页面进入订单详情-取消订单"""
        self.click_cal_order_btn()
        self.click_cal_confirm_btn()
