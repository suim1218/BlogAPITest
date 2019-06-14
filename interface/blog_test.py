# -*- coding: utf-8 -*-
import requests
import unittest
from parameterized import parameterized


class BlogTest(unittest.TestCase):

    def setUp(self):
        self.url = "http://127.0.0.1:8000/"
        self.username = 'admin'
        self.password = '123456'

    def tearDown(self):
        pass

    @parameterized.expand([
        ("01", "", "admin111111", 0, 'username or password null'),
        ("02", "admin", "", 0, "username or password null"),
        ("03", "", "", 0, "username or password null"),
        ("04", "admin1", "admin111111", 0, "username or password error"),
        ("05", "admin", "admin1111112", 0, "username or password error"),
        ("06", "admin1", "admin1111112", 0, "username or password error"),
        ("07", "admin", "123456", 1, "login success"),
    ])
    def test_login(self, testcase_number, username, password, status, msg):
        url = self.url + 'login'
        payload = {'username': username, 'password': password}
        self.result = requests.post(url, payload).json()
        # print(self.result)
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], msg)

    def test_request_type_error(self):
        url = self.url + 'login'
        payload = {'username': self.username, 'password': self.password}
        self.result = requests.get(url, payload).json()
        # print(self.result)
        self.assertEqual(self.result['status'], 0)
        self.assertEqual(self.result['message'], 'request type error')

    @parameterized.expand([
        ("01", "", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("02", "1", "", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("03", "2", "乡愁", "", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("04", "3", "乡愁", "余光中", '', 0, 'id or title or author or content null'),
        ("05", "5", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         1, "add article success"),
        ("06", "1", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         0, "article id already exists"),
        ("07", "3", "乡愁标题过长大于10个字符", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         0, '文章标题过长'),
        ("08", "4", "乡愁", "余光中作者名称过长大于10个字符", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         0, '作者名称过长'),

    ])
    def test_create_blog(self, testcase_number, b_id, title, author, content, status, msg):
        """使用参数化测试创建blog"""
        url = self.url + 'add_article'
        payload = {'id': b_id, 'title': title, 'author': author, 'content': content}
        self.result = requests.post(url, payload).json()
        # print(self.result)
        # self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], msg)

    @parameterized.expand([
        ("01", "10", 1, 'delete article success'),
        ("02", "11", 0, 'id not exist'),
        ("03", "aa", 0, '参数类型错误'),

    ])
    def test_delete_blog(self, testcase_number, b_id, status, msg):
        """使用参数化测试删除blog 先创建一个blog"""

        create_blog_url = self.url + 'add_article'
        payload = {'id': '10', 'title': '乡愁',
                   'author': '余光中', 'content': '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头'}
        requests.post(create_blog_url, payload).json()

        url = self.url + 'delete_article'
        payload = {'id': b_id}
        self.result = requests.post(url, payload).json()
        # print(self.result)
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], msg)

    @parameterized.expand([
        ("01", "", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("02", "12", "", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("03", "12", "乡愁", "", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         'id or title or author or content null'),
        ("04", "12", "乡愁", "余光中", '', 0, 'id or title or author or content null'),
        ("05", "12", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头1',
         1, "modify article success"),
        ("06", "12", "乡愁标题过长大于10个字符", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         0, '文章标题过长'),
        ("07", "12", "乡愁", "余光中作者名称过长大于10个字符", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头',
         0, '作者名称过长'),
        ("08", "aa", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0,
         '参数类型错误'),
        ("09", "13", "乡愁", "余光中", '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头', 0, 'article not exist'),
    ])
    def test_modify_blog(self, testcase_number, b_id, title, author, content, status, msg):
        """使用参数化测试修改blog 先创建一个blog"""

        create_blog_url = self.url + 'add_article'
        payload = {'id': '12', 'title': '乡愁',
                   'author': '余光中', 'content': '小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头'}
        requests.post(create_blog_url, payload).json()

        url = self.url + 'modify_article'
        payload = {'id': b_id, 'title': title, 'author': author, 'content': content}
        self.result = requests.post(url, payload).json()
        # print(self.result)
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], msg)

    def test_query_blog(self):
        """查询blog, 不带条件"""

        create_blog_url = self.url + 'add_article'
        payload = {'id': '14', 'title': '采蘑菇',
                   'author': 'testDog', 'content': '采蘑菇的小姑娘，背着一个大箩筐'}
        requests.post(create_blog_url, payload).json()

        url = self.url + 'get_article'
        payload2 = {}
        self.result = requests.post(url, payload2).json()
        # print(self.result)
        self.assertEqual(self.result['status'], 1)
        self.assertEqual(self.result['message'], 'success')

    def test_query_title_blog(self):
        """根据标题查询blog"""
        title = "跳皮绳"
        create_blog_url = self.url + 'add_article'
        payload = {'id': '15', 'title': title,
                   'author': 'testDog', 'content': '采蘑菇的小姑娘，喜欢跳皮绳'}
        self.result = requests.post(create_blog_url, payload).json()
        # print(self.result)
        url = self.url + 'get_article'
        payload = {"title": title}
        self.result = requests.post(url, payload).json()
        # print(self.result)
        self.assertEqual(self.result['status'], 1)
        self.assertEqual(self.result['message'], 'success')
        self.assertEqual(self.result['data'][0]['title'], title)


if __name__ == '__main__':
    unittest.main()
