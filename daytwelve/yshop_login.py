import requests
import unittest
import time
import re
from utils.HTMLtestRunner import HTMLTestRunner


class YShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = requests.session()

    @classmethod
    def tearDownClass(cls):
        cls.lj = r'D:/pycharm/pythonwenjian/first'
        cls.mlj = unittest.defaultTestLoader.discover(start_dir=cls.lj, pattern='jiekou.py')
        cls.nowtime = time.strftime("%Y-%m-%d-%H-%M-%S")
        cls.wjm = cls.nowtime + 'yshop.html'
        cls.wj = open(cls.wjm, 'wb')
        cls.run = HTMLTestRunner(stream=cls.wj, title='yshop测试', tester='yang', description='测试如下')
        cls.run.run(cls.mlj)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test1(self):
        url = 'http://150.158.171.135:8008/api/login'
        header = {'Content-Type':'application/json'}
        data = {'password': 123456, 'spread': '', 'username': 18811111111}
        p = self.session.post(url=url, headers=header, json=data)
        print(p.text)
        res = re.findall('"token":"(.+)"},', p.text)
        print(res[0])
        # global res1
        res1 = 'Bearer '+res[0]
        return res1

    def test2(self):
        url1 = 'http://150.158.171.135:8008/api/cart/add'
        header1 = {'Content-Type': 'application/json', 'Authorization': self.test1()}
        data1 = {"productId": 15, "cartNum": 1, "new": 0, "uniqueId": "91cc6a8adec04492846716b0330bcc6f"}
        p1 = self.session.post(url=url1, json=data1, headers=header1)
        print(p1.text)


if __name__ == '__main__':
    unittest.main()

