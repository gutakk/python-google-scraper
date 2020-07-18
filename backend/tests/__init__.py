import os
import time
import unittest

import psycopg2
from database import init_db
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


class NimbleBaseTestCase(unittest.TestCase):
    def setUp(self):
        time.sleep(0.1)
        self.pg_host = os.environ['POSTGRES_HOST']
        self.pg_user = os.environ['POSTGRES_USER']
        self.pg_password = os.environ['POSTGRES_PASSWORD']
        self.pg_db = os.environ['POSTGRES_DB']

        self.cnx = psycopg2.connect(user=self.pg_user, password=self.pg_password, host=self.pg_host)
        self.cur = self.cnx.cursor()
        self.cnx.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.cur.execute("CREATE DATABASE {db_name};".format(db_name=self.pg_db))
        self.cnx.commit()

        self.engine = create_engine(
            f'postgresql://{os.environ["POSTGRES_USER"]}:{os.environ["POSTGRES_PASSWORD"]}@{os.environ["POSTGRES_HOST"]}:5432/{os.environ["POSTGRES_DB"]}', 
            convert_unicode=True
        )
        self.db_session = scoped_session(sessionmaker(autocommit=False,
                                                autoflush=False,
                                                bind=self.engine))
        self.Base = declarative_base()
        self.Base.query = self.db_session.query_property()

        init_db(self.engine)


    def tearDown(self):
        self.cur.execute("""
            SELECT pg_terminate_backend(pid)
            FROM pg_stat_activity
            WHERE datname = %s;
        """, [self.pg_db])

        self.cur.execute("DROP DATABASE {db_name};".format(db_name=self.pg_db))

        self.cur.close()
        self.cnx.close()
