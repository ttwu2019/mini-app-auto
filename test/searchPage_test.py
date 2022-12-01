# coding=utf-8


# from case.base import loader
from case.base import para
from case.base.basecase import BaseCase
from case.flows.searchflow import SearchFlow

"""
小程序首页测试
"""


class SearchPageTest(BaseCase):
    def __init__(self, methodName='runTest'):
        super(SearchPageTest, self).__init__(methodName)
        self.searchFlow = SearchFlow(self)

    """
     case3:搜索页面的搜索结果是否正确
    """
    def test_03_page_search_result(self):
        print("检查搜索页搜索==================")
        self.searchFlow.search_flow(para.search_text)
        self.searchFlow.check_search_results(para.search_text)


# if __name__ == "__main__":
#     loader.run(module="test.searchPage_test", config="../config.json", generate_report=True)
