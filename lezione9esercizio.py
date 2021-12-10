class Model():
    def fit(self, data):
        raise NotImplementedError ('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError ('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        if type(data) != list:
            raise TypeError ('Inserire una lista')
        incremento = 0
        media = 0
        ultimo_elemento = data[-1]

        for i in range(1,len(lista)):
            if(len(lista))<2:
                 raise Exception ('Metti più dati')
    
            incremento += lista[i] - lista[i-1]

        media = incremento/(len(lista)-1)
        prediction = ultimo_elemento +media
        
        return prediction


class FitIncrementModel(IncrementModel):
    def fit(self, data):
        if type(data) != list:
            raise TypeError ('Inserire una lista')
        incremento = 0
        media = 0
        ultimo_elemento = data[-1]

        for i in range(1,len(lista)):
            if(len(lista))<2:
                raise Exception ('Metti più dati')
    
            incremento += lista[i] - lista[i-1]

        media = incremento/(len(lista)-1)
        predicion = ultimo_elemento + media

        self.global_avg_increment = media
    


    def predict(self, data):
        if type(data) != list:
            raise TypeError ('Inserire una lista')
        incremento = 0
        media = 0
        ultimo_elemento = data[-1]

        for i in range(1,len(lista)):
            if(len(lista))<2:
                raise Exception ('Metti più dati')
    
            incremento += lista[i] - lista[i-1]

        media = incremento/(len(lista)-1)

        return ((self.global_avg_increment + media)/2)+data[-1]
        

lista = [8,19,31,41,50,52,60]
my_model = FitIncrementModel()
#richiamare la funzione fit
#mettere i dati dentro (lista)
my_model.fit(lista)
print(my_model.predict(lista))

        
       




