import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest

sys.path.append('./interface')
sys.path.append('./db_fixture')
from db_fixture import blog_test_data

# 指定测试用例为当前文件夹下的 interface 目录
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == "__main__":
    blog_test_data.init_data() # 初始化接口测试数据
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='博客接口测试报告',
                            description='Implementation Example with: ')
    runner.run(discover)
    fp.close()
