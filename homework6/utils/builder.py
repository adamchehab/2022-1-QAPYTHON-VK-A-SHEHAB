from models.models import ReqByType
from models.models import Top10Req
from models.models import Top5Req4XX
from models.models import Top5Req5XX
from models.models import TotalReq


class MysqlBuilder:

    def __init__(self, client):
        self.client = client

    # Task 1
    def fill_total_req(self, dic):
        data = TotalReq(
            count=list(dic.keys())[0]
        )
        self.client.session.add(data)
        self.client.session.commit()

    # Task 2
    def fill_req_by_type(self, dic):
        for i in range(len(dic)):
            data = ReqByType(
                req_type=list(dic.keys())[i],
                req_count=list(dic.values())[i],
            )
            self.client.session.add(data)
        self.client.session.commit()

    # Task 3
    def fill_top10_req(self, dic):
        for i in range(len(dic)):
            data = Top10Req(
                req=list(dic.keys())[i],
                req_count=list(dic.values())[i],
            )
            self.client.session.add(data)
        self.client.session.commit()

    # Task 4
    def fill_top5_req_4xx(self, dic):
        for i in range(len(dic)):
            data = Top5Req4XX(
                    ip=list(dic.keys())[i].split()[0],
                    req=list(dic.keys())[i].split()[1],
                    code=list(dic.keys())[i].split()[2],
                    req_len=list(dic.values())[i]
            )
            self.client.session.add(data)
        self.client.session.commit()

    # Task 5
    def fill_top5_req_5xx(self, dic):
        for i in range(len(dic)):
            data = Top5Req5XX(
                    ip=list(dic.keys())[i],
                    ip_count=list(dic.values())[i]
            )
            self.client.session.add(data)
        self.client.session.commit()
