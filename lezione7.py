#testing
#assertEqual arriva da dove?  
#se una cosa ha self davanti una funzione non e build-in ma deriva da un genitore padre 

import unittest
from lezione7esercizi import somma

class testsomma(unittest.Testcase):
    def test_somma(self):
        self.assertEqual(somma(1,1), 2)
        self.assertEqual(somma(1.5,2.5), 4)


class TestCSVFile(unittest.TestCase):
    def test_init(self):
        csv_file = CSVFile('sales.csv')

        slef.assertEqual(csv_file.name, 'sales.csv')