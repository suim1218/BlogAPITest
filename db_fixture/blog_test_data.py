import sys
import time

sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

# create data
data = {
    # 对应数据库表字段

    'article_article': [
        {
            'id': "1",
            'title': "乡愁",
            'author': "余光中",
            'content': "小时候，乡愁是一枚小小的邮票，我在这头，母亲在那头。长大后，乡愁是一张窄窄的船票，我在这头，新娘在那头",
            'date_publish': '2019-05-31 08:55:15.056780'}
    ]

}


# insert
def init_data():
    DB().init_data(data)


if __name__ == '__main__':
    init_data()
