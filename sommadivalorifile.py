#inizializzo una lista vuota per salvare i valori
values = []

#apro e leggo il file linea per linea
my_file = open('sales.txt', 'r')
sum = 0

for line in my_file:

    #faccio lo split del file linea per linea
    elements = line.split(',')

    #se non sto procedendo l'intestazione
    if elememts [0] != 'date':

        #setto la data e il valore
        date = elements[0]
        value = elements[1]

        #aggiungo alla lista dei valori questo valore
        values.append(float(value))

print(my_file.read())





    
