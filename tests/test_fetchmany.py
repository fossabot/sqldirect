import unittest
import os
import logging
import sys
from dotenv import load_dotenv

from sqldirect import SQLiteConnection as DbConnection
from sqldirect import Dictionary

class TestFetchMany(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # specify exact path to avoid use wrong .env in some other folder
        load_dotenv("../.env")


    def setUp(self):
        self.conn = DbConnection(os.getenv("CONNECTION_STRING"))

    def test_dict(self):
        dictionary = self.conn.fetchone("select 'a' as a, 1 as b", Dictionary({'a': 'A', 'b': 'B'}))
        self.assertEqual({'A': 'a', 'B': 1}, dictionary)


    def tearDown(self):
        self.conn.close()


    @classmethod
    def tearDownClass(cls):
        pass

#
# if __name__ == "__main__":
#     logging.basicConfig(stream=sys.stdout, level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
#     unittest.main()
