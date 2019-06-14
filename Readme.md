### 介绍
后台系统接口自动化测试

### 环境
* Python3
* request
* HTMLTestRunner
* unittest
* parameterized

### 目录介绍
* db_fixture 数据库初始化
* interface 测试用例
* report 测试报告
* db_config 数据库配置信息

### 运行
* 单个测试文件运行
~~~
python *_case.py //interface 目录下
~~~

* 批量运行
~~~
python run_test.py //根目录下
~~~