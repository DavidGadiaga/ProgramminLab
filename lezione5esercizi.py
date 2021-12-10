class CSVFile:

    #inizializzo classe con nome del file
    def __init__(self, name):
        #attributo name
        self.name = name
        try:

            my_file = open(self.name, 'r')
        
        except Exception as e:
            print('Non esiste il file!')
            print('Ho avuto un errore generico: {}".'.format(e))
    
    #metodo restituisce una lista di liste conteneti i dati(sono stringhe)
    def get_data(self):

        #lista che conterrà i dati
        all_data = []
        #apro file
        file_csv = open('sales.txt', 'r')

        #guardo il file linea per linea
        for line in file_csv:
            #la salvo in all_data, con le modifiche del caso
            line = line.strip('\n')
            elemento = line.split(',')
            if(elemento[0] != 'Date'):
                all_data.append(elemento)
        
        #chiudo il file e ritorno all_data
        file_csv.close()
        return all_data


myfile = CSVFile('sales.csv')
print(myfile)
print(myfile.name)
print(*myfile.get_data(), sep = '\n')


#super().get_data
class NumericalCSVFile(CSVFile):
    def __init__(self, name):
        self.name = name
        print('Name: {}'.format(self.name))
    
    def get_data(self):
        #definire data 
        all_data = super().get_data() 
        #due cicli for uno per la lista e uno elementi della lista
        values = []
        for my_list in all_data:
            for item in my_list:
                #converto gli item in flaot da aggiungere alla lista
                try:
                    item = float(item)
                    values.append(item)
                except:
                    print('non posso convertire il valore e ho questo errore: "{}".'.format(item))  
        return values
        
my_file = NumericalCSVFile('sales.csv')
print('Dati: {}'.format(my_file.get_data()))


