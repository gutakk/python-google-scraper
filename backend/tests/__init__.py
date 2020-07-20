import os
import time
import unittest

import controllers.data
import controllers.file
import controllers.index
import controllers.user
import psycopg2
from database import init_db
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

        self.cnx = psycopg2.connect(dbname=self.pg_db, user=self.pg_user, password=self.pg_password, host=self.pg_host)
        self.cur = self.cnx.cursor()

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
            DELETE FROM data;
            DELETE FROM file;
            DELETE FROM users;
        """)
        self.cnx.commit()
        self.cur.close()
        self.cnx.close()

        self.db_session.close()
        self.engine.dispose()
