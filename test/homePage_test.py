# coding=utf-8

from case.base.basecase import BaseCase
from case.flows.homeflow import HomeFlow

"""
小程序首页测试
"""


class HomePageTest(BaseCase):
    def __init__(self, methodName='runTest'):
        super(HomePageTest, self).__init__(methodName)
        self.homeFlow = HomeFlow(self)

    """
     case1:判断是否进入小程序首页
    """
    def test_01_home_page_path(self):
        print("检查当前页面路径++++++++++++")
        self.homeFlow.check_homepage_path()

    """
     case2:判断首页弹窗是否存在
    """
    def test_02_page_base_popup(self):
        print("检查首页有弹窗==================")
        self.homeFlow.check_homepage_popup()


# if __name__ == "__main__":
#     loader.run(module="test.homePage_test", config="../config.json", generate_report=True)
