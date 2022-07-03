from utils.selenium_chrome_driver import BaseDriver
from selenium.webdriver.support.select import Select
import random


class TestStudent(BaseDriver):
    def test_one(self):
        time = self.get_time()
        const = self.get_const()
        dr = self.get_chrome_driver_init("file:///D:/pcf/download/qq/student_msg.html")
        select_list = dr.find_elements("name", "subject")
        for i in range(1, len(select_list)):
            index = random.randint(0, len(select_list)-1)
            time.sleep(0.5)
            item = select_list.pop(index)
            item.click()
        time.sleep(1)
        school = dr.find_element("id", "school")
        options = dr.find_elements("xpath", '//*[@id="school"]/option')
        option_index = random.randint(0, len(options)-1)
        Select(school).select_by_index(option_index)
        time.sleep(10)


test = TestStudent()
test.test_one()

