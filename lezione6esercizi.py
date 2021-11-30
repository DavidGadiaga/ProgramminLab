class CSVFile():

    def __init__(self, name):
      
        #alzare un'ecezione
        self.name = name
        #atrributo name della classe sia una stringa
        if not isinstance(self.name,str):
            raise Exception('ho generato a questo errore {}'.format(self.name))
    

    def get_data(self, start= None, end= None):
    
        all_data = []

        #sanitizzazione del codice 1) controllo int
        #se inserisco una styringa con dei numeri cerco di convertirla ad intero 
        if type(start) == str:
            if start.isdigit() == True:
                start = int(start)
        if type(start) == float:
            start = int(start)
         #se le sanificazioni non sono riuscite, blocco il programma
        if not isinstance(start,int):
                raise Exception('"{}" non è un intero ma di tipo "{}"'.format(start, type(start)))

        #stessa cosa con end
        if type(end) == str:
            if end.isdigit() == True:
                end = int(start)
        if type(end) == float:
            end = int(end)
        if not isinstance(end,int):
                raise Exception('"{}" non è un intero ma di tipo "{}"'.format(end, type(end)))    

        file_csv = open('sales.txt', 'r')
        count=0

        for line in file_csv:

            if(start==None and end==None):
                line = line.strip('\n')
                elemento = line.split(',')
                if(elemento[0] != 'Date'):
                    all_data.append(elemento)
        
            elif start<=count<=end:
                line = line.strip('\n')
                elemento = line.split(',')
                if(elemento[0] != 'Date'):
                    all_data.append(elemento)
            count = count+1

            
               

   
        file_csv.close()
        return all_data
        

myfile = CSVFile('sales.csv')
print(myfile)
print(myfile.name)
print(myfile.get_data(5.3,5849930), sep = '\n')