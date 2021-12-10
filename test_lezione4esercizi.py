import unittest
from lezione4esercizi import CSVFile

#output giusto
class testcsvfile(unittest.TestCase):
    def test_get_data(self):
        csv_file = CSVFile('sales_test.csv')
        expectation = [['01-01-2012', '266.0'],['01-02-2012', '145.9']]
        #aperta chiusa parentesi perchè funzione
        self.assertEqual(csv_file.get_data(), expectation)

    def test_name_file(self):
        csv_file = CSVFile('sales.txt')
        self.assertEqual(csv_file.name, 'saless.txt')

    
    

