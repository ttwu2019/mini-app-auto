# coding=utf-8

from case.base import para
from case.base.basecase import BaseCase
from case.flows.nurseorderflow import NurseOrderFlow

"""
小程序首页测试
"""


class NurseOrderTest(BaseCase):
    def __init__(self, methodName='runTest'):
        super(NurseOrderTest, self).__init__(methodName)
        self.nurseOrderFlow = NurseOrderFlow(self)

        """
         case4:搜索页面的搜索结果是否正确
        """

    def test_04_check_nurse_order_success(self):
        print("检查护士下单成功==================")
        self.nurseOrderFlow.check_order_success(para.search_text, para.service_demo)
