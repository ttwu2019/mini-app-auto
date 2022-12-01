from case.pages.homepage import HomePage
from case.base import para


# import time


class HomeFlow(HomePage):
    """小程序首页方法流程"""

    def check_homepage_path(self):
        self.mini.assertEqual(self.get_current_path(), para.homepage_route)

    def check_homepage_popup(self):
        self.mini.assertTrue(self.get_popup())
