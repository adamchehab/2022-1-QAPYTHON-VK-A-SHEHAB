from base import MyTest
from script.script import parse_log


from models.models import ReqByType
from models.models import Top10Req
from models.models import Top5Req4XX
from models.models import Top5Req5XX
from models.models import TotalReq


class TestMySql(MyTest):
    d_list = parse_log()

    # Task 1
    def test_total_req(self, t_name="total_req", t_model=TotalReq):
        d = self.d_list[t_name]
        self.mysql.create_table(t_name)
        self.builder.fill_total_req(d)
        rows_count = self.mysql.session.query(t_model).count()
        assert rows_count == len(d)

    # Task 2
    def test_req_by_type(self, t_name="req_by_type", t_model=ReqByType):
        d = self.d_list[t_name]
        self.mysql.create_table(t_name)
        self.builder.fill_req_by_type(d)
        rows_count = self.mysql.session.query(t_model).count()
        assert rows_count == len(d)

    # Task 3
    def test_top10_req(self, t_name="top10_req", t_model=Top10Req):
        d = self.d_list[t_name]
        self.mysql.create_table(t_name)
        self.builder.fill_top10_req(d)
        rows_count = self.mysql.session.query(t_model).count()
        assert rows_count == len(d)

    # Task 4
    def test_top5_req_4xx(self, t_name="top5_req_4xx", t_model=Top5Req4XX):
        d = self.d_list[t_name]
        self.mysql.create_table(t_name)
        self.builder.fill_top5_req_4xx(d)
        rows_count = self.mysql.session.query(t_model).count()
        assert rows_count == len(d)

    # Task 5
    def test_top5_req_5xx(self, t_name="top5_req_5xx", t_model=Top5Req5XX):
        d = self.d_list[t_name]
        self.mysql.create_table(t_name)
        self.builder.fill_top5_req_5xx(d)
        rows_count = self.mysql.session.query(t_model).count()
        assert rows_count == len(d)
