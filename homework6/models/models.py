from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    __tablename__ = None
    __table_args__ = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)


# Task 1
class TotalReq(BaseModel):
    __tablename__ = 'total_req'

    count = Column(Integer, nullable=False)


# Task 2
class ReqByType(BaseModel):
    __tablename__ = 'req_by_type'

    req_type = Column(String(10), nullable=False)
    req_count = Column(Integer, nullable=False)


# Task 3
class Top10Req(BaseModel):
    __tablename__ = 'top10_req'

    req = Column(String(100), nullable=False)
    req_count = Column(Integer, nullable=False)


# Task 4
class Top5Req4XX(BaseModel):
    __tablename__ = 'top5_req_4xx'

    ip = Column(String(100), nullable=False)
    req = Column(String(100), nullable=False)
    code = Column(String(5), nullable=False)
    req_len = Column(Integer, nullable=False)

# Task 5
class Top5Req5XX(BaseModel):
    __tablename__ = 'top5_req_5xx'

    ip = Column(String(100), nullable=False)
    ip_count = Column(Integer, nullable=False)


# total_req
# req_by_type
# top10_req
# top5_req_4xx
# top5_req_5xx

# headers=["TOTAL"]
# headers=["TYPE", "COUNT"]
# headers=["REQUEST", "COUNT"]
# headers=["IP", "URL", "CODE", "LEN"]
# headers=["IP", "COUNT"]
