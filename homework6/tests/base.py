import pytest
from mysql.client import MysqlClient
from utils.builder import MysqlBuilder


class MyTest:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_client):
        self.mysql: MysqlClient = mysql_client
        self.builder: MysqlClient = MysqlBuilder(self.mysql)
