import minium
import time
import datetime


class BaseSelector(minium.MiniTest):
    """元素操作基类"""

    """等待元素出现然后点击"""

    def waitToClick(self, selector):
        self.mini.page.wait_for(selector)
        ele = self.mini.page.get_element(selector)
        ele.tap()

    def waitToClicks(self, selector, index):
        self.mini.page.wait_for(selector)
        ele = self.mini.page.get_elements(selector)
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print(len(ele))
        ele[index].tap()

    """等待元素出现然后输入"""

    def waitToInput(self, selector, text):
        self.mini.page.wait_for(selector)
        ele = self.mini.page.get_element(selector)
        ele.input(text)

    """等待元素出现然后取得文本内容"""

    def waitToGetTexts(self, selector):
        self.mini.page.wait_for(selector)
        ele = self.mini.page.get_elements(selector)
        text_list = []
        for i in range(len(ele)):
            text_list.append(ele[i].inner_text)
        print(text_list)
        return text_list

    def pick_time(self, selector):
        self.mini.page.wait_for(selector)
        ele = self.mini.page.get_element(selector)
        ele.click()
        current_year = time.localtime().tm_year
        current_month = time.localtime().tm_mon
        current_day = time.localtime().tm_mday
        current_hour = time.localtime().tm_hour
        current_min = time.localtime().tm_min
        ele.pick(str(current_year) + '-' + str(current_month) + '-' + str(current_day))
        ele.pick(str(current_hour + 5) + ':' + str(current_min))

        # curr_time = datetime.datetime.now()
        # current_year = curr_time.year
        # current_month = curr_time.month
        # current_day = curr_time.day
        # current_hour = curr_time.hour
        # current_min = curr_time.minute

    def waitSelectorIsExist(self, selector):
        return self.mini.page.wait_for(selector, 20)


