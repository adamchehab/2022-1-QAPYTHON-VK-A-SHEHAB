import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.orm import sessionmaker
from models.models import Base


class MysqlClient:
    def __init__(self, user, password, db, host="127.0.0.1", port=3306):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

        self.connection = None
        self.engine = None
        self.session = None

    def connect(self, db_created=True):
        db = self.db if db_created else ""
        url = f"mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{db}"

        self.engine = sqlalchemy.create_engine(url, encoding='utf8')
        self.connection = self.engine.connect()

        session = sessionmaker(bind=self.connection.engine)
        self.session = session()

    def create_db(self):
        self.connect(db_created=False)
        self.execute_query(f"DROP database IF EXISTS {self.db}")
        self.execute_query(f"CREATE database {self.db}")

    def create_table(self, table_name):
        if not inspect(self.engine).has_table(table_name):
            Base.metadata.tables[table_name].create(self.engine)
    
    def execute_query(self, query, fetch=False):
        result = self.connection.execute(query)
        if fetch:
            return result.fetchall()
