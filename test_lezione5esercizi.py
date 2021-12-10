import unittest
from lezione5esercizi import CSVFile

class testcsvfile(unittest.TestCase):
    def test_Excpetions(self):
        with self.assertRaises(Exception):
            csv_file = CSVFile('sals.csv')
        