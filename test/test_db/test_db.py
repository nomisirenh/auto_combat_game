import unittest
from unittest import mock
from src.db.db_conection import *
from src.db.get_db import *

class Db_testing(unittest.TestCase):

    def test_connection(self):
        conn = create_connection()
        self.assertTrue(conn)
        conn.close()

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

if __name__ == '__main__':
    unittest.main()