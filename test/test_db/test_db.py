import unittest
from unittest import mock
import src.db.db_connection
from src.db.db_connection import *
from src.db.get_db import *

class Db_testing(unittest.TestCase):

    def test_connection(self):
        conn = create_connection()
        self.assertTrue(conn)

        conn.close()

    @mock.patch('src.db.db_connection.sqlite3')
    def test_connection_error(self, mock_sql):
        mock_sql.connect.side_effect = src.db.db_connection.Error
        conn = create_connection()
        self.assertFalse(conn)

    def test_get_random_fighter(self):
        datas = get_random_fighter()
        self.assertTrue(datas)

        #test the uniqueness of each fighter
        for data in datas:
            datas.pop(datas.index(data))
            self.assertNotIn(data, datas)

    def test_get_random_team(self):
        datas = get_random_team()
        self.assertTrue(datas)

        #test the uniqueness of each data
        for data in datas:
            datas.pop(datas.index(data))
            self.assertNotIn(data, datas)
