class Model():
    def fit(self, data):
        raise NotImplementedError ('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError ('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        if type(data) != list:
            raise TypeError ('Inserire una lista')
       

        for item in data:
            if(len(data))<=2:
                 raise Exception ('Metti più dati')
            
            if data == None:
                raise Exception ("Non hai passato nessun dato")

            if not isinstance(item, int) and not isinstance (item, float):
                raise TypeError ("I dati non sono numeri")
        
            incr_medio = 0
            prediction = 0
            prec = data[0]

            for item in data [1:]:
                incr_medio += item - prec
                prec = item

            prediction = incr_medio/(len(data)-1) + data[-1]
        
        return prediction


class FitIncrementModel(IncrementModel):
    def fit(self, data):
        incr_prec = 0
        predict_prec = 0
        prec = data[0]

        for item in data[1:]:
            
            incr_prec += item - prec
            prec = item
        predict_prec = incr_prec/(len(data)-1)

        self.global_avg_increment = predict_prec
    

    def predict(self, data):
        predict_3 = super().predict(data)
        predict_3 -= data[-1]

        try:
            prediction = (predict_3 + self.global_avg_increment)/2 + data[-1]
        except AttributeError:
            print("Non hai effettuato il fit")
            prediction = predict_3 + data[-1]

        return prediction
        

Increment_model = IncrementModel()
dati_sold = [50,52,60]

Fit_Increment_Model = FitIncrementModel()
fit_dati_sold = [8,19,31,41]

#richiamare la funzione fit
#mettere i dati dentro (lista)
Fit_Increment_Model.fit(fit_dati_sold)
print(Fit_Increment_Model.predict(dati_sold))
print(Increment_model.predict(dati_sold))




        
       




