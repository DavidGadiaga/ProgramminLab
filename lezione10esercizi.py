from lezione9esercizio import FitIncrementModel
from lezione5esercizi import NumericalCSVFile


file_controllo = NumericalCSVfile("CSVFile")
vendite = file_controllo.get_data()
vendite_prima = []
vendite_dopo = []

for item in vendite[:24]:
    vendite_prima.append(item)
for item in vendite[24:]:
    vendite_dopo.append(item)

print(vendite_prima)
print(vendite_dopo)