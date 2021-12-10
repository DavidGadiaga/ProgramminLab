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
        t = 60

        for i in range(1,len(lista)):
            if(len(lista))<2:
                raise Exception ('Metti più dati')

            print(i)
    
            incremento += lista[i] - lista[i-1]

        media = incremento/(len(lista)-1)
        prediction = t+media
        
        return prediction

lista = [50,52,60]
my_model = IncrementModel()

print(my_model.predict(lista))
