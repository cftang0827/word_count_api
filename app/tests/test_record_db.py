import unittest
from models import model
import os


class TestRecordModel(unittest.TestCase):

    def test_add_record(self):
        print("make a fake test record db")
        r = model.Record('test', 'www.google.com', 99,
                         'Sat, 09 Mar 2019 13:44:12 GMT')
        r.add()

    def test_query_record(self):
        print("test query")
        r = model.Record('test', 'www.google.com')
        r.query()
        self.assertEqual(r.result, 99, 'write db and read db are not the same')
