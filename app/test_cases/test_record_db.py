import unittest
from models import model
import os
'''
Test case as db integration test
'''


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

    def test_query_no_record(self):
        r = model.Record('test2', 'www.googlegoogle.com')
        r.query()
        self.assertIs(r.result, None, 'Not none for dismatch')
